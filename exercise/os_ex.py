import os
'''
os.chdir("c:/")
dir = os.popen('dir')
print(dir)

print(dir.read())

'''

# 디렉터리 이름 - 리스트 반환
dirnames = os.listdir('c:/')
print(dirnames)
dirnames2 = os.listdir('c:/pyworks/exercise')
print(dirnames2)
print(dirnames2[0])

for dirname in dirnames2:
    print(dirname)