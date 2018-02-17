cart=[]

print("want to add to cart")
n=int(input('Amount of product  to add'))
for add in range(n) :
    add=str(input("Add to cart"))
    cart.append(add)
print(cart)

n=cart.pop()
print(cart)

