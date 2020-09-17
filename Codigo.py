import matplotlib.pyplot as plt 
import time 

class Variables():
    def __init__(self,pv,cv,cf):
        self.__pv=pv
        self.__cv=cv
        self.__cf=cf

    def Calcular(self):
        Cm=(self.__pv-self.__cv)
        Cu=(self.__pv-Cm)
        va=(Cm/100)
        piezas=(self.__cf/Cm)
        Cf_Mcu=(self.__cf/va)
        comprobacion=(piezas*self.__pv)
        print("Calculando Respuestas...")
        time.sleep(5)


        print("*"*20,"Datos:","*"*20)
        print(f"Precio de Venta Unitario:{self.__pv}")
        print(f"Costos Variables :{self.__cv}")
        print(f"Contribucion Marginal :{Cm}")
        print(f"% Contribucion Unitario : %{Cu}")
        print(f"Costos Fijos :{self.__cf}")
        print("*"*40)
        print("PE Uds")
        print(f"CF/MCU :{piezas}")
        print("*"*40)
        print("PE Ingresos")
        print(f"CF/%MCU :{Cf_Mcu}")
        print(f"Comprobacion : {comprobacion}")
        print("*"*50)

        print("Graficando Grafica...")
        time.sleep(5)

        nombres=["Precio_Venta","Costo_Variable","Costo_Fijos","Contribucion_Marginal","CF/MCU","CF/%MCU","Comprobacion"]
        valores=[self.__pv,self.__cv,self.__cf,Cm,piezas,Cf_Mcu,comprobacion]
        colores=["red","blue","green","pink","yellow","purple","orange"]
        plt.title("Grafica de Variables")
        plt.bar(nombres,height=valores,color=colores,width=0.5)
        plt.show()



















menu=1
while menu==1:
    print("*"*20,"Bienvenido al Menu ","*"*20)
    pv=float(input("Ingresa el precio de Venta Unitario: "))
    cv=float(input("Ingresa el los Costos Variables : "))
    cf=float(input("Ingresa los Costos Fijos : "))
    objeto=Variables(pv,cv,cf)
    objeto.Calcular()
    print("1=SI\n2=NO")
    menu=int(input("Desea seguir con el programa : "))
