#height of boxes
largebox=float(input("enter height of large box in inches eg 7.5 : \n"))
print("you have entered",largebox,"inches as height for the large box")

smallbox=float(input("enter height of small box in inches eg 7.5 : \n"))
print("you have entered",smallbox,"inches as height for the small box")

#requesting user for the height of a single book
heightb=float(input("enter height of a book in inches : \n"))
print("you have entered",heightb,"inches per book")

#request user for number of books
books=int(input("enter number books : \n"))
print("you have entered",books,"books")

totalh=books*heightb
print ("the total height is ",totalh,"inches")

#small box check
if totalh <= smallbox:
    print("ship 1 small box")


#large box check
elif smallbox < totalh <= largebox:
    print("ship 1 large box")

#where a large and a small box are needed
elif totalh > largebox:
    #calculate large boxes needed
    x=totalh/largebox
    i= int(x)
    s = totalh%largebox
    if s == 0:
        print("Shipping" ,i, "boxes")
        print(i, "large")
    else:
        
        if s > smallbox:
            print("Shipping" ,i+1, "boxes")
            print(i+1, "large" )
        else:
            print("Shipping" ,i+1, "boxes")
            print(i, "large," ,1, "small")


else:
    print("seek help")
