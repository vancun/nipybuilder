
"""
Test cases for NiPiAction class.
"""

import unittest
from unittest import mock
from nipybuilder.actions import actions, Action, ActionContext
from nipybuilder import NiFiClient
import nipybuilder.model as m
from ruamel import yaml

class NiPiActionTest(unittest.TestCase):
    cfg_yaml = """
        {
            "parameters": {
                "name": "Ivan",
                "greeting": "Hello {name}"
            },
            "x_step": 25,
            "y_step": 35,
            "nifi_api_url": "http://40.68.60.242:8080/nifi-api",
            "container_path": "/container",
        }

    """
    @classmethod
    def setUpClass(cls):
        cls.conf = m.ConfigSchema().load(yaml.safe_load(cls.cfg_yaml))
        cls.ctx = ActionContext(cls.conf)

    def test_config_is_loaded(self):
        actions.init_context(self.ctx)
        self.assertEqual(25, self.ctx.vars.x_step)
        self.assertEqual(35, self.ctx.vars.y_step)
        self.assertEqual("Ivan", self.ctx.param('name'))
        self.assertEqual("http://40.68.60.242:8080/nifi-api", self.ctx.vars.nifi_api_url)
        self.assertIsInstance(self.ctx.nifi, NiFiClient)
        self.assertEqual("/container", self.ctx.vars.container_path)
