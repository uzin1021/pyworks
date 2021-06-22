#정사각형의 넓이

"""size = 5""" #기본
size = int(input("한 변의 길이 : ")) #input 입력 받았을때

area = size * size

print("정사각형의 넓이 : ", area, "cm")
print("정사각형의 넓이 : %dcm" % area) #글자 붙여서 출력할 때 

#삼각형의 넓이

width = 5
height = 7

area = (width * height)/2

print("삼각형의 넓이 : ", area, "cm")
print("삼각형의 넓이 : %dcm" % area)

