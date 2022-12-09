import random 

class Usuarios():
    def __init__(self,id: int =0, password:str=' ', dpto:int=0):
        self._id  = id
        self._password = password 
        self._dpto = dpto
   
    def id (self):
        return self._id

    def set_id(self, id: int):
        if type(id) == int:
            self._id = id 
        else:
            raise ValueError("Sorry: the Id property is not integer value ")

    def password(self,):
        return '*' * len(self._password) 

    def set_password(self, pwd:str):
        c = len(pwd)
        if c <= 10 and c >= 4: 
            self._password = pwd
        else: 
            raise ValueError("Sorry: the password length mus not be greater than 10 not less than 4")

    def dpto (self):
        return str(self._dpto)

    def set_dpto (self, dpto_number:int):
        if type(dpto_number) == int:
            if dpto_number in range(1,20):
                self._dpto = dpto_number
        else:
            raise ValueError("Sorry: the departament number property is not integer value ")


def generateString():
    strings = ['a','b','c','d','f','g','h','i','j','k','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    word = ''
    n = random.randrange(4,10)
    for i in range(0,n):
        index = random.randrange(0,len(strings))
        word += strings[index]
    return word

def GenerateUsers(n, registerUsers):
   
    for i in range(0,n):
        id = random.randrange(0,1000000)
        pas = generateString()
        dpto = random.randrange(1,20) 

        try:
            user = Usuarios()
            user.set_id(id)
            user.set_password(pas)
            user.set_dpto(dpto)
            registerUsers.append(user)
        except ValueError:
            n += 1
            continue
    return registerUsers
        

def bubble_sort(v):
    n = len(v)
    for i in range(n-1): 
        ordenado = True
        for j in range(n-i-1):
            if v[j].id() > v[j+1].id():
                ordenado = False
                v[j], v[j+1] = v[j+1], v[j]
        if ordenado:
             break


def getAllUsers(RegisterUsers):
    
    for user in RegisterUsers:
        print('')
        print('*' * 25)
        print(f'ID:     {user.id()}')
        print(f'PWD:    {user.password()}')
        print(f'DPTO:   {user.dpto()}')
        print('*' * 25)

    return None

# tabla hash de dptos agrega los dptos que no se encuentran todavia como key e incrementa su valor si ya existe la key  
def usersXDpto(ResgiterUsers):
    dptos = {f'{i}':0 for i in range(1,21)}

    for user in ResgiterUsers:
        if user.dpto() in list( dptos.keys() ):
            dptos[user.dpto()] += 1

    return dptos 
        

# Realiza uan bsuqueda binaria por id  y uan vez que lo encuentra setea nuevamente el atributo password
def updatepasswordUserXid (rgU, id, newpassword):     
     i, d = 0 , len(rgU) -1
     while i <= d:
        c = (i + d) // 2
        if int(rgU[c].id()) < id:
            i = c + 1
        elif int(rgU[c].id()) > id:
            d = c -1
        else: 
            rgU[c].set_password(newpassword)
            print('')
            print('Update password  ')
            return True
     print('') 
     print(' Id User invalid ')



def menu ():
    print('')
    print('*' * 25)
    print('1- Listar Usuarios ')
    print('2- Usuarios por departamentos')
    print('3- Modificar contraseña')

def main():
    registerUsers = []
    registerUsers = GenerateUsers(20,registerUsers)
    bubble_sort(registerUsers)
    menu()

    aux = True
    op = 0
    while op in range(1,4) or aux :
        aux = False 
        op = int(input('Selecionar una opcion: '))
        if op == 1:
            getAllUsers(registerUsers)
        if op == 2:
            userXDptos =usersXDpto(registerUsers)
            for dptos in userXDptos.items():
                print(f'{dptos} ' )
        if op == 3:
            usuario = int(input('introducir id de usuario : '))
            newpass = input('introducir nueva contraseña: ')
            updatepasswordUserXid(registerUsers,usuario,newpass)
        menu()
    

    
if __name__ == '__main__':
    main()