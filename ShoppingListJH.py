class ShoppingListJH:
    def __init__(self, food:str, amount:int) -> None:
        self.__food:str = food
        self.__amount:int = amount
        self.__priceMatch = {
            "Dry Cured Iberian Ham" : 177.80,
            "Wagyu Steaks" : 450.00,
            "Matsutake Mushrooms" : 272.00,
            "Kopi Luwak Coffee" : 306.50,
            "Moose Cheese" : 487.20,
            "White Truffles" : 3600.00,
            "Blue Fin Tuna" : 3603.00,
            "Le Bonnotte Potatoes" : 270.81
        }
        self.__itemPriceMatchingJH()
        self.__totalPrice = self.calculateCostJH()
        
    def __itemPriceMatchingJH(self) -> None:
        
        self.__standardPrice = self.__priceMatch.get(self.__food, 0.00)
        return
    
    def calculateCostJH(self) -> float:
        return self.__standardPrice * self.__amount
    
    def __str__(self) -> str:
        return f'Item: {self.__food} \nAmount ordered: {self.__amount} pounds\nPrice per pound: ${self.__standardPrice}\nPrice of order: ${self.__totalPrice}'