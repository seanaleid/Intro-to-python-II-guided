class Product:
    def __init__(self, name, price, description, brand_name, sku, on_sale=False)
        self.name = name
        self.price = price
        self.description=description
        self.brand_name = brand_name
        self.sku = sku
        self.on_sale = on_sale
        ### if we don't add line 8, it wouldn't exist when we run the class with new info
    
    def __str__(self):
        return self.name + "\t$" + str(self.price)

class Clothing(Product):
    def __init__(self, name, price, description, brand_name, sku, color, size)
        super().__init__(name, price, description, brand_name, sku, on_sale, on_sale=True)
        self.color = color
        self.size = size

    def __str__(self):
        ### a way to call a method from the Product class
        return super().__str__() + " comes in " + self.color + ", " + self.size