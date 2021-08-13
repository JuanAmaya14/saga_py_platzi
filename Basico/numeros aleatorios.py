import random

def run():
    min = int(input('pon un numero minimo: '))
    max = int(input('pon un numero maximo: '))
    numero_aleatorio = random.randint(min, max)


    print('Un numero del ' + str(min) + ' al ' + str(max))
    print(numero_aleatorio)



if __name__=='__main__':
    run()