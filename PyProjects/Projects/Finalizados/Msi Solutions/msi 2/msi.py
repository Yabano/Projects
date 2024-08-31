import mysql.connector

db = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "1234",
database = "msi"
)
cursor = db.cursor()

obraDict = {
    "obra1":1,
    "obra2":2,
    "obra3":3,
    "obra4":4
}

class main():

    def printCursor():
        for x in cursor:
            print(x)

    def dbAdd():
        while True:  
            # input de 2 variaveis ( referencia e nome da obra )
            try:
                id = input("digite o id do funcionario e a obra em que se encontra.\n (1) eletricista (2) gerente (3) producao ")

                #faz o typecast de string para int pra iterar na função key
                value = int(input("digite a obra em que o funcionario se encontra.\n (1) obra1 (2) obra2 (3) obra3 "))
                key = list(filter(lambda x: obraDict[x] == value, obraDict))[0]

            except (UnboundLocalError, ValueError):
                print("algo deu errado...")

            cursor.execute("INSERT INTO obras (ref, nomeObra, hora_do_dia) VALUES (%s, %s, CURRENT_TIME())", (id,key))
            db.commit()
            
            q = input("deseja adicionar mais informações no banco? (q) sair (enter) continuar ")           
            if(q == "q" or q == "Q"):
                break
                
        print("\nData base\n") #Printa a table atual
        cursor.execute("SELECT nome, funcao, nomeObra, hora_do_dia FROM funcionarios INNER JOIN obras ON obras.ref = funcionarios.id")
        main.printCursor()
    

class clear():

    def dbClear(): #Deleta  as informações da table
        print("Excluir tudo (1) | Excluir linha: (2) ")
        escolha = input()
        idObra = input("Id da linha a ser deletada")

        if escolha == "1":
            cursor.execute("DELETE FROM obras")
            cursor.execute("ALTER TABLE obras AUTO_INCREMENT=0")
            db.commit()
            print("Delete complete...!")
            db.close()

        elif escolha == "2":
            cursor.execute("DELETE FROM OBRAS WHERE obraID = " +str(idObra))
            db.commit()
            print("Delete complete...!")
            db.close()
        else:
            print("algo deu errado, verifique sua digitação")

class choice():
    print("voce quer adicionar informações ou remover da table?\n adicionar = add; remover = del; sair = q")
    choice = input()

    if choice == "add" or choice == "ADD":
        main.dbAdd()
    elif choice == "del" or choice == "DEL":
        clear.dbClear()
    elif choice == "q" or choice == "Q":
        db.close()
    else:
        print("algo deu errado, verifique a digitação")    

if __name__ == "__main__":
    choice()