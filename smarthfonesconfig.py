"""
Represents a smartphone with attributes like name, RAM, and storage.

Example usage:

>>> xiaomi = Smartphone("Redmi 9S")
>>> xiaomi.ram = "4GB"
>>> xiaomi.memory = "64GB"
>>> print(f"{xiaomi.name} with {xiaomi.ram} RAM and {xiaomi.memory} storage")
Redmi 9S with 4GB RAM and 64GB storage
"""

class Smarthphone:
    def __init__(self, name):
        self.name = name
        self._ram = None
        self._memory = None

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, valor):
        self._ram = valor

    @property
    def memory(self):
        return self._memory

    @memory.setter
    def memory(self, valor):
        self._memory = valor


class Ram:
    def __init__(self, name):
        self.name = name


class Memory:
    def __init__(self, name):
        self.name = name                

xiaomi = Smarthphone("redmi 9s")
ram = Ram("4gb ram")
memory = Memory("64gb memory")
xiaomi.ram = ram
xiaomi.memory = memory     
print(xiaomi.name, xiaomi.ram.name, xiaomi.memory.name)