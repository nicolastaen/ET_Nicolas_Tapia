import os
os.system("cls")

#productos = {model: [marca,pantalla,RAM,disco,GB de disco,proce,video]}

productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def opciones(opc_max):
    while True:
        try:
            opcion = int(input("ingrese una opcion: "))
            if 0 < opcion < opc_max:
                return opcion
            else:
                print("opcion invalida")
        except:
            print("opcion invalida\n debe ingresar un numero")
            input("")

def ver_marcas():
    lista = set()

    for i in productos.items():
        lista.add(i[1][0])
    
    for i in lista:
        print(" - ", i)

def Stock_por_marca(marca):
    cantidad = 0
    
    for modelo,datos in productos.items():
        if datos[0].lower() == marca.lower():
            cantidad =+ stock[modelo][1]
    
    print(f"el stock es de {cantidad}")
    input("")

def busqueda_por_precio(p_min,p_max):
    lista = []
    for modelo, (precio,stok) in stock.items():
        if p_min <= precio <= p_max and stok > 0:
            marca = productos[modelo][0]
            lista.append(f"{marca}--{modelo}")
   
    for i in lista:
        print(i)
        input("")

def actualizar_precio(modelo, precio_new):
    while True:
        if modelo in stock:
            stock[modelo][0] = precio_new
            print("Se cambio el precio")
        else:
            print("no se encontro el producto")
        elecion = str(input("quiere cambiar el precio de otro producto? (Si/No)")).lower
        if elecion == "no":
            break

def menu():
    while True:
        os.system("cls")
        print("===== MENU PRINCIPAL =====")    
        print("1.- Stock Marca")
        print("2.- Búsqueda por precio")
        print("3.- Actualizar precio")
        print("4.- Salir")

        elecion = opciones(5)

        if elecion == 1:
            ver_marcas()
            marca = input("Ingrese Marca a consultar: ")
            Stock_por_marca(marca)
        elif elecion == 2:  
            while True:
                try:
                    p_min = int(input("Ingrese precio minimo: "))
                    break
                except:
                    print("debe ingresar un numero")
            while True:
                try:
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except:
                    print("debe ingresar un numero")

            busqueda_por_precio(p_min,p_max)
        elif elecion == 3:
            modelo = input("ingrese el modelo a actualizar: ")
            while True:
                try:
                    p = int(input("Ingrese precio nuevo: "))
                    break
                except:
                    print("debe ingresar un numero")

                actualizar_precio(modelo, p)
        elif elecion == 4:
            print("programa finalizado")
            break

menu()