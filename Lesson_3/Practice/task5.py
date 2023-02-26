# Написать программа, которая из заданного списка элементов создает список из уникальных элементов.
user_list = [1, 2, 3, 5, 1, 5, 3, 10]

result_list = []

for i in user_list:
    count = 0
    for k in user_list:
        if i == k: 
            count += 1
    if count == 1:
        result_list.append(i)
print(result_list)


result_list2 = []
for i in user_list:
    if user_list.count(i) == 1:
        result_list2.append(i)
print(result_list2)

result_list3 = [i for i in user_list if user_list.count(i) == 1]
print(result_list3)


print(list(filter(lambda x: user_list.count(x) == 1 , user_list)))