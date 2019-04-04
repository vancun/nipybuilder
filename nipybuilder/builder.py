
from nipybuilder.actions import ActionContext
from nipybuilder.lib import Namespace
from .nifi import NiFiClient

from nipybuilder.actions import actions

class Builder:
    
    def __init__(self, conf):
        assert isinstance(conf, Namespace), 'conf is not instance of Namespace: %s' % type(conf)
        self._conf = conf

    def build(self, pipeline):
        ctx = ActionContext(self._conf)
        ctx.vars.pipeline = pipeline
        actions.init_context(ctx)
        actions.init_container(ctx)
        actions.init_stream(ctx)     
        print(ctx.vars)   
