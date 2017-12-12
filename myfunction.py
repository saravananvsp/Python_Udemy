def min_to_hours(minutes):
    hours = minutes / 60
    return hours

def sec_to_hours(seconds):
    hours = seconds / 3600
    return hours

minutes = int(input("Enter Minutes: "))
print(str(minutes)+" minutes = "+str(min_to_hours(minutes))+" hours")

seconds = int(input("Enter Seconds: "))
print(str(seconds)+" seconds = "+str(sec_to_hours(seconds))+" hours")

def string_length(string):
    if type(string) == int:
        return "Sorry, integers don't have length"
    elif type(string) == float:
        return "Sorry, float don't have length"
    else:
        return len(string)

string = input("Enter a string: ")
print(string_length(string))
string=44
print(string_length(string))
string=44.00
print(string_length(string))

def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Please enter a valid temperature which a physical matter can reach :p"
    else:
        fahrenheit = (celsius * 9/5.0)+32
        return fahrenheit

celsius = float(input("Enter Temperature in Celsius : "))
print("Temperature in Fahrenheit : "+str(celsius_to_fahrenheit(celsius)))

temperatures = [10,-20,-289,100]

for temperature in temperatures :
    print(celsius_to_fahrenheit(temperature))