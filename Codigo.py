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
        Cf_Mcu=(self.__cf/Cu)
        comprobacion=(piezas*self.__pv)
        print("Calculando Respuestas...")
        time.sleep(5)


        print("*"*20,"Datos:","*"*20)
        print(f"Precio de Venta Unitario:{self.__pv}")
        print(f"Costos Variables :{self.__cv}")
        print(f"Contribucion Marginal :{Cm}")
        print(f"% Contribucion Unitario : {Cu}")
        print(f"Costos Fijos :{self.__cf}")
        print("*"*40)
        print("PE Uds")
        print(f"CF/MCU :{piezas}")
        print("*"*40)
        print("PE Ingresos")
        print(f"CF/%MCU :{Cf_Mcu}")
        print("*"*50)

        print("Graficando Grafica...")
        time.sleep(5)
        

