
# See https://yaml.readthedocs.io/en/latest/
from ruamel import yaml

js_str = """
{
 "name": "the_pipeline",
 "steps": [
  {
   "name": "step1",
   "activity": "do_something"
  }
 ]
}
"""

d = yaml.safe_load(js_str)
print(d)

y_str = """
name: the_pipeline
steps:
   - name: step1
     activity: do_something
"""

y = yaml.safe_load(y_str)
print(y)

