#course: Object-oriented programming, year 2, semester 1
#academic year: 2020-21
#author: B. Schoen-Phelan
#date: 02-10-2020
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: " + message)

        #
        # Enter your own print statements below:
        #

        print("The acceleration due to Gravity is approximately 9.8 mss")

        # print only first and last of the sentence:

        print("T s")

        # use slice notation:
        print("The acceleration due to Gravity is approximately 9.8 mss"[6:18])

        # escaping a character:
        print("He said “that’s fantastic”!")
        ##I think that this works without escape chars because of the different type of double quotation marks being used?

        print("He said \"that's fantastic\"!")
        ##Likely happened due to copy paste from word doc


        # find all a's in the input word and count how many there are:

        print(message.find("a"[:]))
        print(message.count("a"))

        # replace all occurences of the character a with the - sign

        test = list(message)

        test[test.count("a")] = "-"

        print(test)

        # try this first by assignment of a location in a string and
        # observe what happens, then use replace():

        print(message.replace("a", "-"))


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out:

        testlist = list(message.split(" "))

        print(testlist)

        # append a new element to the list and print:

        testlist.append("lmao")

        print(testlist)

        # remove from the list in 3 ways:

        testlist.remove("lmao")
        testlist.remove("?")
        testlist.remove("and")

        #if the item isn't in the list an error is printed also, And? or any similar form is not recognized as two separate things, so removing "?" doesnt work this way

        print(testlist)

        # check if the word cake is in your input list:

        print(testlist.count("cake"))


        # reverse the items in the list and print:



        # reverse the list with the slicing trick:

        print(testlist[::-1])

        # print the list 3 times by using multiplication:

        print(testlist*3)

tas = Types_and_Strings()
# tas.play_with_strings()
tas.play_with_lists()
