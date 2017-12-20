import datetime

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d-%H-%M-%S-%f")

file1 = open('file1.txt','r')
file2 = open('file2.txt','r')
file3 = open('file3.txt','r')
file4 = open(filename+'.txt','w')

file1_contents = file1.readlines()
file2_contents = file2.readlines()
file3_contents = file3.readlines()

file4.write(file1_contents[0]+'\n')
file4.write(file2_contents[0]+'\n')
file4.write(file3_contents[0]+'\n')

file1.close()
file2.close()
file3.close()
file4.close()