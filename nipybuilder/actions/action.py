"""
Classes for action support: Action, ActionContext and ActionWrapper
"""
from nipybuilder.lib import Namespace


class Action:
    """
    Abstract NiPi action.
    """

    def execute(self, context):
        pass


class ActionWrapper:
    def __init__(self, action):
        self._action = action

    @property
    def action(self):
        return self._action

    def __call__(self, context, *args, **kwargs):
        self._action.execute(context, *args, **kwargs)


class ActionContext():
    def __init__(self, conf, params={}):
        self._conf = conf
        self._params = params
        self._vars = Namespace()

    @property
    def vars(self):
        return self._vars

    @property
    def conf(self):
        return self._conf

    def param(self, name):
        """
        Returns a value associated with a parameter.
        
        Args:
            name (str): The name of the parameter.
        Returns:
            Associated value.
        """
        return self._params[name]
       
    def format_with_params(self, value):
        """
        Returns value formatted with a parameter.
        
        To format value, the string's format_map method is used. params 
        is passed as an argument.
        
        Args:
            value (str): Value to be formatted. Will be cast to string.
        Returns:
            (str) Formatted string with params applied.
        """
        return str(value).format_map(self._params)

    def format_param(self, name):
        """
        Returns formatted value associated with a parameter.
        
        To format param string's format_map method is used. params 
        is passed as an argument.
        
        Args:
            name (str): The name of the parameter.
        Returns:
            (str) Formatted string with applied parameters.
            
        """
        return self.format_with_params(self._params[name])
    
    def update_params(self, param_update):
        """
        Update parameters from a dictionary.
        """
        self._params.update(param_update)


