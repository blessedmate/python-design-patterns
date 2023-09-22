import copy


class Prototype:
    def __init__(self) -> None:
        self._objects = {}

    def register_object(self, name, obj):
        """Register an obj"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an obj"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update its attributes"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Car:
    """Product"""

    def __init__(self):
        self.name = "Skylark"
        self.color = "Red"
        self.options = "Ex"

    def __str__(self):
        return "{} | {} | {}".format(self.name, self.color, self.options)


c = Car()
p = Prototype()
p.register_object("skylark", c)

cl = p.clone("skylark")
print(cl)
