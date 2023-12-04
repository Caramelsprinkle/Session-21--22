from ShoppingListJH import ShoppingListJH

def orderFoodJH() -> list[ShoppingListJH]:
    allOrderedFood = []
    
    while True:
        numberOfItems = int(input("How many items will you order today? "))
        if numberOfItems >= 1:
            break
        print("Number of items must be at least 1.")
    
    for foodIndex in range(numberOfItems):
        print(f'Item #{foodIndex + 1}-')
        food = input("Enter food: ")
        
        while True:
            amount = float(input("Enter amount of pounds: "))
            if amount >= 1:
                break
            print("Amount of pounds must be greater than 0.")
        print("")
        allOrderedFood.append(ShoppingListJH(food.lower(), amount))
        
    return allOrderedFood

def displayContentsJH(listOfFoodOrder:list[ShoppingListJH]) -> None:
    for foodOrder in listOfFoodOrder:
        print(foodOrder)
        print("")
    return

def calculateTotalCostJH(listOfFoodOrder:list[ShoppingListJH]) -> float:
    cumulativeCost = 0
    for foodOrder in listOfFoodOrder:
        cumulativeCost += foodOrder.calculateCostJH()
    return cumulativeCost

def main():
    listOfOrderedFood = orderFoodJH()
    print("Here's a summary of the items purchased:\n----------------")
    displayContentsJH(listOfOrderedFood)
    totalCost = calculateTotalCostJH(listOfOrderedFood)
    print(f'Total Cost: ${totalCost}')
    
main()