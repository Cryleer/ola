import copy
from Utilidades import tiempo,error
#Rut empresa
Rut_E = "12.345.678-4"
#Numero Factura y Boleta
NumF = 0
NumB = 0

#Funciones de Pago    
def pago(total):
    
    while True:
        
        try:
            MetPag = int(input("Seleccione el metodo de pago: \n 1- WebPay \n 2- Transferencia Bancaria \n"))
            if MetPag == 1: 
                while True:
                    try:
                        Nombrecliente = input("Ingrese el nombre asociado a la tarjeta:  ")
                        Rutcliente = input("Ingrese el Rut(sin guion) asociado ala tarjeta:  ")
                        NumTar = int(input("Ingrese el numero de su tarjeta:  "))
                        cvv = int(input("Ingrese su CVV: "))
                        print("                            ")
                        print("SU PAGO SE HA REALIZADO CON EXITO") 
                        print("                                    ")
                        tiempo(3)
                        break
                    except ValueError:
                        error(2)
            elif MetPag == 2:
                while True:
                    try:
                        Nombrecliente=input("Ingrese el nombre de la cuenta de origen:  ")
                        Rutcliente = int(input("Ingrese el RUN/T de la cuenta origen:  "))
                        print ("RUN\T de la cuenta destino: ",Rut_E,"\n") 
                        tiempo(2)   
                        print("Su total a pagar es de: ",total,"\n")
                        tiempo(3)
                        print ("SU PAGO SE HA REALIZADO CON EXITO \n") 
                        tiempo(2)
                        break   
                    except ValueError:
                        error(2)     
                        
        except ValueError:
            error(2)
        break
    global Comp
    while True:
        try:
            Comp = int(input("Elija qué quiere recibir:\n1- Boleta\n2- Factura\n"))
            break
        except ValueError:
            error(2)
    return Nombrecliente,Rutcliente
def GenComp(total):
    print("_______________________")
    print("COMPROBANTE ")
    print("                      ")
    print("Industria: I-L")
    print (total)      
def GenBoleta(contacto,cantidad_t,carrito,carrito_det,subtotal,iva,total_c):
    
    if Comp == 1:
        boleta={"Tipo": "Boleta",
        "Número": NumB + 1,
        "Industria": "I-L",
        "Giro": "Peletería",
        "Ciudad": "Rancagua",
        "Email": "ilempresa@live.com",
        "Teléfono": contacto,
        "RUT": "11111111-1",
        "Cantidad": cantidad_t,
        "Detalle": copy.copy(carrito),
        "Valor unitario": carrito_det,
        "Neto": subtotal,
        "Iva": iva,
        "Total": total_c}
        
        print("_________________________")
        print(Rut_E)
        print("BOLETA")
        print("N° ", NumB + 1)
        print("Industria: I-L\n Giro: Peleteria\n Ciudad: Rancagua\nE-mail: ilempresa@live.com\nTelefono:  ", contacto, "contacto" ,"RUT: 11111111-1")
        print("Cantidad: ",cantidad_t,"\n","Detalle: ",carrito,"\n" ,"Valor unitario: ",carrito_det,"\n", )
        print("Neto :",subtotal,"  \n Iva: ",iva,"\n Total: ",total_c)
        print("_________________________")
        return boleta
        
def GenFactura (contacto,Nombrecliente,Rutcliente,cantidad_t,carrito,carrito_det,subtotal,iva,total_c):
    
    if Comp == 2:
        print("_________________________")
        print("                           ")
        print("SE NECESITAN DATOS ADICIONALES PARA GENERAR FACTURA\n")
        DomicilioCliente=input("Ingrese su domicilio: \n")
        Fono=input("Ingrese su fono: \n")
        Ciudad= input("ingrese su ciudad: \n")
        
        factura={"Tipo": "Factura",
        "Número": NumF + 1,
        "Industria": "I-L",
        "Giro": "Peletería",
        "Ciudad": "Rancagua",
        "Email": "ilempresa@live.com",
        "Teléfono": contacto,
        "Señor/a": Nombrecliente,
        "Run/T": Rutcliente,
        "Dirección": DomicilioCliente,
        "Fono": Fono,
        "Ciudad": Ciudad,
        "Cantidad": cantidad_t,
        "Detalle": copy.copy(carrito),
        "Valor unitario": carrito_det,
        "Neto": subtotal,
        "Iva": iva,
        "Total": total_c}
        
        print("__________________________")
        print(Rut_E)
        print("FACTURA \n N° ", NumF + 1)
        print("Industria: I-L\nGiro: Peleteria\nCiudad: Rancagua\nE-mail: ilempresa@live.com\nTelefono:  ",contacto, "contacto" ,)
        print("Señor/a: ",Nombrecliente,"\n","Run/T: ",Rutcliente,"\n","Direccion: ",DomicilioCliente,"\n","Fono: ",Fono,"\n","Ciudad:",Ciudad,"\n","Giro: Peleteria")
        print("Cantidad: ",cantidad_t,"\n","Detalle: ",carrito,"\n" ,"Valor unitario: ",carrito_det,"\n", )
        print("Neto :",subtotal,"  \n Iva: ",iva,"\n Total: ",total_c)
        print("__________________________")
        
        return factura
        

