nome1, idade1 = input("digite o primeiro nome e idade: ").split()
nome2, idade2 = input("digite o primeiro nome e idade: ").split()
idade1 = int(idade1)
idade2 = int(idade2)

if idade1 > idade2:
    print(f"{nome1} é o(a) mais velho(a)")
elif idade1 < idade2:
    print(f"{nome2} é o(a) mais velho(a)")
else: 
    print(f"{nome1} e {nome2} possuem a mesma idade.")
