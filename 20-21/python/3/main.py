class Product():
    def __init__(self, Name: str, ProductID: int, Price: float):
        self.ProductID = ProductID
        self.Price = Price
        self.Name = Name
    
    def __str__(self):
        return f"ID: {self.ProductID}\tName: \'{self.Name}\'\t€{self.Price}"

bike = Product("Cool Red Bike", 1, 40.99)

print(bike)