no = 2
even_list = []
for num in range(4, 31):
    even = num % no
    if even == 0:
        even_list.append(num)
print(even_list)