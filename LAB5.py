money_dict = {'inon' : 500 , 'dad' : 1000 , 'mom' : 1500 , 'ariel' : 2000 , 'gal' : 2500}

print ("The amount of money that inon and gal have is: " + str(money_dict['inon'] + money_dict['gal']) )

money_dict.update({'dudu' : money_dict['inon'] + money_dict['gal']})

print ("The amount of entries is: " + str(len(money_dict)))

print ("idan" in money_dict)