
from .action import Action
import nipybuilder

class InitContainer(Action):
    
    def execute(self, context):
        context.vars.container_pg_id = context.nifi.get_pg_id_for_path(
            context.vars.container_path)
        if not context.vars.container_pg_id:
            raise nipybuilder.NiPyBuilderException("Flow container Process Group '%s' not found." % context.vars.container_path)

