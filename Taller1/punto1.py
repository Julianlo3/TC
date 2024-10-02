#1. Sean L1 = {x,y,z}; L2= {0,1}; L3={a,b} resolver
# concatenación
#a. L1 • L2
#b. L3 • L1
#c. L2 • L3 • L1
#d. L1*
#e. (L2 • L3) *
def punto1titulo():
        print("---------------------------------")
        print(" Taller 1 - punto 1 ")
        print(" Sean L1 = {x,y,z}; L2= {0,1}; L3={a,b} resolver")
        print("a. L1 • L2 \n b. L3 • L1 \n c. L2 • L3 • L1  \n d. L1* \n e. (L2 • L3) *)")
        print("----------------------------------")
        
def solucionPunto1():
        L1=["x","y","z"];
        L2=["0","1"]
        L3=["a","b"]
        punto1titulo();
        # a -------------------
        print("a L1 • L2");
        productoCruz2(L1,L2);
        print(productoCruzRe([L1,L2]))
        # b ------------------
        print("\nb L3 • L1");
        productoCruz2(L3,L1);
        #c -------------
        print("\nL2 • L3 • L1");
        productoCruz3(L2,L3,L1);
        #d cerradura de Kleene L1*
        print("\nL1*")
        #productoCruz3(L1,L1,L1)
        CerraduraKleeneNum3(L1);

def CerraduraKleeneNum3(lista):
        cerradura=[];
        cerradura.append("ε");

        for item1 in lista:
            cerradura.append(item1);

        for item1 in lista:
            for item2 in lista:
                cerradura.append(item1+item2);

        for item1 in lista:
            for item2 in lista:
                for item3 in lista:
                    cerradura.append(item1+item2+item3);
        print(cerradura)
        

def productoCruz2(lista1,lista2):
        operacionCruz =[];
        for elemento1 in lista1:
            for elemento2 in lista2:
                operacionCruz.append(elemento1+elemento2);
        resultado= lista1 + lista2 + operacionCruz;
        print(resultado)

def productoCruz3(lista1,lista2,lista3):
        operacionCruz =[];
        for elemento1 in lista1:
            for elemento2 in lista2:
                for elemento3 in lista3:
                    operacionCruz.append(elemento1+elemento2+elemento3);
        resultado= lista1 + lista2 + lista3 + operacionCruz;
        print(resultado)
        
def productoCruzRe(listas=[],index=0):
    if index==len(listas):
        return [[]]
    else:
        listaRecorrer = productoCruzRe(listas,index+1)
        
        resultado =[]
        for elemento1 in listas[index]:
            for elemento2 in listaRecorrer:
                resultado.append([elemento1] + elemento2)
    return resultado




if __name__ == "__main__":
    
    
    
    
    



  

    

    #d cerradura de Kleene L1*
    print("\nL1*")
    #productoCruz3(L1,L1,L1)
    CerraduraKleeneNum3(L1);

    #e (L2 • L3) *
    print("(L2 • L3) * \n");
    print("(L2 • L3)");
    productoCruz2(L2,L3);
