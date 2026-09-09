import logging

# Configurar logging
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('error.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def dividir(a, b):
    """
    Función para dividir dos números.
    
    Args:
        a: Dividendo
        b: Divisor
        
    Returns:
        float: Resultado de la división
        
    Raises:
        ZeroDivisionError: Si el divisor es cero
    """
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError as e:
        # Registrar el error con nivel ERROR
        logger.error(f"Error de división por cero: No se puede dividir {a} entre {b}", exc_info=True)
        raise

def main():
    """Función principal para demostrar el logging de errores."""
    print("=== Aplicación de División con Logging ===\n")
    
    # Caso 1: División válida
    try:
        resultado = dividir(10, 2)
        print(f"✓ 10 ÷ 2 = {resultado}\n")
    except ZeroDivisionError:
        print("✗ No se pudo realizar la división\n")
    
    # Caso 2: División por cero (provoca error intencionalmente)
    try:
        print("Intentando dividir 15 ÷ 0...")
        resultado = dividir(15, 0)
        print(f"✓ 15 ÷ 0 = {resultado}\n")
    except ZeroDivisionError:
        print("✗ Se capturó la excepción de división por cero\n")
    
    # Caso 3: Otra división válida
    try:
        resultado = dividir(20, 4)
        print(f"✓ 20 ÷ 4 = {resultado}\n")
    except ZeroDivisionError:
        print("✗ No se pudo realizar la división\n")

if __name__ == "__main__":
    main()
