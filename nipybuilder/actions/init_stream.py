
from .action import Action

class InitStream(Action):
    """
    Initialize NiFi acquisition stream being built.

    Makes sure Process Group for the stream exists:
      * Existing PG with the same name is removed
      * PG for the stream is positioned. 
        * If PG with the same name previously existed, the position
          is preserved.
        * Otherwise is positioned below the left bottom of the canvas
          rectangle.
    """

    def _position_stream(self, ctx):
        if (ctx.vars.stream_pg_id):
            stream_pg = ctx.nifi.get_pg_by_id(ctx.vars.stream_pg_id)
            stream_x = stream_pg.component.position.x
            stream_y = stream_pg.component.position.y
        else:
            rect = ctx.nifi.get_canvas_rect(ctx.vars.container_pg_id)
            stream_x = rect.left
            stream_y = rect.bottom + ctx.vars.y_step
         
        ctx.vars.stream_x = stream_x
        ctx.vars.stream_y = stream_y

    def _setup_stream_pg(self, ctx):
        if (ctx.vars.stream_pg_id):
            ctx.nifi.delete_pg(ctx.vars.stream_pg_id)
        stream_pg = ctx.nifi.create_pg(ctx.vars.container_pg_id,
            ctx.vars.pipeline.name, ctx.vars.stream_x, ctx.vars.stream_y)
        ctx.vars.stream_pg_id = stream_pg.id


    def execute(self, ctx):
        """
        Execute action.
        
        Args:
            ctx (ActionContext): Action context.

        Context Input Vars:
            pipeline - Stream pipeline definition
            container_pg_id - ID of the container Process Group.
            y_step - Vertical step for laying out components

        Context Output Vars:
            stream_pg_id - ID of the stream Process Group.
        """
        assert ctx.vars('pipeline', None), 'Context var pipeline is required'
        assert ctx.vars('container_pg_id', None), 'Context var container_pg_id is required'
        assert ctx.vars('y_step', None), 'Context var y_step'

        ctx.vars.stream_pg_id = ctx.nifi.get_pg_id_for_name(ctx.vars.pipeline.name, 
                ctx.vars.container_pg_id)
        self._position_stream(ctx)
        self._setup_stream_pg(ctx)

