
from .action import Action, ActionContext, ActionWrapper

from .init_container import InitContainer
from .init_context import InitContext
from .init_stream import InitStream


from nipybuilder.lib import Namespace

actions = Namespace()
actions.init_container = ActionWrapper(InitContainer())
actions.init_context = ActionWrapper(InitContext())
actions.init_stream = ActionWrapper(InitStream())

