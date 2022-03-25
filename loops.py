for i in range(1,10):
    print(i)

for i in range(0,12,3):
    print(i)



string = "String traversal!"
for i in range(len(string)):
    print(string[i])


string = "String traversal!"
for char in string:
    print(char)

for i in range(3):
    for j in range(2):
        print(j)



#10 x 10 multiplication table


for i in range(1,11):
    print('{:<3}|'.format(i),end="")

for j in range(1,11):
    print('{:>4}'.format(i * j),end="")
if i == 1:
    print('\n{:#^44}'.format(""), end="")




condition = 10

while condition != 0:
    print(condition)
    condition = condition - 1
    















    