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
