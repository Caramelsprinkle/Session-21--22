class ShoppingListJH:
    def __init__(self, food:str, amount:int) -> None:
        self.__food:str = food
        self.__amount:int = amount
        self.__priceMatch = {
            "dry cured iberian ham" : 177.80,
            "wagyu steaks" : 450.00,
            "matsutake mushrooms" : 272.00,
            "kopi luwak coffee" : 306.50,
            "moose cheese" : 487.20,
            "white truffles" : 3600.00,
            "blue fin tuna" : 3603.00,
            "le bonnotte potatoes" : 270.81
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