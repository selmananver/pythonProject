
 # files =["Joker.mp4",'Money Heist.mp4','Memories.mp4']
 # for x in range(10,51,5):
 #    print(x)
 #    print(x[0:-4])

num = int(input('Enter the multiplication table'))
limit = int(input('Enter the limit'))
for i in range(1, limit + 1):
    multiply = int(i * num)
    print(str(i) + '*' + str(num) + '=' + str(multiply))
# for i in range(5):
#     if i ==3 :
#         continue
#     print(i)