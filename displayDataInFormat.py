item = input("Enter the item: ")
price = input("Enter the item's price: ")

itemLength = len(item)
priceLength = len(price)

numberOfDots = '.' * (25-(itemLength+priceLength))

print(item+numberOfDots+price)
