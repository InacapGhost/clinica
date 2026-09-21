from paciente import Paciente
pacientes: list[Paciente] =[]

def agregar_paciente()->None:
    rut = input("ingrese el rut del paciente: ")
    nombre = input("ingrese el nombre del paciente: ")
    edad = int(input("ingrese edad del paciente: "))
    print("previsiones disponibles:")
    print("1.- Fonasa")
    print("2.- isapre")
    prevision = input("Seleccione la prevision del paciente: ")
    if prevision == "1":
                prevision = "Fonasa"
    else: prevision = "isapre"

    paciente = Paciente(rut, nombre, edad, prevision)
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def leer_numero(mensaje:str)-> int:
     while True:
          try:
               numero = int(input(mensaje))
               return numero
          except ValueError:
               print("Por favor, ingrese un número válido.")

         
def menu ()-> int: 
       op=-1
       while op<0 or op>5:
        print("menu de opciones")
        print("1.- Agregar paciente")
        print("2- Editar paciente")
        print("3.- Eliminar paciente")
        print("4.- Imprimir paciente")
        print("5.- Imprimir todos los pacientes")
        print("0.- Salir")
        opcion = leer_numero("Seleccione una opción: ")
        return opcion
def main(): 
    op=-1
    while op!=0:
         op=menu()
         if op==1:
              print("Agregar paciente")
         elif op==2:
              print("Editando paciente")
         elif op==3:
            print ("Eliminado paciente")
         elif op==4:
              print("Imprimiendo un paciente")
         elif op==5:
              print ("Imprimiendo todos los paciente")
         elif op==0: 
              print("saliendo del programa")
    

    
if __name__ == "__main__":
    main()

