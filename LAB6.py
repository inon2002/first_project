print("MENU\n1. Insert a number and ** by 3\n2. Insert 4 IPs to a list and print it\n3. Insert 4 entries to DNS_Dictionary and print it\n4. check if a string is polindrom")

menu_num = int(input("Choose a number between 1 - 4\n"))

if (menu_num == 1):
    num = int(input("Choose your number: "))
    print ("The new number is: " + str(num**3))

elif (menu_num == 2):
    ip_list = []
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    ip_list.append(input("Enter new IP: "))
    print("The IPs you entered are: \n------------\n" + str(ip_list))

elif (menu_num == 3):
    dns_dict = {}
    dns_dict.update({input("Enter new URL: "): input("Enter its ip: ")})
    dns_dict.update({input("Enter new URL: "): input("Enter its ip: ")})
    dns_dict.update({input("Enter new URL: "): input("Enter its ip: ")})
    dns_dict.update({input("Enter new URL: "): input("Enter its ip: ")})
    print("The DNS dictionary is: \n------------\n" + str(dns_dict))

elif(menu_num == 4):
    polindrom = input("Enter a string: ")
    if (polindrom == polindrom[::-1]):
        print("Your string is polindrom")
    else:
        print("Your string is not polindrom")

else:
    print ("Insert a 1-4 number!")



