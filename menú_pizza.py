"""
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función 
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 

Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y 
todos los ingredientes que lleva.

"""
#Realicé la primera opción, con pizza vegetariana. Falta la no vegetariana
try:
    print("="*30)
    print("     Pizzería Bella Napoli       ")
    print("="*30)

    tipoPizza = int(input("Elija su tipo de Pizza\n [1]: Vegetariana \n [2]: No vegetariana \n> "))
    if tipoPizza == 1:
        tipoPizza = "Vegetariana"
        print("-------------       Menú Vegetariano         -------------")
        print("'Una pizza con una base de salsa de tomate y queso mozzarella'")
        print("Ingredientes vegetarianos: Pimiento y tofu")
        ingrediente = input("Elige un ingrediente de la lista [P/T]: ").lower()
        if ingrediente == "p":
            ingrediente = "Pimiento"
        else:
            if ingrediente == "t":
                ingrediente = "Tofu"
    elif tipoPizza == 2:
        tipoPizza = "No Vegetariana"
        print("-------------       Menú no Vegetariano         -------------")
        print("'Una pizza con una base de salsa de tomate y queso mozzarella'")
        print("Ingredientes vegetariana: Pepperoni y carne")
        ingrediente = input("Elige un ingrediente de la lista [P/J/S]: ").lower()
        if ingrediente == "p":
            ingrediente = "Pepperoni"
        elif ingrediente == "j":
             ingrediente = "Jamon"
        elif ingrediente == "s":
            ingrediente = "Salmon"
        else:
            print("Ingrediente no correcto")

except ValueError:
    print("Error de valor ingresado")