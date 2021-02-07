name = input("Please enter your name: ")
print("Hello", name + ", Welcome to your personal unit converter")
print("Please choose which conversion you would like to perform: ")
print("1 - convert cm to inches")
print("2 - convert percent to letter grade")
print("3 - convert kg to pounds")
print("4 - convert km to miles")
print("5 - convert fahrenheit to celsius")
choice = input('')

if choice =='1':
    x = float(input("value in cm to convert to inches : "))
    inches=x/2.54
    print(x, "cm =" ,inches, "inches")

elif choice =="2":
    x=int(input("percent to convert to letter grade\n"))
    if  80<= x <=100:
        print(x, "% = A")
    elif 70<= x <=79:
        print (x,"% = B")
    elif 60<= x <=69:
        print(x, "% = C")
    elif 50<= x <=59:
        print(x, "% = D")
    elif 20<= x <=49:
        print(x, "% = E")
    elif 0<= x <=19:
        print(x, "% = F")
    else:
        print("input not valid") 

elif choice =="3":
    x=int(input("enter capacity in kg : "))
    lb=x*2.20462
    print(x, "kg =" ,lb, "pounds")

elif choice =="4":
    x=int(input("value in in km : "))
    miles=x/1.621371
    print((x, "km =" ,miles, "miles"))

elif choice =="5":
    x=float(input("temperature in fahrenheit to convert tto celsius : "))
    fahrenheit=(x-32)*5/9
    print(x,"celsius = ",fahrenheit,"degrees fahrenheit")           
else:
        print("select again")

print("Goodbye",name) 
