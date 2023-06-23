import sys
from Utilidades import error
from Operaciones import cam_precio, agr_prod, del_prod
# Menus:
# Imprimir Catálogos
def catalogo(diccionario):
    for nombre, precio in diccionario.items():
        print(f"Nombre: {nombre}")
        print(f"Precio: {precio}")
        print()

# Menu Invitados
def menu_inv():
    print("\nMenu:")
    print("============")
    print("Cinturones")
    print("Mochilas")
    print("Monederos")
    print("Bananos")
    print("Contacto")
    print("                                                ")
    print("Opciones:")
    print("============")
    print("Iniciar sesión")
    print("Quitar producto")
    print("Pagar")
    print("Salir\n")

# Mostrar Menú
def mostrar_menu():
    print("\nMenu:")
    print("============")
    print("Cinturones")
    print("Mochilas")
    print("Monederos")
    print("Bananos")
    print("Contacto")
    print("                                                ")
    print("Opciones:")
    print("============")
    print("Quitar producto")
    print("Pagar")
    print("Cerrar sesión")
    print("Salir\n")



# Menus Admins
def mostrar_catalogo_A():
    print("\nCatalogo:")
    print("============")
    print("1-Cinturones")
    print("2-Mochilas")
    print("3-Monederos")
    print("4-Bananos")
    print("5-Volver\n")

def administrar_catalogo():
    print("\nAdministrar")
    print("====================")
    print("1-Modificar producto")
    print("2-Agregar producto")
    print("3-Eliminar producto")
    print("4-Registros")
    print("5-Cerrar sesión")
    print("6-Salir\n")

def m_admin(cin,moc,mon,ban,registro_transacciones):
    while True:
        try:
            administrar_catalogo()
            op_a = int(input("Ingrese el número de la opción: "))

            if op_a == 1:
                op_a = 0
                while True:
                    try:
                        mostrar_catalogo_A()
                        op_a = int(input("Elija la sección a modificar: "))
                        break
                    except ValueError:
                        error(2)

                if op_a == 1:
                    while True:
                        try:
                            catalogo(cin)
                            prod_s = input("Ingrese el nombre del producto: ").strip().lower().capitalize()
                            precio_n = int(input("Ingrese el nuevo precio: "))
                            cam_precio(prod_s, precio_n, cin)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 2:
                    while True:
                        try:
                            catalogo(moc)
                            prod_s = input("Ingrese el nombre del producto: ").strip().lower().capitalize()
                            precio_n = int(input("Ingrese el nuevo precio: "))
                            cam_precio(prod_s, precio_n, moc)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 3:
                    while True:
                        try:
                            catalogo(mon)
                            prod_s = input("Ingrese el nombre del producto: ").strip().lower().capitalize()
                            precio_n = int(input("Ingrese el nuevo precio: "))
                            cam_precio(prod_s, precio_n, mon)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 4:
                    while True:
                        try:
                            catalogo(ban)
                            prod_s = input("Ingrese el nombre del producto: ").strip().lower().capitalize()
                            precio_n = int(input("Ingrese el nuevo precio: "))
                            cam_precio(prod_s, precio_n, ban)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 5:
                    break

            elif op_a == 2:
                op_a = 0
                while True:
                    try:
                        mostrar_catalogo_A()
                        op_a = int(input("Elija la sección a modificar: "))
                        break
                    except ValueError:
                        error(2)

                if op_a == 1:
                    while True:
                        try:
                            catalogo(cin)
                            prod_n = input("Ingrese el nombre del nuevo producto: ").strip().lower().capitalize()
                            prod_p = int(input("Ingrese el precio del nuevo producto: "))
                            agr_prod(prod_n, prod_p, cin)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 2:
                    while True:
                        try:
                            catalogo(moc)
                            prod_n = input("Ingrese el nombre del nuevo producto: ").strip().lower().capitalize()
                            prod_p = int(input("Ingrese el precio del nuevo producto: "))
                            agr_prod(prod_n, prod_p, moc)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 3:
                    while True:
                        try:
                            catalogo(mon)
                            prod_n = input("Ingrese el nombre del nuevo producto: ").strip().lower().capitalize()
                            prod_p = int(input("Ingrese el precio del nuevo producto: "))
                            agr_prod(prod_n, prod_p, mon)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 4:
                    while True:
                        try:
                            catalogo(ban)
                            prod_n = input("Ingrese el nombre del nuevo producto: ").strip().lower().capitalize()
                            prod_p = int(input("Ingrese el precio del nuevo producto: "))
                            agr_prod(prod_n, prod_p, ban)
                            break
                        except ValueError:
                            error(2)
                elif op_a == 5:
                    break

            elif op_a == 3:
                op_a = 0
                while True:
                    try:
                        mostrar_catalogo_A()
                        op_a = int(input("Elija la sección a modificar: "))
                        break
                    except ValueError:
                        error(2)

                if op_a == 1:
                    while True:
                        try:
                            catalogo(cin)
                            prod_n = input("Ingrese el nombre del producto a eliminar: ").strip().lower().capitalize()
                            del_prod(prod_n, cin)
                            break
                        except ValueError:
                            error(2)

                elif op_a == 2:
                    while True:
                        try:
                            catalogo(moc)
                            prod_n = input("Ingrese el nombre del producto a eliminar: ").strip().lower().capitalize()
                            del_prod(prod_n, moc)
                            break
                        except ValueError:
                            error(2)

                elif op_a == 3:
                    while True:
                        try:
                            catalogo(mon)
                            prod_n = input("Ingrese el nombre del producto a eliminar: ").strip().lower().capitalize()
                            del_prod(prod_n, mon)
                            break
                        except ValueError:
                            error(2)

                elif op_a == 4:
                    while True:
                        try:
                            catalogo(ban)
                            prod_n = input("Ingrese el nombre del producto a eliminar: ").strip().lower().capitalize()
                            del_prod(prod_n, ban)
                            break
                        except ValueError:
                            error(2)

                elif op_a == 5:
                    break

            elif op_a == 4:
                for registro in registro_transacciones:
                    print(registro)

            elif op_a == 5:
                op_a = 0
                print("¿Desea cerrar sesión?")
                salir = input("Escriba 'si' o 'no': ").strip().lower()
                if salir == "si":
                    return salir
            elif op_a == 6:
                print("¿Está seguro de salir?")
                salir = input("Escriba 'si' o 'no': ").strip().lower()
                if salir == "si":
                    sys.exit()

        except ValueError:
            error(2)          
    