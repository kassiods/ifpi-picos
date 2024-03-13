resp='sim'
while resp=='sim':
    a=int(input("Digite um numero:"))
    fatorial=1
    for i in range(1,a+1):
        fatorial=fatorial*i
    print("o fatorial de seu numero é:", fatorial)
    resp=input("Deseja calcular o fatorial de outro numero? (sim/nao)")