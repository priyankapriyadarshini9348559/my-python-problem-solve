#write in the file
f=open("example.txt","w")
f.write("Hello priyanka!")
f.close()
# read from the file
f =open("example.txt","r")
content=f.read()
print(content)
f.close()
f=open("example.txt","w")
f.write("heelo baby")
f.close()
#append a line in file
f=open("example.txt","a")
f.write("\n i love you")
f.close()
#read lines from file
with open("example.txt","r") as f:
    for line in f:
        print(line.strip())
#tell method
f=open("example.txt","r")
print("current pointer:",f.tell())
f.read(5)
print("after reading 5 charchter:",f.tell())
f.close()
# seek method
f=open("example.txt","r")
print(f.read( 5))
f.seek(0)
print(f.seek(1))
f.close()
#practice problem-1
with open("student.txt","w") as f:
    f.write("Babul\n")
    f.write("Baiya\n")
    f.write("Banty\n")
    f.write("Biki\n")
    f.write("Mamuni\n")

with open("student.txt","a") as f:
    f.write("guddu\n")
    f.write("dudu")
with open("student.txt","r") as f:
    print("read the name start with b:")
    for line in f:
        name=line.strip()
        if name.startswith("B"):

            print(name)
