class Borg:
    """Borg design pattern"""

    _shared_data = {}  # Attribute dict

    def __init__(self):
        self.__dict__ = self._shared_data  # Make an attribute dict


class Singleton(Borg):

    """The singleton class"""

    def __init__(self, **kwargs):
        Borg.__init__(self)
        self._shared_data.update(kwargs)  # Update the dict with new key-val pair

    def __str__(self) -> str:
        return str(self._shared_data)  # Returns the attribute dict for printing


# Create a singleton object and add first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")

# Print object
print(x)

# Create another singleton object
# ad another acronym
y = Singleton(SNMP="Simple Network Management Protocol")

# Print object
print(y)
