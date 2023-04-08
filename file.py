# file1 = open('notes.txt', 'r')
# print(file1.read())
# print(file1.readlines())
# file1.close()

with open('notes.txt', 'a') as file1:
    file1.write('Hellow')
    print(file1.readlines())    
     
with open('notes.txt', 'r') as file2:
    print(file2.readlines())