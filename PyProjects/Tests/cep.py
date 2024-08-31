import string
import secrets

try:
    numeroCep = int(input("numero de ceps ae: "))

    def teste(ncep):
        
        ceps = []

        cepstr = ""
        numbers = string.digits 
        num = 8
        contador = 4

        while ncep != 0:
            for num in range(num): 
                
                str = secrets.choice(numbers)
                cepstr += str
                
                if contador == 0:
                    cepstr += "-"
                    contador = 4
                else:
                    contador -= 1
            
            num = 8    
            ncep -= 1
            contador = 4
            ceps.append(cepstr)
            cepstr = ""

        print(ceps)


    teste(numeroCep)

except(NameError, ValueError):
    print("faz o bgl direito")
        