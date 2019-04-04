
"""
Test cases for Action class.
"""

import unittest
from unittest import mock
from nipybuilder.actions import Action, ActionWrapper, ActionContext

class ActionTest(unittest.TestCase):
    def test_create_instance_passes(self):
        act = Action()
        self.assertIsNotNone(act)

# ##############################################
class ActionWrapperTest(unittest.TestCase):

    def test_action_property_returns_action(self):
        action = mock.Mock(spec=Action)
        wrapper = ActionWrapper(action)
        self.assertIs(action, wrapper.action)

    def test_when_called_wrapped_action_execute_is_called_passing_params(self):
        action = mock.Mock(spec=Action)
        wrapper = ActionWrapper(action)
        wrapper('Hi', 'there',when='today')
        action.execute.assert_called_with('Hi','there', when='today')


# ###############################################
class ActionContextTest(unittest.TestCase):
    def test_passed_params_are_set(self):
        ctx = ActionContext(None, params={'name': 'John'})
        self.assertEqual(ctx.param('name'), 'John')
        
    def test_format_with_params_applies_template(self):
        ctx = ActionContext(None, params={'name':'John'})
        self.assertEqual('Hi, John!', ctx.format_with_params('Hi, {name}!'))
    
    def test_format_param_applies_template(self):
        ctx = ActionContext(None, params={'name': 'John', 'greeting':'Hello, {name}!'})
        self.assertEqual(ctx.format_param('greeting'), 'Hello, John!')
        
    def test_update_params_adds_parameter(self):
        ctx = ActionContext(None, params={'name': 'John'})
        ctx.update_params({'city':'Barcelona'})
        self.assertEqual(ctx.param('city'), 'Barcelona')

    def test_update_params_changes_parameter(self):
        ctx = ActionContext(None, params={'name': 'John'})
        ctx.update_params({'name':'Sergio'})
        self.assertEqual(ctx.param('name'), 'Sergio')
