from colorama import init, Fore,Back,Style
init(autoreset=True)
prices={"indigo":45000,"PIA":50000,"vistara":55000,"Unite Arab Emirates":60000,"Blue lines":40000}
airlines=(input('''
please select the airline you want to prefer...
    1:vistara
    2:indigo
    3:PIA
    4:United Arab Emirates
    5:Blue lines
'''))
departure_city=(input('''
please enter your departure city or country....
    1:"Lahoure"
    2:"Karachi"
    3:"delhi"
    4:"multan"
    5:"mumbai"
    
    
'''))
destination=(input('''
please select your destination from 1 to 10...
    1:sialkot
    2:sydney
    3:franc
    4:itly
    5:london
   
   
'''))
if airlines==1 or "vistara":
    airlines="vistara"
    if departure_city==1:
        departure_city = "lahore"
    elif departure_city==2:
        departure_city="karachi"
    elif departure_city == 3:
        departure_city = "delhi"
    elif departure_city == 4:
        departure_city = "multan"
    elif departure_city == 5:
        departure_city = "mumbai"
    else:
        ("invalid operation")
    if destination==1:
        destination = "sialkot"
    elif destination==2:
        destination="sydney"
    elif destination==3:
        destination="france"
    elif destination==4:
        destination="itly"
    elif destination==5:
        destination="london"
    else:
        ("invalid operation")

    print("you have selected airline",Fore.RED+Back.GREEN+(airlines),"departure city",Fore.RED+Back.GREEN+(departure_city),"and destination",Fore.RED+Back.GREEN+(destination))
    s = prices["vistara"]
    print("your fare price prediction is:", s)

    user_choice = (input('''
       please write yes to confirm your ticket...
            1: yes
            2: No
    '''))
    if user_choice == "yes":
        print("congratulations your ticket is confirmed safe travels")
        exit()
    elif user_choice == "No":
        exit()
    else:
        user_choice = (input('''
                        please try again you did something wrong...
                            1: yes
                            2: No
                        '''))
        if user_choice == "yes":
            print("congratulations your ticket is confirmed safe travels")
            exit()
        elif user_choice=="No":
            exit()

if airlines==2 or "indigo":
    airlines = "indigo"
    if departure_city == 1:
        departure_city = "lahore"
    elif departure_city == 2:
        departure_city = "karachi"
    elif departure_city == 3:
        departure_city = "delhi"
    elif departure_city == 4:
        departure_city = "multan"
    elif departure_city == 5:
        departure_city = "mumbai"
    else:
        ("invalid operation")
    if destination == 1:
        destination = "sialkot"
    elif destination == 2:
        destination = "sydney"
    elif destination == 3:
        destination = "france"
    elif destination == 4:
        destination = "itly"
    elif destination == 5:
        destination = "london"
    else:
        ("invalid operation")

    print("you have selected airline",Fore.RED+Back.GREEN+(airlines),"departure city",Fore.RED+Back.GREEN+(departure_city),"and destination",Fore.RED+Back.GREEN+(destination))
    s=prices["indigo"]
    print("your fare price prediction is:", s)

    user_choice = (input('''
        please write yes to confirm your ticket...
            1: yes
            2: No
        '''))
    if user_choice == "yes":
        print("congratulations your ticket is confirmed safe travels")
        exit()
    elif user_choice == "No":
        exit()
    else:
        user_choice = (input('''
                        please try again you did something wrong...
                            1: yes
                            2: No
                        '''))
        if user_choice == "yes":
            print("congratulations your ticket is confirmed safe travels")
            exit()
        elif user_choice=="No":
            exit()

