sen = str(input())
boom = str(input())
count = 1
len_b = len(boom)
while (count !=0) :
    count = 0
    for i in range(len(sen)-len(boom)+1):
        if (sen[i:len_b+i] == boom) ==True:
            sen = sen[:i]+sen[len_b+i:]
            count += 1
if sen == '':
    print("FRULA")
else:
    print(sen)