from Utilidades import tiempo
#agregar producto al catalogo
def agr_prod(nombre, precio, diccionario):
    diccionario[nombre] = precio
    print(f"\nEl producto '{nombre}' ha sido agregado al catálogo.")
    tiempo(2)

#f cambiar precio de producto en catalogo   
def cam_precio(nombre, nuevo_precio, diccionario):
    if nombre in diccionario:
        diccionario[nombre] = nuevo_precio
        print(f"\nEl precio de '{nombre}' ha sido modificado a {nuevo_precio}.")
        tiempo(2)
    else:
        print(f"\nNo se encontró el producto '{nombre}' en el catálogo.\n")
        tiempo(2)       
               
#f eliminar producto del catalogo
def del_prod(nombre, diccionario):
    if nombre in diccionario:
        del diccionario[nombre]
        print(f"\nEl producto '{nombre}' ha sido eliminado del catálogo.\n")
        tiempo(2)
    else:
        print(f"\nNo se encontró el producto '{nombre}' en el catálogo.\n")
        tiempo(2)
#modificar productos de carrito:
  
def agregar_producto(diccionario,carrito, total_c,carrito_det,cantidad_t):
    print("Ingrese el nombre del producto a agregar al carrito")
    op = input("Si desea volver escriba volver: ").strip().lower().capitalize()
    if op in diccionario:
        producto = op.strip().lower().capitalize()
    
        # Agregar producto al carrito
        carrito.append(producto)
    
        # Calcular total a pagar
        total_c += diccionario[producto]
  
        # Agregar producto al diccionario de detalles
        carrito_det[op] = diccionario[op]
        
        # Incrementar la cantidad total
        cantidad_t += 1
    elif op == "Volver":
        print("\nVolviendo al menú principal...\n")
        tiempo(2)
    else:
        print("\nEl producto ",op," no esta en el catalogo\n")
        tiempo(2)
    return total_c,carrito,cantidad_t,carrito_det
#obtiene el precio del producto selecionado

def quitar_producto(carrito, cantidad_t, carrito_det):
    op = input("Ingrese el nombre del producto a eliminar: ").strip().lower().capitalize()
    if op in carrito:
        carrito.remove(op)
        cantidad_t -= 1
        del carrito_det[op]
        print("Producto quitado del carrito.")
        tiempo(2)
    else:
        print("El producto no está en el carrito.")
        tiempo(2)
    return carrito, cantidad_t, carrito_det

def calcular_iva(total_c):
    global iva
    iva = total_c * 0.19
    return iva
    
    
def calcular_subtotal(total_c):
    subtotal = total_c - iva
    return subtotal
    
    
