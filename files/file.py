lines = ['안녕하지 못하는 \n', 'python \n', 'coding']

# with open('./hello.txt', 'w')as file:
#     file.writelines(lines)

with open('./hello.txt', 'r') as file:
    lines=file.readlines()
    print(lines)

with open('hello.txt', 'r')as file:
    line=None
    while line !='':
        line=file.readline()
        print(line.strip('\n'))