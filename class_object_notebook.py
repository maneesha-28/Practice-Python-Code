class notebook:
    def __init__ (self,dimension,price,pages,size):
        self.dimension=dimension
        self.price=price
        self.pages=pages
        self.size=size
b1=notebook("21*28 cm", "Rs. 60", 320,"A4")
print(b1.dimension)
print(b1.price)
print(b1.pages)
print(b1.size)
