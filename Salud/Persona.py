class Persona:
    tipDoc=""
    documento=0
    nombre=""
    apellido=""
    peso=0
    estatura=0
    edad=0
    genero=""

    def pedirDatos(self):
        self.tipoDoc=input("Ingrese tipo de documento: ")
        self.documento=int(input("Ingrese número de documento: "))
        self.nombre=input("Ingrese su nombre: ")
        self.apellido=input("Ingrese su apellido: ")
        self.peso=float(input("Ingrese su peso: "))
        self.estatura=float(input("Ingrese su estatura: "))
        self.edad=int(input("Ingrese su edad: "))
        self.genero=input("Ingrese su genero: ")

    def mostrarpersona(self):
        print("Sus datos registrados son: \nNombre y apellido: ",self.nombre,"",self.apellido,"\nTipo de documento: ",self.tipoDoc,"\nDocumento: ",self.documento,"\nPeso: ",self.peso,"\nEstatura: ",self.estatura," \nEdad: ",self.edad," \nGenero: ",self.genero)

    def calcularlmc(self, estatura, peso):
        estatura2=estatura*estatura
        pesoActual=peso/estatura2
        
        if pesoActual<20:
            print("Su peso esta por debajo de lo ideal, su peso es ",pesoActual)
        elif pesoActual>20 and pesoActual<=25:
            print("Su peso es ideal, su peso es: ",pesoActual)
        elif pesoActual>25:
            print("Tiene sobrepeso, su peso actual es ",pesoActual)
            return pesoActual
    
    def mayorEdad(self,edad):
        if edad>=18:
            print("Usted es mayor de edad")
        elif edad<18 and edad>0:
            print("Usted es menor de edad")
        else:
            print("Dato invalido")
            return edad