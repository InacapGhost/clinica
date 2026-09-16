from paciente import Paciente

def main(): 
    #crear paciente con el constructor __int__
    p1 = Paciente("11.111.111-1", "franco suarez", 40, "isapre")
    #mostrar informacion del paciente
    #__str_ es llamado automaticamente al imprimir el objeto
    print(p1)
if __name__ == "__main__":
    main()