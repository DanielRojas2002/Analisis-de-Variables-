import matplotlib.pyplot as plt 
import time 

class Variables():
    def __init__(self,pv,cv,cf):
        self.__pv=pv
        self.__cv=cv
        self.__cf=cf

    def Calcular(self):
        Cm=(self.__pv-self.__cv)
        Cu=(self.__pv/Cm)
        piezas=(self.__cf/Cm)
        Cf_%Mcu=(self.__cf/Cu)
        comprobacion=(piezas*self.__pv)
