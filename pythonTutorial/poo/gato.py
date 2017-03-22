class Gato(object):
    """docstring for Gato."""
    def __init__(self, energia, hambre):

        self.energia = energia
        self.hambre= hambre
        print ('se creo un Gato')
    def tomar_leche(self, leche_en_litros):
        self.hambre= self.hambre + leche_en_litros
        print ('toma leche_en_litros')
    def acariciar(self):
        print ('prrrrr')
    def jugar(self):
        if self.energia<=0 or self.hambre <=1:
            print ('el gato no quiere jugar')
        else:
            self.energia -=1
            self.hambre -=2
            print ('juega')

    def dormir(self, horas):
        self.energia+=horas
        print ('Zzzzzzz')


gato= Gato(5,5)
gato.acariciar()
gato.jugar()
gato.jugar()
gato.jugar()
gato.tomar_leche(4)
print (gato.hambre)
print (gato.energia)
