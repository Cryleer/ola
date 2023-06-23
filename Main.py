import sys

from Utilidades import tiempo,error
from Pago import pago,GenComp,GenBoleta,GenFactura
from Menus import menu_inv,mostrar_menu,m_admin,catalogo
from Operaciones import agregar_producto,quitar_producto,calcular_iva,calcular_subtotal


#Credenciales de usuarios
usuarios={
    "Ivan": {"contraseña": "Vas", "rol": "cliente"},
    "Constanza": {"contraseña": "Val", "rol": "cliente"},
    "admin": {"contraseña": "admin123", "rol": "admin"}
}

#listas de carrito y registros
carrito=[]
registro_transacciones=[]

#total del carrito
total_c =0
#cantidad de productos del carrito
cantidad_t=0

#arible para elegir comprobante    
Comp=0

#detalle del carrito
carrito_det = {}

#Numero de contacto
contacto="+569 9612 2247"


#Crear diccionarios de cada catalogo
cin = {"Cinturon1": 20000,
    "Cinturon2": 25000,
    "Cinturon3": 15000,}
moc = {"Mochila1": 20000,
    "Mochila2": 25000,
    "Mochila3": 15000,}
mon = {"Monedero1": 20000,
    "Monedero2": 25000,
    "Monedero3": 15000,}
ban = {"Banano1": 20000,
    "Banano2": 25000,
    "Banano3": 15000,}





#Funcion Inicio sesion
def inicio_sesion():
    global total_c, carrito, Comp,iva,subtotal,cantidad_t,op,carrito_det
    while True:
        print("\n---------------BIENVENIDO----------------")
        print("(Si desea salir escriba salir)")
        us = input("/// INGRESE SU USUARIO ///\n")
        if us.lower() == 'salir':
            print("\nSesión cancelada. Saliendo...")
            tiempo(2)
            return
        con = input("/// INGRESE SU CONTRASEÑA ///\n")
        if us in usuarios:
            if usuarios[us]["contraseña"] == con:
                rol = usuarios[us]["rol"]
                if rol=="cliente":
                    print("\nInicio de sesión exitoso\n")
                    tiempo(2)
                    while True:
                        
                        iva = calcular_iva(total_c)
                        subtotal = calcular_subtotal(total_c)
                        
                        mostrar_menu()
                        print("Carrito:", "       ", "Total:", total_c, "SubTotal:", subtotal, "Iva:", iva)
                        print("=================================")
                        print(carrito)
                        op = input("Escriba el nombre de la sección a ingresar: ").strip().lower()
                        if op == "cinturones":
                            catalogo(cin)
                            total_c, carrito, cantidad_t, carrito_det = agregar_producto(cin, carrito, total_c, carrito_det, cantidad_t)
                        elif op == "mochilas":
                            catalogo(moc)
                            total_c, carrito, cantidad_t, carrito_det = agregar_producto(moc, carrito, total_c, carrito_det, cantidad_t)
                        elif op == "monederos":
                            catalogo(mon)
                            total_c, carrito, cantidad_t, carrito_det = agregar_producto(mon, carrito, total_c, carrito_det, cantidad_t)
                        elif op == "bananos":
                            catalogo(ban)
                            total_c, carrito, cantidad_t, carrito_det = agregar_producto(ban, carrito, total_c, carrito_det, cantidad_t)
                        elif op == "contacto":
                            print("Número de contacto:", contacto)
                            tiempo(3)
                        elif op == "quitar producto" or op == "quitarproducto":
                            quitar_producto(carrito, cantidad_t, carrito_det)
                        elif op == "pagar":
                            while True:
                                if total_c>0:    
                                    Nombrecliente, Rutcliente= pago(total_c)
                                    GenComp(total_c)
                                    boleta=GenBoleta(contacto,cantidad_t,carrito,carrito_det,subtotal,iva,total_c)
                                    registro_transacciones.append(boleta)
                                    factura=GenFactura(contacto,Nombrecliente,Rutcliente,cantidad_t,carrito,carrito_det,subtotal,iva,total_c)
                                    registro_transacciones.append(factura)
                                    print("Desea salir?")
                                    salir=input("Escriba si o no: ")
                                    if salir=="si":
                                        sys.exit()
                                    else:
                                        carrito.clear()
                                        total_c=0 
                                        subtotal=0 
                                        iva=0
                                        break
                                else:
                                    print("\nUsted no tiene productos añadidos, añada un producto para pagar")
                                    tiempo(3)
                                    break
                        elif op == "cerrarsesion" or op=="cerrar sesion":
                            print("Desea cerrar sesion?")
                            salir=input("Escriba si o no: ")
                            if salir=="si":
                                print("\nCerrando sesion... ")
                                tiempo(2)
                                break
                        elif op == "salir":
                            print("Desea salir?")
                            salir=input("Escriba si o no: ")
                            if salir=="si":
                                sys.exit()
                        else:
                            error(2)
                elif rol=="admin":
                    print("\nInicio de sesión exitoso como administrador\n")
                    tiempo(2)
                    while True:
                        salir=m_admin(cin,moc,mon,ban,registro_transacciones)
                        if salir=="si":
                            break
            else:
                print("Contraseña incorrecta")
        else:
            print("Usuario no existente")

