class Car:
    def __init__(self, licensePlate, color, turnedOn):
        self.__licensePlate = licensePlate
        self.__color = color
        self.__turnedOn = turnedOn

    def __str__(self):
        return f"{self.__licensePlate} {self.__color} {self.__turnedOn}"