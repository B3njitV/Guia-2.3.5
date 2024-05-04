# Precios de las pizzas
precios_pizzas = {
    "Pepperoni": 8.99,
    "Margarita": 7.99,
    "Hawaiana": 9.99,
    "Vegetariana": 7.99,
    "Queso": 6.99
}

def calcular_costo_pedido(pedido):
    subtotal = sum(precios_pizzas[pizza] for pizza in pedido)
    impuesto = subtotal * 0.1  # Impuesto del 10%
    total = subtotal + impuesto
    return subtotal, impuesto, total

def main():
    print("Bienvenido a Cesar’s Pizza")
    print("Menú de pizzas:")
    for pizza, precio in precios_pizzas.items():
        print(f"- {pizza}: ${precio}")

    pedido = input("\nIngrese las pizzas que desea (separadas por comas): ").split(",")

    # Eliminar espacios en blanco alrededor de cada pizza y convertir a minúsculas
    pedido = [pizza.strip().capitalize() for pizza in pedido]

    subtotal, impuesto, total = calcular_costo_pedido(pedido)

    print("\nDetalle del Pedido:")
    for pizza in pedido:
        print(f"- {pizza}")

    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Impuesto (10%): ${impuesto:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
