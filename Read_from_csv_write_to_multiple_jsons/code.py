fi = open('input.csv','r')
lines=fi.readlines()

x=lines[0].split(",")

for i in range(1,len(lines)):
    y=lines[i].split(",")
    data={x[0]:y[0],x[1]:y[1],x[2]:y[2],x[3].replace("\n",""):y[3].replace("\n","")}
    fo = open(str(i)+'.json','w+')
    fo.write(str(data))
    fo.close()
fi.close()
