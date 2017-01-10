import random

class passwordgeration:

    def generathions(self):
        randoms = random.randint(10000,20000) * 2
        return randoms


class cripto(passwordgeration):

    def generathions(self):
        fors = ascii(super().generathions())
        print('password:',fors)


mygen = cripto()
mygen.generathions()

close = input('press to enter')






