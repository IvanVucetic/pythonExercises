import datetime
dt = datetime.datetime.now()

print "What is your name?"
name = raw_input("> ")

print "What is your age?"
age = raw_input("> ")

print "What is your reddit username?"
username = raw_input("> ")

print "Your name is %s, you are %s years old, and your username is '%s'." % (name, age, username)

logtime = dt.strftime("%d-%m-%Y %H:%M")
logtext = "%s - NAME: %s, AGE: %s, USERNAME: %s\n" % (logtime, name, age, username)
log = open("1e_logfile.txt","a") #otvara fajl logfile_1.txt
log.write("%s" % logtext)
log.close()
