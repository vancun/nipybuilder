"""
"""

from marshmallow import Schema, fields, post_load
from nipybuilder.lib import Namespace

class Config(Namespace):
    pass

class ConfigSchema(Schema):
    parameters = fields.Dict(keys=fields.Str(), values=fields.Str())
    container_path = fields.Str()
    nifi_api_url = fields.Str()
    x_step = fields.Float()
    y_step = fields.Float()

    @post_load
    def _make(self, data):
        return Config(**data)

