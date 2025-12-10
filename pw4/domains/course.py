class Course:
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__credits = 0
    
    def input(self):
        self.__id = input("Course ID: ")
        self.__name = input("Course Name: ")
        self.__credits = int(input("Course Credit:"))
        print("----------")

    def getID(self): 
        return self.__id 

    def getName(self):
        return self.__name
    
    def getCredits(self):
        return self.__credits