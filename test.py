import time
password = "idapadasssymanny"
u = {
    "qwretyyui":{"username":"iamauser","password":"iamapassword"},
    "iadjmaosdkpogfkd":{"username":"okayhaha", "password":"iamapassylassy"},
    "opasdkaspodkapasdodka":{"username":"userðuser","password":"idapassdf3a3ymanny"},
    "opasdkaspodkapfghodka":{"username":"userðuser","password":"idapas3ffaf3afsymanny"},
    "opasdkaspodkap23odka":{"username":"userðuser","password":"idapassfafaf3fa43ymanny"},
    "opasdkaspodkahggfhpodka":{"username":"userðuser","password":"idapa33awfdsassymanny"},
    "opasdkaspodkafdspodka":{"username":"userðuser","password":"idapfwaf3fasdassymanny"},
    "opasdkaspodkapodka":{"username":"userðuser","password":"idapassa32f3fasdymanny"},
    "opasdkfgaspodkapodka":{"username":"userðuser","password":"idapasawfsdfasfsymanny"},
    "opasdkaspsfdodkapodka":{"username":"userðuser","password":"idapassf3afdfymanny"},
    "opasdkassfdfsdpodkapodka":{"username":"userðuser","password":"idapasdaafasdfsdssymanny"},
    "opasdfsdkaspodkapodka":{"username":"userðuser","password":"idapassyasdfwaf34wafmanny"},
    "opasdkaspodfsdfsdkapodka":{"username":"userðuser","password":"idapa3a3wfessymanny"},
    "opasdkaspofsddkapodka":{"username":"userðuser","password":"idapassymsdfsadfsadanny"},
    "opasdkaspfsdfsdodkapodka":{"username":"userðuser","password":"idapassy33f34afmanny"},
    "opasdkaspofsdsfddkapodka":{"username":"userðuser","password":"idapassyfddfeafwsfmanny"},
    "opasdkaspfsdfsdodkapodka":{"username":"userðuser","password":"idapassy3afeafaemanny"},
    "opasdkaspfsdasdaodkapodka":{"username":"userðuser","password":"idapass3fewafdsfymanny"},
    "opasdkaspoadsasddkapodka":{"username":"userðuser","password":"idapassymwfdsfq32sdfanny"},
    "opasdkaspofhgdhfgdkapodka":{"username":"userðuser","password":"idapassy4asdfsadfafmanny"},
    "opasdkaspofsdfsdddkapodka":{"username":"userðuser","password":"idapassysdfdfasfasfmanny"},
    "opasdkaspodkadasdasdapodka":{"username":"userðuser","password":"idapassasfdsfeasdf43qfymanny"},
    "opasdkaspodkdasdasapodka":{"username":"userðuser","password":"idapassyffasfsafmanny"},
    "opasdkaspodadasdaskapodka":{"username":"userðuser","password":"idapasfasfafasymanny"},
    "opasdkaspodkadadasdasdpodka":{"username":"userðuser","password":"idapaffdfsafsafssymanny"},
    "opasdkaspoddasdasdaskapodka":{"username":"userðuser","password":"idapafsaasfafassymanny"},
    "opasdkaspodkapdasdadasdodka":{"username":"userðuser","password":"idapafsdafsadfasfssymanny"},
    "opasdkaspodkaadadaspodka":{"username":"userðuser","password":"idapasfadafasfsymanny"},
    "opasdkaspodkadasadpodka":{"username":"userðuser","password":"idapassaewfeawfsdfymanny"},
    "opasdkaspodkaasdasdaspodka":{"username":"userðuser","password":"idapafdsafsdafafssymanny"},
    "opasdkaspodkapdsadadasodka":{"username":"userðuser","password":"idapaswfweqfqwefqsymanny"},
    "opasdkaspoddasdasdaskapodka":{"username":"userðuser","password":"idapafsfasfafssymanny"},
    "opasdkaspodkadasdadaspodka":{"username":"userðuser","password":"idapasffewfeaqfsymanny"},
    "opasdkaspodasdadasdkapodka":{"username":"userðuser","password":"idapassadfewfewqymanny"},
    "opasdkaspdadadasdasodkapodka":{"username":"userðuser","password":"idapsfsafsafsassymanny"},
    "opasdkaspsdasddodkapodka":{"username":"userðuser","password":"idapassyewfafmanny"},
    "opasdkasdaasdapodkapodka":{"username":"userðuser","password":"idapassyfwefwefewmanny"},
    "opasdkadasdasdspodkapodka":{"username":"userðuser","password":"idapassasdade2wefwymanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapassadasdasdassymanny"},
    "opasdkadasdasspodkapodka":{"username":"userðuser","password":"idapassydsaadasdanny"},
    "opasdkadassdaspodkapodka":{"username":"userðuser","password":"idapassydasdasdamanny"},
    "opasdkadasdadspodkapodka":{"username":"userðuser","password":"idapassy12313213dasmanny"},
    "opasdkaadadspodkapodka":{"username":"userðuser","password":"idapassde3dawdqymanny"},
    "opasdkaasdaspodkapodka":{"username":"userðuser","password":"idapassyd32d23manny"},
    "opasdkasddasdadspodkapodka":{"username":"userðuser","password":"idapadf43f23ssymanny"},
    "opasdkasdasdasaspodkapodka":{"username":"userðuser","password":"idapfdfdsfsadassymanny"},
    "opasdkdasdasaspodkapodka":{"username":"userðuser","password":"idapafasdadas12essymanny"},
    "opasdkdadasaspodkapodka":{"username":"userðuser","password":"idapassd21sadfdsfdsymanny"},
    "opasdkdasasdaaspodkapodka":{"username":"userðuser","password":"idapadasdasdssymanny"},
    "opasdkdaaspodkapodka":{"username":"userðuser","password":"idapassymd12dasanny"},
    "opasdkasdasdasdspodkapodka":{"username":"userðuser","password":"idapas23dasdassymanny"},
    "opasdkadasdasdasdspodkapodka":{"username":"userðuser","password":"idapdasdassymanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapasdsdawsymanny"},
    "opasdkadasdasdasdspodkapodka":{"username":"userðuser","password":"idap2312dwaassymanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapasdadsymanny"},
    "opasdkadasdasspodkapodka":{"username":"userðuser","password":"idapassdasdadasymanny"},
    "opasdkadasdspodkapodka":{"username":"userðuser","password":"idapassym323233qanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapaqf44f3q4f3fq43fq43fq43ssymanny"},
    "opasdkadasdasspodkapodka":{"username":"userðuser","password":"idapass4f4q4q34qf4ymanny"},
    "opasdkadsadasspodkapodka":{"username":"userðuser","password":"idapassyf4f4f43qf4qfmanny"},
    "opasdkadasdasdspodkapodka":{"username":"userðuser","password":"idapass4fqf443fq434q3ymanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapasqq4f4f43qf4q3f43qsymanny"},
    "opasdkaadsdasspodkapodka":{"username":"userðuser","password":"idapassy3qf434q3f43fmanny"},
    "opasdkasasdasdasdaspodkapodka":{"username":"userðuser","password":"idapasswefq4f4ymanny"},
    "opasdkadasasdasdadasdspodkapodka":{"username":"userðuser","password":"idapagrgw453rqssymanny"},
    "opasdkaspdadasdodkapodka":{"username":"userðuser","password":"idapassfwqfwqweymanny"},
    "opasdkaspdasasdadodkapodka":{"username":"userðuser","password":"idapasqewfewqfqewfymanny"},    
    "opasdkaspdasdassdasdaodkapodka":{"username":"userðuser","password":"idapfqeqqwassymanny"},
    "opasdkasadasdsapodkapodka":{"username":"userðuser","password":"idapassyeefqfeqmanny"},
    "opasdkasdasdadpodkapodka":{"username":"userðuser","password":"idapassyqwffqefmanny"},
    "opasdkaasdaadspodkapodka":{"username":"userðuser","password":"idapassywfqwefefqmanny"},
    "opasdkasdadasdasdasaspodkapodka":{"username":"userðuser","password":"idapeqwfewqqeeqassymanny"},
    "opasdkaspsaddadaodkapodka":{"username":"userðuser","password":"idapaefqewfeqfqfssymanny"},
    "opasdkaddasdaspodkapodka":{"username":"userðuser","password":"idapasewfqfqfqsymanny"},
    "opasdkadadasdspodkapodka":{"username":"userðuser","password":"idapassfeqfqwefqewfqewymanny"},
    "opasdkaasdasdasspodkapodka":{"username":"userðuser","password":"idapafqeqfeqssymanny"},
    "opasdkasasdfdsfdpodkapodka":{"username":"userðuser","password":"idapafweqfeqwfwessymanny"},
    "opasdkadasdasdspodkapodka":{"username":"userðuser","password":"idapafwefwfwefewssymanny"},
    "opasdkaspgfgfdgdodkapodka":{"username":"userðuser","password":"idapfqwewassymanny"},
    "opasdkasphgfhodkapodka":{"username":"userðuser","password":"idapasfewfqsymanny"},
    "opasdkaspfhgfhodkapodka":{"username":"userðuser","password":"idapassewfwefwefwymanny"},
    "opasdkaspgfhfghfgodkapodka":{"username":"userðuser","password":"idapawefwefwessymanny"},
    "opasdkasphsadaasdodkapodka":{"username":"userðuser","password":"idapfwefassymanny"},
    "opasdkaspasdasdasodkapodka":{"username":"userðuser","password":"idapassdfdsfsfsymanny"},
    "opasdkaspdhgfhfgodkapodka":{"username":"userðuser","password":"idapassyddmanny"},
    "opasdkaspdgdfdgfodkapodka":{"username":"userðuser","password":"idapassyeedqwdqwmanny"},
    "opasdkaspogfdfgdfgdkapodka":{"username":"userðuser","password":"idapawwrssymanny"},
    "opasdkasphsfdfdsodkapodka":{"username":"userðuser","password":"idapassgwrwregrwegymanny"},
    "opasdkaspgdfgdfodkapodka":{"username":"userðuser","password":"idapassewrgfregwergrewmanny"},
    "opasdkaspdfgdfggdfgdfgodkapodka":{"username":"userðuser","password":"idapasfrewfwerfsymanny"},
    "opasdkaspdfgdodkapodka":{"username":"userðuser","password":"idaparewfrewfwerfwerssymanny"},
    "opasdkaspodkarewfwepodka":{"username":"userðuser","password":"idapassydsafasfmanny"},
    "opasdkaspodwefgrewgdkapodka":{"username":"userðuser","password":"idapasfsfsdfasfsymanny"},
    "opasdkaspfewdwedwedweodkapodka":{"username":"userðuser","password":"idapdfsdghtrgrefgassymanny"},
    "opasdkaspregregerodkapodka":{"username":"userðuser","password":"idapassymanny"},
    "opasdkaspgeregegergodkapodka":{"username":"userðuser","password":"idapasghetrfwfregwtgsymanny"},
    "opasdkaspqwdwqdqdqodkapodka":{"username":"userðuser","password":"idapassdfdweymanny"},
    "opasdkaspogfdgreegergrdkapodka":{"username":"userðuser","password":"idapasssdasdasdasymanny"},
    "opasdkaspoqwedfwefewewfdkapodka":{"username":"userðuser","password":"idapfsaadsasdassymanny"},
    "opasdkaspowqdwefegerdkapodka":{"username":"userðuser","password":"idapadaasdsfsdssymanny"},
    "opasdkaspodregerfecdkapodka":{"username":"userðuser","password":"idapasdasdassymanny"},
    "opasdkaspogergergedkapodka":{"username":"userðuser","password":"idapadasssymanny"},
    
}
user = list(u.items())


for x in range(len(user)):
    start = time.time()
    for key,value in user[x][1].items():
        if key == "password" and value == password:
            print("ok")
        else: 
           print("ok")
end = time.time()
print("list:",format(end - start), ".2f")

for key, value in u.items():
    start = time.time()
    if value["password"] == password:
        print("ok")
    else:
         print("ok")
end = time.time()
print("dict:",format(end - start), ".2f")

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
