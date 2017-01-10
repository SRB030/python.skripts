class passwordkeeper:

     def inppass(self):
         while 1:
             try:
                inputpass = input('password:')
                passretain = open('password.txt', 'w')
                passretain.write(inputpass + '\n')
                break
             except SystemError:
                 print('пароль не введен повторите попытку')



myclass = passwordkeeper()
myclass.inppass()



