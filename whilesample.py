# i=1
# while i<=10:
#     print(i)
#     i=i+1
# else:
#     print('loop finished')

rows = int(input('Enter no of rows'))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print('*', end='')
        j = j + 1
    print()
    i = i + 1
