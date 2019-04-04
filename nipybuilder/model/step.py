"""
"""

from marshmallow import Schema, fields, post_load
from nipybuilder.lib import Namespace

class Step(Namespace):
	pass


class StepSchema(Schema):
    name = fields.Str(required=True)
    activity = fields.Str(required=True)
    variables = fields.Dict(keys=fields.Str(), values=fields.Str())
    properties = fields.Dict(keys=fields.Str(), values=fields.Dict(keys=fields.Str(), values=fields.Str()))

    @post_load
    def _make(self, data):
        return Step(**data)
