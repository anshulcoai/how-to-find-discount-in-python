#Write a programm to read price and quantity of the price & quantity of the product. Find total price and the net price After 5% discount.

p=int(input('Enter the price of the product :'))
q=int(input('Enter the quantity of the product :'))

tp=p*q
d=(6*tp)/100
np=tp-d

print('Total Price :',tp)
print('discount :',d)
print('Net price :',np)
