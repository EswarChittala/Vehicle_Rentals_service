import datetime
import time
def trip():
    print("...WELCOME TO GOA...")
    adhar_no=0
    driving_licence=0
    amount=0
    bike_cost=500
    car_cost=700
    a=datetime.datetime.now()
    b=a.strftime("%H:%M:%S")
    option=int(input("1.Bikes\n2.Cars\nEnter your choice: "))
    if option==1:
        two=int(input("Choose Vechile:\n1.R15\n2.Rx100\n3.Ktm\n4.duke--- "))
        if two==1:
            print("your vechile is R15.")
        elif two==2:
            print("your vechile is RX100.")
        elif two==3:
            print("your vechile is Ktm")
        elif two==4:
            print("your vechile is duke.")
        else:
            print("choise correct option:")
        days=int(input("Number of days Booking:"))
        amount=days*bike_cost
        #print("Your Bill amount is:",amount)
        name=input("Enter your name: ")
        adhar=int(input("Enter your adhar number: "))
        driving_licence=input("Enter your driving_licence number: ")
        if len(str(adhar))==12 and len(str(driving_licence))==7:
            print("==Your Booking details==")
            print("Your name: ",name)
            print("Your 12_digit adhar number:",adhar)
            print("Your 7_digit DL NO:",driving_licence)
            print("your bill amount:",amount)
            con=int(input("Do you want to confirm 0/1: "))
            if con==1:
                print("Please wait your Recipet is in processing:")
                print("======Reciept======")
                time.sleep(1)
                print("----->Booking Successfully<------")
                print("Your name: ",name)
                print("Your adhar number:",adhar)
                print("Your DL NO:",driving_licence)
                print("Number of days Booking:",days)
                print("your bill amount:",amount)
                print("Time:",a.strftime("%H:%M:%S"))
                print("date: ",a.strftime("%Y:%M:%D"))
                print("===Thank for visiting===")
                print("==Visit Again==")
            else:
                print("Booking not confirmed.")
                print("==Thank for Visiting==")
                print("==Visit Again==")
        else:
            print("adhar and Dl not verified.")
    elif option==2:
        four=int(input("Choose Vechile:\n1.Rangrover\n2.Thar\n3.Scorpio\n4.Duster ---"))
        if four==1:
            print("your vechile is Rangerover.")
        elif four==2:
            print("your vechile is Thar.")
        elif four==3:
            print("your vechile is Scorpio")
        elif four==4:
            print("your vechile is Duster.")
        else:
            print("choise correct option:") 

        days=int(input("Number of days Booking:"))
        amount=days*bike_cost
        #print("Your Bill amount is:",amount)
        name=(input("Enter your name: "))
        adhar=int(input("Enter your 12_digit adhar number: "))
        driving_licence=input("Enter your  7_digit driving_licence number: ")
        if len(str(adhar))==12 and len(str(driving_licence))==7:
            print("==Your Booking details==")
            print("Your name: ",name)
            print("Your adhar number:",adhar)
            print("Your DL NO:",driving_licence)
            print("your bill amount:",amount)
            con=int(input("Do you want to confirm 0/1: "))
            if con==1:
                print("======Reciept======")
                time.sleep(1)
                print("------>Booking Successfully<------")
                print("Your name: ",name)
                print("Your adhar number:",adhar)
                print("Your DL NO:",driving_licence)
                print("Number of days Booking:",days)
                print("your bill amount:",amount)
                print("Time:",a.strftime("%H:%M:%S"))
                print("date: ",a.strftime("%Y:%M:%D"))
                print("===Thank for visiting===")
                print("==Visit Again==")
            else:
                print("Booking not confirmed.")
                print("==Thank for Visiting==")
                print("==Visit Again==")
        else:
            print("adhar and Dl not verified.")       
    else:
        print("Enter correct option.")
        
trip()
es=int(input("do you want to continue 0/1:"))
if es==1:
    while es==1:
        trip()
        es=int(input("do you want to continue 0/1:"))   
else:
    print("Thank For Visting")
    print("==Visit Again==")
