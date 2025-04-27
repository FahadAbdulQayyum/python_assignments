class Rich:
    def __init__(self, name, age, netwealth):
        self.name = name                # Public
        self._age = age                 # Protected
        self.__netwealth = netwealth    # Private

e = Rich("Abdul Rehman Bin Auof (R.A)", 50, "$510B")
print(f"Name: {e.name}")      # Accessible
print(f"Age: {e._age}")   # Accessible (protected but not enforced)
# print(f"Net Wealth: {e.__netwealth}")   # Raises AttributeError
print(f"Net Wealth: {e._Rich__netwealth}")  # Name mangling to access private variable