

file=open("my file.txt","r")
test=file.read()
print(test)
file.seek(0)#this is allow u to print 2 times
my =file.readlines()
print(my)