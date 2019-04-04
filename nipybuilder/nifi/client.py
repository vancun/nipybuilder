
import nipyapi
from nipybuilder.lib import Namespace


class NiFiClient:
    DEF_API_BASE = 'http://localhost:8080/nifi-api'
    
    def __init__(self, api_base=None):
        self._api_base = api_base if api_base else type(self).DEF_API_BASE
        self._root_pg_id = None
        
    @property
    def _api(self):
        nipyapi.config.nifi_config.host=self._api_base
        return nipyapi
        
    @property
    def root_pg_id(self):
        if self._root_pg_id is None:
            self._root_pg_id = self._api.canvas.get_root_pg_id()
        return self._root_pg_id
        
    def get_root_pg_id(self):
        return self.root_pg_id
        
        
    def get_pg_flow(self, pg_id = 'root'):
        """
        Returns information about NiFi Process Group flow.
        
        Args:
            pg_id(str): Process Group ID.
        Returns:
            (ProcessGroupFlowEntity): Process Group Flow entry details.
        """
        if pg_id == 'root':
            pg_id = self.root_pg_id
        try:
            return self._api.nifi.FlowApi().get_flow(pg_id)
        except self._api.nifi.rest.ApiException as err:
            raise ValueError(err.body)

        
    def get_pg_by_id(self, pg_id):
        if pg_id == 'root': 
            pg_id = self.root_pg_id
        return self._api.nifi.ProcessGroupsApi().get_process_group(pg_id)

    def list_pg_id_for_name(self, name, parent_pg_id='root'):
        if not name:
            id_list = [self.root_pg_id]
        else:
            parent_flow = self.get_pg_flow(parent_pg_id)
            pg_list = parent_flow.process_group_flow.flow.process_groups
            results = filter(lambda pg: pg.component.name == name, pg_list)
            id_list = [pg.component.id for pg in results]
        return id_list

    def get_pg_id_for_name(self, name, parent_pg_id='root'):
        id_list = self.list_pg_id_for_name(name, parent_pg_id)
        if len(id_list) > 1:
            raise Exception('Multiple results found for %s at %s.' % (name, parent_pg_id))
        return id_list[0] if id_list else None
            
            

    def get_pg_id_for_path(self, path):
        if isinstance(path, str):
            path = path.split('/')
        parent_pg_id = self.root_pg_id
        for name in path:
            if name == '':
                continue
            pg_list = self.list_pg_id_for_name(name, parent_pg_id)
            if not pg_list:
                return None
            if len(pg_list) > 1:
                raise Exception('Multiple results found for %s at %s.' % (name, parent_pg_id))
            parent_pg_id = pg_list[0]
        return parent_pg_id
        
        
    def delete_pg(self, pg, force=False):
        assert isinstance(pg, (self._api.nifi.ProcessGroupEntity, str))
        assert isinstance(force, bool)
        if isinstance(pg, str):
            pg = self.get_pg_by_id(pg)
        self._api.canvas.delete_process_group(pg, force, False)
        
    def get_canvas_rect(self, pg='root'):
        flow = self.get_pg_flow(pg).process_group_flow.flow
        
        l,t,b,r = (0,0,0,0)
        
        positions = []
        for entity in ('process_groups', 'remote_process_groups', 'processors', 'input_ports', 'output_ports', 'funnels'):
            positions.extend(item.position for item in getattr(flow, entity))
        if positions:
            l = min(positions, key=lambda pos: pos.x).x
            r = max(positions, key=lambda pos: pos.x).x
            t = min(positions, key=lambda pos: pos.y).y
            b = max(positions, key=lambda pos: pos.y).y
            
        return Namespace(left=l, top=t, right=r, bottom=b)
        
    def create_pg(self, parent_pg, new_pg_name, x, y):
        """
        Creates a new Process Group with the given name under the provided parent
        Process Group at the given Location
        Args:
            parent_pg (ProcessGroupEntity or Str): The parent Process Group to create the
                new process group in
            new_pg_name (str): The name of the new Process Group
            x (float): the x coordinate for the new Process Group under the parent
            x (float): the y coordinate for the new Process Group under the parent
        Returns:
            (ProcessGroupEntity): The new Process Group
        """
        nipyapi = self._api
        assert isinstance(parent_pg, (nipyapi.nifi.ProcessGroupEntity, str))
        assert isinstance(new_pg_name, str)
        assert isinstance(x, (float, int))
        assert isinstance(y, (float, int))
        parent_pg_id = parent_pg if isinstance(parent_pg, str) else parent_pg.id
        try:
            return nipyapi.nifi.ProcessGroupsApi().create_process_group(
                id=parent_pg_id,
                body=nipyapi.nifi.ProcessGroupEntity(
                    revision={'version': 0},
                    component=nipyapi.nifi.ProcessGroupDTO(
                        name=new_pg_name,
                        position=nipyapi.nifi.PositionDTO(
                            x=x,
                            y=y
                        )
                    )
                )
            )
        except nipyapi.nifi.rest.ApiException as e:
            raise e
