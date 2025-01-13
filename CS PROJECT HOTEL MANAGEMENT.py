# PROJECT ON HOTEL MANAGEMENT WITH PYTHON.
ch = 0
#Some variables
mnumber=''
cid=''
print("####                          H E L L O                           ####")
print("###   W E L C O M E  T O  T H E  H O T E L  K I N G  P A L A C E   ###")
print()
print("This is the program by which you can choose your ROOM and Package")
print("for staying in our hotel")
print()
print("To choose staying plan, you have to fill details stepwise")
print()
while True:
    print(" 1-> Enter Customer Details")
    print(" 2-> Booking Record")
    print(" 3-> Room Rent")
    print(" 4-> To choose Food pakage")
    print(" 5-> To use Hotel club for entertainment")
    print(" 6-> Display Customer Details")
    print(" 7-> Total Bill")
    print(" 8-> EXIT")
    print()
    print()
    ch= int(input("Enter the number{between 1-10} to confirm details -> "))
    print()

    #To enter details.
    if ch == 1:
        mnumber = input("Enter your mobile number-> ")
        cid = 'KP'+ mnumber
        print("Your customer id is-> ",cid)
        name = input("Enter your name-> ")
        address = input("Enter your Address-> ")
        city= input("Enter the city you in which you live-> ")
        age = int(input("Enter your age-> "))
        email = input("Enter your email id-> ")
        Cdetail= [cid, name, age, city, address, email]
        print(Cdetail)
        print()
        print("New customer ", name, " Entered successfully!")
        print("Now you can go for Booking record(2)")
        print()
        print()

    #Booking Record
    if ch==2:
        checkindate = input("Enter the date you want to check-in the hotel{dd/mm/yyyy}-> ")
        checkoutdate = input("Enter the date you want to check-out-> ")
        ndays = int(input("Enter Number of days you want to live in hotel-> "))
        Cdetail=[cid,name,age,city,address,email,ndays]
        print()
        print("Now you can go for room rent(3)")
        print()
        print()

    #Room Rent
    if ch==3:
        choice=0
        print("#...We have following type of rooms for you...#")
        print()
        print(" 1. LUXURIOUS PRO --> 10000 Rs perday {Top floor, Free-> food,games and pool for 4 persons}")
        print(" 2. LUXURIOUS ------> 6000 Rs perday {Free games and pool for 2 persons}")
        print(" 3. Couple ---------> 3000 Rs perday{for 2 persons}")
        print(" 4. Normal ---------> 2000 Rs perday per person")
        print()
        choice = int(input("Enter the number to select the type of room: "))
        while True:
            roomrent=0
            roomtype=''
            if choice == 1:
                roomtype='LUXURIOUS PRO'
                print(" You have selected LUXURIOUS PRO room type, your Room Rent will be")
                roomrent= ndays*10000
                print('###', roomrent, "Rs"'###')
            elif choice == 2:
                roomtype='LUXURIOUS'
                print(" You have selected LUXURIOUS room type, your Room Rent will be")
                roomrent= ndays*6000
                print('###', roomrent, "Rs"'###')
            elif choice == 3:
                roomtype='Couple'
                print(" You have selected Couple room type, your Room Rent will be")
                roomrent= ndays*3000
                print('###', roomrent, "Rs"'###')
            elif choice == 4:
                roomtype='Normal'
                print(" You have selected Normal room type, your Room Rent will be")
                roomrent= ndays*2000
                print('###', roomrent, "Rs"'###')
            else:
                print("Your entry is out of range please select number between 1 to 4")
            break
        Cdetail= [cid, name, age, city, address, email,ndays,roomrent,roomtype]
        print()
        print("Now you can go for Food(4)")
        print()
        print()
        
    #Food.
    if ch==4:
        a=0
        print("#...The following are the Food types for whole day...#")
        print()
        print(" 1. Pure Vegitarian -----------------> 600 Rs")
        print(" 2. Pure non-vegitarian -------------> 1000 Rs")
        print(" 3. Normal{veg+(non-veg)} -------------> 800 Rs")
        print(" 4. To skip")
        print()
        while True:
            a = int(input("Enter the number to choose type of food-> "))
            frent=0
            foodtype=''
            if a == 1:
                print("You have selected for Pure Vegitarian food")
                frent = ndays*600
                print("Your Food rent is-")
                print('###', frent, "Rs"'###')
                foodtype='Pure vegitarian'
            if a== 2:
                print("You have selected for Pure non-vegitarian food")
                frent = ndays*1000
                print("Your Food rent is-")
                print('###', frent, "Rs"'###')
                foodtype='Pure non-vegitarian'
            if a==3:
                print("You have selected for Normal food")
                frent = ndays*800
                print("Your Food rent is-")
                print('###', frent, "Rs"'###')
                foodtype='Normal'
            if a==4:
                frent = ndays*0
                print("Your Food rent is-")
                print('###', frent, "Rs"'###')
                foodtype='NONE'
            else:
                print()
            break
        Cdetail= [cid, name, age, city, address, email, ndays, roomrent, roomtype, frent,foodtype]
        print("Now you can go for Hotel Club(5)")
        print()
        print()

    #Hotel Club
    if ch==5:
        print("If are coming to enjoy with your family in hotel so can select vaious things...")
        print("Hotel's gaming room includes 3D games and online computer games")
        print("Hotel has a small waterpark")
        print("Room with vaious indoor games like chess, table tennies, etc")
        print()
        print(" 1. Gaming Room ---------------> 3000 Rs/day{2 times entry}")
        print(" 2. Water Park ----------------> 2000 Rs/day{morining 8AM to 1Pm}")
        print(" 3. Indoor Games --------------> 1500 Rs/day")
        print(" 4. To skip the choice")
        b = 0
        erent=0
        print("Enter the number which you want to add in your package->")
        print("For example if you want to add GAMING ROOM(1) and WATERPARK(2)")
        print("you have to write number 12{in acending order}")
        b = int(input("Enter number here-> "))
        etpye=''
        while True:
            if b == 1:
                erent = ndays*3000
                print("Gaming has been added to your package")
                etype='Gaming Room'
            if b == 2:
                erent = ndays*2000
                print("Water park has been added to your package")
                etype='Water park'
            if b == 3:
                erent = ndays*1500
                etype='Indoor Games'
            if b == 4:
                erent = ndays*0
                print(" You are Not useing Hotel club")
                etype='none'
            if b == 12:
                erent= ndays*5000
                print("Gaming room and water park have been added to your package")
                etype='Gaming room + water park'
            if b == 13:
                erent = ndays*4500
                print("Gaming room and Indoor games have been added to your package")
                etype='Gaming room + Indoor games'
            if b == 23:
                erent = ndays*3500
                print("Water park and Indooe games have been added to your package")
                etype='Water park + Indoor games'
            if b == 123:
                erent = ndays*6500
                print("Gaming room, Water park and Indoor games have been added to your package")
                etype='Gaming room + Water park + Indoor games'
            else:
                print("Your entry is out of range please see example and try again")
            break
        print("Your Club rent is->")
        print("###", erent, "Rs","###")
        Cdetail= [cid, name, age, city, address, email, ndays, roomrent, roomtype, frent, foodtype, erent]
        print()
        print("Now you can display your details(6)")
        print()
        print()
    #To display Customer details
    if ch == 6:
        print("-> Name- ", name)
        print("-> Customer Id- ", cid)
        print("-> Age- ", age)
        print("-> Address- ", address)
        print("-> City- ", city)
        print("-> Email- ", email)
        print("-> Check-In date- ", checkindate)
        print("-> Check-Out date- ", checkoutdate)
        print("-> Room Type- ", roomtype)
        print("-> Room Rent- ", roomrent)
        print("-> Food Type- ", foodtype)
        print("-> Food Rent- ", frent)
        print("-> Hotel Club facilities- ", etype)
        print("-> Club Rent- ", erent)
        print()
        print("Now you can check Your TOTAL BILL(7)")
        print()
        print()
    # TOTAL BILL
    tbill=0
    if ch == 7:
        tbill = frent + erent
        print("### TOTAL BILL-> ", tbill, "Rs ###")
        print()
        print()

    #EXIT
    if ch == 8:
        print("# # # T H A N K   Y O U :) # # #")
        break
    else:
        print("Selected number is out of range please try again")
        
print("---------------------------------------------------------")

