#test 113p

#5번
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

#6번
a = [1,3,5,4,2]
a.sort()
print(a)
a.reverse()
print(a)

#7번
a = ['Life','is','too','short']
result = " ".join(a)
#result = a[0]+a[1]+a[2]+a[3] 따로따로 불가능.
print(result)

#split() 예제
s = "Life is too short"
s = s.split() #구분 기호 : 공백 
print(s)

s = "a:b:c:d"
s = s.split(":")
print(s)

#8번
a = (1,2,3)
a = a + (4,)
print(a)

#9번
a = dict()
print(a)
a['name'] = 'python'



#10번
a = {'A':90 ,'B':80, 'C':70}
result = a.pop('B')
print(a)
print(result)

#11번
a = [1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b = list(aSet)
print(b)

#12번



def is_odd(number):
    if is_odd % 2 == 1:
        return True
    else:
        return False

print(is_odd)
