#Este programa tem como intuito simular as funções básicas de uma televisão.

class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentacanal(self):
        if self.ligada:
            self.canal +=1

    def diminuicanal(self):
        if self.ligada:
            self.canal -=1

if __name__ == '__main__':
    televisao = Televisao()
    print(f'A televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'A televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'A televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'A televisão está ligada? {televisao.ligada}')

    print(f'canal: {televisao.canal}')
    televisao.aumentacanal()
    print(f'canal: {televisao.canal}')
    televisao.diminuicanal()
    print(f'canal: {televisao.canal}')