while True:
    print("                  I-L Cueros")
    print("                                             ")
    print(" -> Desea iniciar sesion o ingresar como invitado\n")
    print("---- Escriba el nombre de la opcion que desea ----")
    print("  ______________________________________________")
    op=input(" | Invitado  |   Iniciar sesion  |  Registrarse |\n").strip().lower()
    if op == "invitado":
        while True:
            
            iva = total_c * 0.19
            subtotal = total_c - iva
            
            menu_inv()
            print("Carrito:", "       ", "Total:", total_c, "SubTotal:", subtotal, "Iva:", iva)
            print("=================================")
            print(carrito)
            op = input("Escriba el nombre de la sección a ingresar: ").strip().lower()
            if op == "cinturones":
                catalogo(cin)
                total_c, carrito, cantidad_t, carrito_det = agregar_producto(cin, carrito, total_c, carrito_det, cantidad_t)
            elif op == "mochilas":
                catalogo(moc)
                total_c, carrito, cantidad_t, carrito_det = agregar_producto(moc, carrito, total_c, carrito_det, cantidad_t)
            elif op == "monederos":
                catalogo(mon)
                total_c, carrito, cantidad_t, carrito_det = agregar_producto(mon, carrito, total_c, carrito_det, cantidad_t)
            elif op == "bananos":
                catalogo(ban)
                total_c, carrito, cantidad_t, carrito_det = agregar_producto(ban, carrito, total_c, carrito_det, cantidad_t)
            elif op == "contacto":
                print("Número de contacto:", contacto)
                tiempo(3)
            elif op == "quitar producto" or op == "quitarproducto":
                quitar_producto(carrito, cantidad_t, carrito_det)
            elif op == "pagar":
                
                while True:
                    if total_c>0:
                        Nombrecliente, Rutcliente= pago(total_c)
                        GenComp(total_c)
                        boleta=GenBoleta(contacto,cantidad_t,carrito,carrito_det,subtotal,iva,total_c)
                        registro_transacciones.append(boleta)
                        factura=GenFactura(contacto,Nombrecliente,Rutcliente,cantidad_t,carrito,carrito_det,subtotal,iva,total_c)
                        registro_transacciones.append(factura)
                        print("Desea salir?")
                        salir=input("Escriba si o no: ")
                        if salir=="si":
                            sys.exit()
                        elif salir=="no":
                            carrito.clear()
                            total_c=0 
                            subtotal=0 
                            iva=0
                            break
                    else:
                        print("Usted no tiene productos añadidos, añada un producto para pagar")
                        tiempo(3)
                        break
            elif op== "iniciarsesion" or op== "iniciar sesion":
                while True:
                    inicio_sesion()
            elif op == "salir":
                print("Desea salir?")
                salir=input("Escriba si o no: ")
                if salir=="si":
                    sys.exit()
            else:
                error(2)
            

    elif op== "iniciarsesion" or op== "iniciar sesion":
        while True:
            inicio_sesion()
            
    elif op== "registrarse":
                print()
                us=input("\n/// INGRESE SU USUARIO ///\n")
                con=input("\n/// INGRESE SU CONTRASEÑA ///\n")
                n_rol="cliente"
                if us in usuarios:
                    print("El usuario ya existe en el sistema, elija otro nombre usuario porfavor")
                    tiempo(2)
                else:
                    usuarios[us] = {"contraseña": con, "rol":n_rol}
                    print("\nUsuario Registrado exitosamente\n")
                    tiempo(2)
    else:
        error(2)