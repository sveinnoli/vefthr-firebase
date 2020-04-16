
#print("------------------------------\n Start of Dict\n------------------------------")
#    u = {"opasdkpsoadkaspo":{"password":"secret1","username":"iamauser"},
#         "ADSOJ0"Qss0J":{"password":"supersecret39","username":"iamtotallynotauser"},
#         "ADSOPKopaksdpokas=2":{"password":"imsuperdubersecret64","username"."imsonotauser"}}
#    print("Type:", type(u), "\nlength:", len(u), "\nitem:", u, "\n")
#    for key,value in u.items():
#        #print("key:",key ,"value:",value)
#        print("User Id: {}\nUsername: {}\nPassword: {}\n".format(key, value["username"], value["password"]),)
#    print("------------------------------\n End of Dict")
#    
#    print("------------------------------\n Start of List\n------------------------------")
#    users = list(u.items())
#    print("Type:", type(users), "\nlength:", len(users), "\nitem", users)
#    for x in range(len(users)):
#        print("item number", x, ":", users[x])
#    print("------------------------------\n End of List\n------------------------------")


#Use dict.get or if key in dict to iterate through a dictionary to be able to confirm it dosen't exist,
        #Iterating through it as below means there are no ways to add a pass without using a sort of Boolean
        #for key, value in userbase.items():
            #if value["password"] == password:
                #print("Password: {} already exists in the database".format(password))
                #return redirect(url_for('signup'))
            #else:
                #print(value["password"], password)

        #db.child("account").push({"username":username, "password":password}) #Adds user to database
        
password = 'testing1'
userbase = {'-M4mvBdrd1nJvmYLUFoX': {'password': 'mammaþin112', 'username': 'sveinnoli112'}, '-M4mw7CFJrKyMl1dl9yX': {'password': 'testing1', 'username': 'test1'}, '-M4mw8vpRu8b96oaFKbs': {'password': 'imanotheruser1', 'username': 'anotheruser'}}
userbase_value = userbase.values()
#A dictionary containing 3 keys user IDS, each ID holds a username and a password in a dictionary as the IDS value
#i need to compare the password value of each one of the IDS and check if it is the same as the password variable
#if it is the same then it already exists and i bring up an error otherwise the password gets added to the database
#Problem is finding a way to iterate through the dictionary withouit using 2 and to compare each key with the variable


#This iterates through the dictionary and manages to find the correct password.
def credentialCheck(password):
    database_password = {}
    for key,value in userbase.items():
        if value["password"] == password:
            return print("Password already in database: {password}".format(password=value["password"]))
        else:
            print("Pass: {password} {dbpass}".format(dbpass=value["password"], password=password))
    database_password["password"] = password
    print(database_password)
    #This is unreachable if the password is found as it will use the return function to get out of the credentialCheck function
credentialCheck(password)

#This is the same as the one above just different iteration.
def credentialCheck2(password):
    database_password = {}
    for x in userbase_value:
        if password in x["password"]:
            return print("Password already in database: {password}".format(password=x["password"]))
        else:
            print("Pass:",password, x["password"])
    #This is unreachable if the password is found as it will use the return function to get out of the credentialCheck function
    database_password["password"] = password
credentialCheck2(password)

tupledict = ([('-M4mvBdrd1nJvmYLUFoX', {'password': 'mammaþin112', 'username': 'sveinnoli112'}), ('-M4mw7CFJrKyMl1dl9yX', {'password': 'testing1', 'username': 'test1'}), ('-M4mw8vpRu8b96oaFKbs', {'password': 'imanotheruser1', 'username': 'anotheruser'})])
for x in tupledict:
    print(x[1]["password"])
result = [x for values in userbase_value for x in values]
print(result)


#TODO find a way to iterate through a nested dictionary (userbase) and compare all user id's and check the password
#TODO if the database password matches the entered password do it in oneline with a nested comprehensive listing function of some sort goodluck


            #<label><p>Email:</p>
             #   <input
             #   required
            #    type="email" 
             #   name="email" 
            #    placeholder="name@email(.is/.com)"
            #    title="Enter email">
           # </label> -->

          #  <!-- <p>Comment</p>
          #  <textarea rows="4" name="comments"></textarea>

            #REDIRECT
            #return redirect(url_for('signup'))