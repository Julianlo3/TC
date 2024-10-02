
if __name__ == "__main__":
    #2 Demuestre mediante tablas de verdad las leyes de De Morgan 
# ∧ = Y verdad si los dos son verdad
# ∨ = or falso si las dos son falsos
    print("\nPunto 2 - Leyes de morgan")
#¬ (p Λ q) ⬄ ¬p Ѵ ¬q 
    print("¬ (p Λ q) <=> ¬p Ѵ ¬q \n")

    print("¬ (p Λ q) \n")
    print(["p","q","(p Λ q)","¬ (p Λ q"])
    variables= [True,False];
    resultado1=[];
    for p in variables:
        for q in variables:
            resultado1.append(not(p and q));
            print([p,q,p and q,not(p and q)])


    print("\n(¬p)∨(¬q) \n")
    print(["p","q","(¬p)","(¬q)","(¬p)∨(¬q)"])
    variables= [True,False];
    resultado2=[];
    for p in variables:
        for q in variables:
            resultado2.append((not(p) or not(q)))
            print([p,q,not(p),not(q),not(p) or not(q)])

    if(resultado1==resultado2):
        print("\nSe puede concluir que la ley de morgan: ¬(p Λ q) <=> ¬p Ѵ ¬q  se cumple")
    else:
        print("Algo quedó mal")
        
        print("¬ (p Λ q) <=> ¬p Ѵ ¬q \n")
    #----------------------------------------------------------
    print("¬ (p ∨ q) <=> ¬p Λ¬q \n")

    print("¬ (p ∨ q) \n")
    print(["p","q","(p ∨ q)","¬ (p ∨ q"])
    variables= [True,False];
    resultado1=[];
    for p in variables:
        for q in variables:
            resultado1.append(not(p or q));
            print([p,q,p and q,not(p or q)])

    print("\n(¬p)Λ(¬q) \n")
    print(["p","q","(¬p)","(¬q)","(¬p)Λ(¬q)"])
    variables= [True,False];
    resultado2=[];
    for p in variables:
        for q in variables:
            resultado2.append((not(p) and not(q)))
            print([p,q,not(p),not(q),not(p) and not(q)])

    if(resultado1==resultado2):
        print("\nSe puede concluir que la ley de morgan: ¬(p ∨ q) <=> ¬p Λ ¬q  se cumple")
    else:
        print("Algo quedó mal")
        