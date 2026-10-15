from companies.manager import Manager

class MegaManager(Manager):
    def __init__(self, name, wage, manageUnit, megaAttr):
        super().__init__(name, wage, manageUnit)
        self.__megaAttr = megaAttr