# SISTEMA DE INVENTARIO - JOSEPH ROMERO
# Importamos las funciones de validación desde el archivo externo, funcion creada bajo el criterio de recursividad
from Fun_validations import validate_text, validate_number

# -------------------------------------------
# Ciclo principal
# -------------------------------------------
continuar = True

while continuar:
    print("\n--- Registro de Producto ---")
    
    # Usamos validate_text para el nombre (asegura que no esté vacío ni tenga números)
    nombre = validate_text("Ingrese el nombre del producto: ")
    
    # Usamos validate_number especificando el tipo de dato (float para precio, int para cantidad)
    precio = validate_number("Ingrese el precio del producto: ", float)
    cantidad = validate_number("Ingrese la cantidad del producto: ", int)

    # Calcular el costo total
    costo_total = precio * cantidad

    # Mostrar resultados en consola
    print(f"\n Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} | Total: ${costo_total:.2f}")

    # Preguntar si desea registrar otro producto
    respuesta = input("\n¿Desea registrar otro producto? (s/n): ").lower().strip()
    if respuesta != "s":
        continuar = False

print("\nPrograma finalizado. ¡Gracias por usar el sistema!")