# 3A
# 4B
# 5C
# #bài 1
# arr = [0,1,2,3,4,5,6,7,8,9]
# add2 = []
# nhan2 = []
# dich2 = []
# for i in range(len(arr)):
#     add2.append(arr[i] + 2)
#     nhan2.append(2*arr[i])
#     dich2.append(arr[(i + 2) % len(arr)])
# print("Original list".ljust(13),":", arr)
# print("Add 2".ljust(13),":", add2)
# print("Multiply by 2".ljust(13),":",nhan2)
# print("Shift 2".ljust(13),":",dich2)



# #bài 2
# arr = ['l', 'o', 'o', 'h', 'c', 'S', ' ', 'y', 'g', 'o', 'l', 'o', 'n', 'h', 'c', 'e', 'T', ' ', 'X', 'd', 'n', 'i', 'M']
# rev = arr[::-1]
# res = ''.join(rev)
# print(res)


# #bài 3
# n = int(input("Input a positive number: "))
# fib = [0]*(n + 1)
# fib[1] = 1
# for i in range(2, n + 1):
#     fib[i] = fib[i - 1] + fib[i - 2]
# print("First",n,"Fibonacci number(s):", *fib[1:])

# #bài 4
# n = int(input("Number of items: "))
# menu = []
# for i in range(n):
#     item = input(f"Item {i+1}: ")
#     price = float(input(f"Price of item {i+1}: "))
#     menu.append((item, price))

# average_price = sum([item[1] for item in menu])/n
# print(f"Average price: {average_price:.2f}")

# above_average_items = [item for item in menu if item[1] > average_price]
# print("Item(s) above average price:", *above_average_items)

# #bài 5
# print('Number of unique words:',len(set(input('Write a sentence: ').split())))

