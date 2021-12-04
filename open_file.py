

with open('hello1.txt','w') as file:
    for i in range(3):
        file.write('Hello,world.lll! {0} ....\n'.format(i))