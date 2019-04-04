
from .action import Action
from nipybuilder.constants import *
from nipybuilder.nifi import NiFiClient

class InitContext(Action):
    
    def execute(self, context):
        context.vars.x_step = context.conf(CONF_X_STEP, DEF_X_STEP)
        context.vars.y_step = context.conf(CONF_Y_STEP, DEF_Y_STEP)
        context.vars.nifi_api_url = context.conf(CONF_NIFI_API_URL, DEF_NIFI_API_URL)
        context.update_params(context.conf(CONF_PARAMS, {}))
        context.vars.container_path = context.conf(CONF_CONTAINER_PATH, DEF_CONTAINER_PATH)
        context.nifi = NiFiClient(context.vars.nifi_api_url)