if airlines==3 or "PIA":
    airlines = "PIA"
    if departure_city == 1:
        departure_city = "lahore"
    elif departure_city == 2:
        departure_city = "karachi"
    elif departure_city == 3:
        departure_city = "delhi"
    elif departure_city == 4:
        departure_city = "multan"
    elif departure_city == 5:
        departure_city = "mumbai"
    else:
        ("invalid operation")
    if destination == 1:
        destination = "sialkot"
    elif destination == 2:
        destination = "sydney"
    elif destination == 3:
        destination = "france"
    elif destination == 4:
        destination = "itly"
    elif destination == 5:
        destination = "london"
    else:
        ("invalid operation")

    print("you have selected airline",Fore.RED+Back.GREEN+(airlines),"departure city",Fore.RED+Back.GREEN+(departure_city),"and destination",Fore.RED+Back.GREEN+(destination))
    s=prices["PIA"]
    print("your fare price prediction is:", s)
    user_choice = (input('''
        please write yes to confirm your ticket...
            1: yes
            2: No
        '''))
    if user_choice == "yes":
        print("congratulations your ticket is confirmed safe travels")
        exit()
    elif user_choice == "No":
        exit()
    else:
        user_choice = (input('''
                please try again you did something wrong...
                    1: yes
                    2: No
                '''))
        if user_choice == "yes":
            print("congratulations your ticket is confirmed safe travels")
            exit()
        elif user_choice=="No":
            exit()


if airlines==4 or "United Arab Emirates":
    airlines = "United Arab Emirates"
    if departure_city == 1:
        departure_city = "lahore"
    elif departure_city == 2:
        departure_city = "karachi"
    elif departure_city == 3:
        departure_city = "dellhi"
    elif departure_city == 4:
        departure_city = "multan"
    elif departure_city == 5:
        departure_city = "mumbai"
    else:
        ("invalid operation")
    if destination == 1:
        destination = "sialkot"
    elif destination == 2:
        destination = "sydney"
    elif destination == 3:
        destination = "france"
    elif destination == 4:
        destination = "itly"
    elif destination == 5:
        destination = "london"
    else:
        ("invalid operation")

    print("you have selected airline",Fore.RED+Back.GREEN+(airlines),"departure city",Fore.RED+Back.GREEN+(departure_city),"and destination",Fore.RED+Back.GREEN+(destination))
    s=prices["Unite Arab Emirates"]
    print("your fare prediction is:", s)
    user_choice = (input('''
        please write yes to confirm your ticket...
            1: yes
            2: No
        '''))
    if user_choice == "yes":
        print("congratulations your ticket is confirmed safe travels")
        exit()
    elif user_choice == "No":
        exit()
    else:
        user_choice = (input('''
                        please try again you did something wrong...
                            1: yes
                            2: No
                        '''))
        if user_choice == "yes":
            print("congratulations your ticket is confirmed safe travels")
            exit()
        elif user_choice=="No":
            exit()


if airlines==5 or "Blue lines":
    airlines = "Blue lines"
    if departure_city == 1:
        departure_city = "lahore"
    elif departure_city == 2:
        departure_city = "karachi"
    elif departure_city == 3:
        departure_city = "delhi"
    elif departure_city == 4:
        departure_city = "multan"
    elif departure_city == 5:
        departure_city = "mumbai"
    else:
        ("invalid operation")
    if destination == 1:
        destination = "sialkot"
    elif destination == 2:
        destination = "sydney"
    elif destination == 3:
        destination = "france"
    elif destination == 4:
        destination = "itly"
    elif destination == 5:
        destination = "london"
    else:
        ("invalid operation")

    print("you have selected airline",Fore.RED+Back.GREEN+(airlines),"departure city",Fore.RED+Back.GREEN+(departure_city),"and destination",Fore.RED+Back.GREEN+(destination))
    s=prices["Blue lines"]
    print("your fare price prediction is:", s)
    user_choice=(input('''
    please write yes to confirm your ticket...
        1: yes
        2: No
    '''))
    if user_choice=="yes":
        print("congratulations your ticket is confirmed safe travels")
        exit()
    elif user_choice=="No":
        exit()
    else:
        user_choice = (input('''
                        please try again you did something wrong...
                            1: yes
                            2: No
                        '''))
        if user_choice == "yes":
            print("congratulations your ticket is confirmed safe travels")
            exit()
        elif user_choice=="No":
            exit()


