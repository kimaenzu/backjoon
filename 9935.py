sen = str(input())
boom = str(input())
count = 2
len_b = len(boom)
i = 0
pre_sen = 'a'
while (count !=0) :
    if (sen[i:len_b+i] == boom) ==True:
        pre_sen = sen
        sen = sen[:i]+sen[len_b+i:]
    else:
        i += 1
    if (len(sen)-len(boom)+1 == i):
        i = 0
        count -= 1
    if sen[i:len_b+i] == '':
        count = 0
if sen == '':
    print("FRULA")
else:
    print(sen)