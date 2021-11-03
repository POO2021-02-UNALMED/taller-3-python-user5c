from televisores.marca import Marca


class TV:
    numTv = 0

    def __init__(self, marca: Marca, estado: bool) -> None:
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        TV.numTv += 1

    @classmethod
    def setNumTV(cls, numTv):
        cls.numTv = numTv

    def getMarca(self):
        return self._marca

    def setMarca(self, marca: Marca):
        self._marca = marca

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio: int):
        self._precio = precio

    def getVolumen(self):
        return self._volumen

    def setVolumen(self, volumen: int):
        if (0 <= volumen <= 7) and self._estado:
            self._volumen = volumen

    def getCanal(self):
        return self._canal

    def setCanal(self, canal: int):
        if (0 < canal <= 120) and self._estado:
            self._canal = canal

    @classmethod
    def getNumTV(cls):
        return cls.numTv

    # Encender o Apagar el TV
    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False
    
    def getEstado(self):
        return self._estado

    # Controlar canal
    def canalUp(self):
        if self._canal < 120 and self._estado:
            self._canal += 1

    def canalDown(self):
        if self._canal > 1 and self._estado:
            self._canal -= 1

    # Controlar volumen
    def volumenUp(self):
        if self._volumen < 7 and self._estado:
            self._volumen += 1

    def volumenDown(self):
        if self._volumen > 0 and self._estado:
            self._volumen -= 1


    
    