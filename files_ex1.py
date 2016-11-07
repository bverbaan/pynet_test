a = open("my3lines.txt")
for line in a:
    print line
a.close()


b = open("newlines.txt\n", "w")
b.write('test')
b.close()

with open('newlines.txt','a') as c:
    c.write('test2\n')
c.close()
