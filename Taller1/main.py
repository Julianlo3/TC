import punto1
import punto2

print("---------------------------------")
print(" Taller 1 ")
print(" Anderson Vinaso - Julián Rojas López")
print("----------------------------------")

opcion = 0;

def mostrarMenu():
    print("Punto 1 - Sean L1= {x,y,z}; L2 = {0,1}; L3 = {a,b}");
    print("Punto 2 - Demuestre mediante tablas de verdad las leyes de De Morgan");
    print("Punto 3 - Vending Machine con monedas de 500,200 y 100");
    print("Ingrese 0 para salir")
 

while opcion!=-1:
    mostrarMenu();
    opcion=input("Ingresa la opcion a realizar:");
    match opcion:
        case "1":
            punto1.punto1titulo();
            punto1.solucionPunto1();
        case "2":
            print("hola")
        case _:
            print("error");
            break;
        
    



