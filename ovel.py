l=["Hello","hii","who","are","you"]
for i in l:
    k=list(map(lambda x:x if x not in "aeiouAEIOU" else"",i))   print(k)



from functools import reduce

numbers = [5, 10, 15, 20, 25, 30]

result = reduce(
    lambda x, y: x + y,
    filter(
        lambda x: x % 5 == 0,
        map(lambda x: x ** 2, numbers)
    )
)

print("Sum:", result)





all_orders = []
total_orders = 0

def order(*items, **details):
    global all_orders, total_orders

    order_data = {
        "items": items,
        **details
    }

    all_orders.append(order_data)
    total_orders += 1

# Call the function twice
order("Pizza", "Burger", customer="Abhi", payment="Online")
order("Coffee", "Sandwich", customer="Rahul", payment="Cash")

print("All Orders:")
print(all_orders)

print("Total Orders:", total_orders)




d = {"apple": 100, "banana": 40, "cherry": 150}

result = list(filter(lambda key: d[key] > 50, d))

print(result)
