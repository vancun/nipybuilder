
import nipybuilder.model as m
from ruamel import yaml

from nipybuilder import Builder


with open('demo/config.yaml', 'r') as f:
    cfg = m.ConfigSchema().load(yaml.safe_load(f))

with open('demo/pipeline.yaml', 'r') as f:
    po = yaml.safe_load(f)
    sc = m.PipelineSchema()
    pipeline = sc.load(po)


b = Builder(cfg)
b.build(pipeline)
