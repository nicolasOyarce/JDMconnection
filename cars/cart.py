class ShoppingCart:

    def __init__(self, request):

        self.request = request
        self.session = request.session

        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart


    

    def add(self, product):
        product_id = str(product.id)

        if product_id not in self.cart.keys():
            self.cart[product_id] = {
                "car_id": product.id,
                "brand": product.brand,
                "model": product.model,
                "stock": product.stock,
                "quantity": 1,
                "age": product.age,
                "price": str(product.price),
                "image": product.image.url,
            }
        else:
            for key, value in self.cart.items():
                if key == product_id:
                    if value["quantity"] + 1 > product.stock:
                        return  

                    value["quantity"] = value["quantity"] + 1
                    value["price"] = int(value["price"]) + product.price
                    break

        self.save()


        
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True


    def remove(self, product):
        product.id = str(product.id)
        if product.id in self.cart:
            del self.cart[product.id]
            self.save()


    def decrement(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            value = self.cart[product_id]
            value["quantity"] = value["quantity"] - 1
            value["price"] = int(value["price"]) - product.price
            if value["quantity"] < 1:
                self.remove(product)
            self.save()
        else:
            print("El producto no existe en el carrito")


    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True