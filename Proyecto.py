"""
Proyecto final Algoritmos y programacion - William Andres Parada Antonio - Universidad EAN
El objetivo del programa es crear una interfaz que simule algunas opciones de un cajero automatico
como los son las opciones de retirar dinero o tranferirle dinero a otra cuenta bancaria y opciones de actualizacion de datos como el cambio de contraseña
"""
import os #Carpeta para poder limpiar la pantalla (cls) y pausar el programa en un tiempo requerido (pause) por medio del algoritmo
contador=3
saldoI=50000
opcion=0
Usu="William"
contras="Tetris"
Cuentas=[]
Tranferencias=[]
Ingreso=[]

#Funcion para aniadir movimientos de retiro de dinero
def retiro(c: int):
    Tranferencias.append(c) 
                    

#Solicitando usuario y contraseña
while(contador!=0):
    print("Digite el nombre de usuario:")
    Usuario = input()
    print("Digite la contraseña: ")
    Contra= input()

    if (Usuario == Usu and Contra == contras):
        print("Ingresaste correctamente")
        os.system ("pause")
        os.system ("cls")
        break
    else:
        print("\nNombre de usuario y/o contra incorrectas")
        contador -=1
        print("Intentos restantes: ",contador)
        os.system ("pause")
        os.system ("cls")

if(contador==0):
    print("Numero de intentos permitidos terminados, ingrese mas tarde")
    os.system("exit")
else:
    while(opcion != 7):
        #Ingrso al cajero auomatico y listado de opciones
        print("\t||Bienvenido a tu cajero automatico||\t")
        print("Opciones:")
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Transferir dinero")
        print("4. Consultar saldo")
        print("5. Cambio de clave")
        print("6. Ultimos movimientos" )
        print("7. Salir")
        opcion= int(input("Digite la opcion: "))

        #Listado de acciones por opciones
        if(opcion ==1):
            cantidad = int(input("Digite la cantidad de dinero a ingresar: "))
            Ingreso.append(cantidad)
            saldoI += cantidad #Ingresando el dinero a la cuenta
            print("Dinero ingresado correctamente")
            os.system ("pause")
            os.system ("cls")
        elif(opcion ==2):
            cantidad = int(input("Digite la canidad de dinero a retirar: "))
            if(cantidad>saldoI):
                print("Usted no dispone de esta cantidad de dinero")
                os.system ("pause")
                os.system ("cls")
            else:
                saldoI -=cantidad
                retiro(cantidad)
                print("Dinero retirado exitosamente")
                os.system ("pause")
                os.system ("cls")
        elif(opcion == 3):
                Num = int(input("Ingrese el numero de la cuenta donde tranferir: "))
                cantidad = int(input("Digite la canidad de dinero a transfeir: "))
                if(cantidad>saldoI):
                    print("Usted no dispone de esta cantidad de dinero")
                    os.system ("pause")
                    os.system ("cls")
                else:
                    saldoI -= cantidad
                    print("Dinero tranferido a la cuenta",Num,"Exitosamente")
                    Cuentas.append(Num)
                    retiro(cantidad)
                    os.system ("pause")
                    os.system ("cls")
        elif(opcion==4):
            print("El saldo en su cuenta es:",saldoI)
            os.system ("pause")
            os.system ("cls")
        elif(opcion==5):
            Contra= input("Digite la contraseña actual:")
            if(Contra == contras):
                contras=input("Digite la nueva contraseña: ")
                print("Contraseña cambiado exitosamente")
                os.system ("pause")
                os.system ("cls")
            else:
                print("Esa no es la contraseña actual")
                os.system ("pause")
                os.system ("cls")
        elif(opcion==6):
            print("Cuentas a las que se a tranferido:")
            print(Cuentas)
            print("Dinero retirado:")
            print(Tranferencias)
            print("Dinero ingresado: ")
            print(Ingreso)
            os.system ("pause")
            os.system ("cls")
        elif(opcion==7):
            print("Hasta Luego :D")
            os.system("exit")
        else:
            print("La opcion ingresado no existe")
            os.system ("pause")
            os.system ("cls")