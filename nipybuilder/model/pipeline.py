"""
"""

from marshmallow import Schema, fields, post_load
from nipybuilder.lib import Namespace
from .step import StepSchema

class Pipeline(Namespace):
    pass

class PipelineSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str()
    steps = fields.List(fields.Nested(StepSchema()), required=True)

    @post_load
    def _make(self, data):
        return Pipeline(**data)

