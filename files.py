file = open('example.txt','r')

#Read content of file as a String
contents = file.read()
print(contents)
print(type(contents))

#Read content of file as a List
contents = file.readlines()
#Will be empty as the previous file.read operator has iterated to the EOF
print(contents)
print(type(contents))

#Reset the pointer file to the beginning of the file
file.seek(0)
#Read content of file as a List
contents = file.readlines()
print(contents)
print(type(contents))

#Remove \n from each line
contents = [i.rstrip("\n") for i in contents]
print(contents)
#Remove the file pointer
file.close()

file = open('fruits.txt','r')
contents = file.read()
print(contents)
file.close()

file = open('fruits.txt','r')
contents = file.readlines()
contents=[i.rstrip('\n') for i in contents]
for i in contents:
    print(len(i))
file.close()

#Write/Create new file
numbers = [1,2,3]
file = open('test.txt','w')
for num in numbers:
    file.write(str(num)+'\n')
file.close()

file=open('test.txt','r')
contents=file.read()
print(contents)
file.close()

#Add/Append lines to the file
file = open('test.txt','a')
file.write('Helloo\n')
file.close()

temperatures = [10,-20,-289,100]
def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Please enter a valid temperature which a physical matter can reach :p"
    else:
        fahrenheit = (celsius * 9/5.0)+32
        return fahrenheit

file = open('test.txt','a')
for temperature in temperatures:
    celsius = celsius_to_fahrenheit(temperature)
    if(type(celsius)!=str):
        file.write(str(celsius)+'\n')
file.close()