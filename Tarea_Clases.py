class Computadora:

    marca = ""
    procesador = ""
    sistema_operativo = ""
    memoria_ram = 0

    def __init__(self, marca, procesador, sistema_operativo, memoria_ram ):
        self.marca = marca
        self.procesador = procesador
        self.sistema_operativo = sistema_operativo
        self.memoria_ram = memoria_ram

    def __str__(self):
        return "Marca : {} \nProcesador : {}\n" \
               "Sistema Operativo : {} \nCapacidad Ram : {} GB" \
               "".format(self.marca, self.procesador, self.sistema_operativo, self.memoria_ram)

    def aumentado_ram(self, cantidad):
        memoria_ram = self.memoria_ram + cantidad
        return memoria_ram

    def cambiar_so(self, nuevo_so):
        sistema_operativo = nuevo_so
        print(sistema_operativo)

print("*************** CLASE COMPUtADORA ************************")
comp = Computadora("Hp" , "Intel Core i7", "Windows", 4)
print(comp)
print("Nueva capacidad de memoria RAM : " + str(comp.aumentado_ram(4)))
comp.cambiar_so("Linux")
print("*********************************************************\n \n")


class Libro:

    def __init__(self, titulo, nro_paginas, editorial, año_dur):
        self.titulo = titulo
        self.nro_paginas = nro_paginas
        self.editorial = editorial
        self.año_dur = año_dur

    def __str__(self):
        return "Titulo : {} \nNro Paginas : {} \nEditorial : {} \nAño de recorrido: {}".format(self.titulo, self.nro_paginas, self.editorial, self.año_dur)

    def hoja_perdida(self, perdido):
        nro_paginas = self.nro_paginas - perdido
        if nro_paginas > 0:
            return nro_paginas
        else:
            return 0

    def tiempo_recorrido(self):
        año_dur = self.año_dur + 1
        return año_dur

print("*************** CLASE LIBRO ************************")
lib = Libro("Harry Potter", 200, "Salamanca", 6)
print(lib)
print("Cantidad de hojas actuales : " + str(lib.hoja_perdida(2)))
print("Ya paso 1 año mas : " + str(lib.tiempo_recorrido()))
print("*********************************************************\n \n")

class Cocina:

    def __init__(self, marca, nro_ornilla, tipo, sc_horno):
        self.marca = marca
        self.nro_ornilla = nro_ornilla
        self.tipo = tipo
        self. sc_horno = sc_horno

    def imprimir(self):
        return "Marca: {}\nNumero de ornillas : {}\nTipo: {}\nTiene horno : {}" \
               "".format(self.marca, self.nro_ornilla, self.tipo, self.sc_horno)

    def encendido(self):
        print("Cocina Encendida")

    def apagado(self):
        print("Cocina Apagada")

print("*************** CLASE COCINA ************************")
coc = Cocina("LG", 4, "De gas", "SI")
print(coc.imprimir())
coc.encendido()
coc.apagado()
print("*********************************************************\n \n")

class Celular:

    def __init__(self, marca, modelo, color, m_interna, m_externa):
        self.marca = marca
        self.modelo = modelo
        self. color = color
        self.m_interna = m_interna
        self.m_externa = m_externa

    def imprime(self):
        print("Marca : {} \nModelo : {} \nColor : {} \nCapacidad Memoria Interna : {} \n"
              "Capacidad Memoria Externa : {}".format(self.marca, self.modelo,
                                                       self.color, self.m_interna, self.m_externa))

    def cambiar_color(self, n_color):
        color= n_color
        return color

    def cambiar_capacidad_me(self, n_mem):
        m_externa = n_mem
        return m_externa

    def apagado(self):
        print ("Celular Apagado")

    def encendido(self):
        print("Celular Encendido")

print("*************** CLASE CELULAR ************************")
cel = Celular("Samsung", "Galaxy S10", "Negro", 128, 128)
cel.imprime()
cel.encendido()
print("Nuevo Color : " + cel.cambiar_color("Blanco"))
print("Nueva Capacidad de Memoria Externa : " + str(cel.cambiar_capacidad_me(512)))
cel.apagado()
print("*********************************************************\n \n")
