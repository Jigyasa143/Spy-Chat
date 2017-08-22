import time
print "********SPY SEE*********"

spy_name=raw_input("Enter your assigned name here.")

#'+' denotes the process of concatenation.

spy_salutation=raw_input("What should we call you(Mr. or Ms.)?")

#Needs to modify the above code..

if len(spy_name)>0 and len(spy_salutation)>0:
    print'Input Taken'

    spy_name=spy_salutation+" "+spy_name

#Considering the priority of opertors from right to left.

    print'Identification started....'
    start=time.time()
    time.sleep(3)
    done=time.time()

  #Need Time interval for the above code
    print"User identified"

    print"welcome\t"+spy_name

    print"Alright\t"+spy_name+"\nBefore proceeding,Lets talk a little more about you."

    spy_age=0
    spy_rating=0.0
    spy_is_online=False
    spy_age=int(raw_input("Enter Your age:"))


    print spy_age

else:
    print"Authentication failed"+"Invalid Input"


   # ifelse elif for mutlitple or guest fucntion in the project, then ask do youwant to continue as MR. Bond, Print with or logic Y or y
    #if Y==y or N==n


    def name(spy_name, spy_saluttaion,spy_age):
        print "test"




