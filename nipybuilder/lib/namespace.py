

class Namespace(dict):
    """
    http://code.activestate.com/recipes/577887-a-simple-namespace-class/
    """

    def __init__(self, **data):
        super().__init__(data)

    def __dir__(self):
        return tuple(self)

    def __repr__(self):
        return "%s(%s)" % (type(self).__name__, super().__repr__())

    def __getattribute__(self, name):
        try:
            return self[name]
        except KeyError:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (type(self).__name__, name))

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        del self[name]
        
    def __call__(self, name, *args, **kwargs):
        if (name in self):
            return self[name]
        elif len(args) > 0:
            return args[0]
        elif 'default' in kwargs:
            return kwargs['default']
        else:
            msg = "'%s' object has no attribute '%s'"
            raise AttributeError(msg % (type(self).__name__, name))
