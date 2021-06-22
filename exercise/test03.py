#146p

#1

a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:
    print("shirt")
elif "nee" in a:
    print("need")
else:
    print("none")

#2
result =0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
        
print(result)

#3
i = 0
while True:
    i += 1
    if i > 5:
        break
    print("*" * i)

#이중 for문

for i in range(1,6):
    for j in range(1,i+1):
        print("*", end="")
    print()    

#4
for i in range(100):
    i += 1
    print(i, end = " ")


#5
print("\n")
print("================5번============")    
A = [70,60,55,75,95,90,80,80,85,100]
total = 0
for score in A:
    total += score
average = total/10
print(average)
'''
#6번
numbers = [1,2,3,4,5]
result = []
for n in number:
    if n % 2 == 1:
        result.append(n*2)
 
'''
