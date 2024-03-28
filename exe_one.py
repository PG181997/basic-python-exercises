'Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.'
from datetime import date

class Persion:
    
    def __init__(self, name, country, dob):

        self.name = name
        self.country = country
        self.dob = str(dob)
        self.age = None
        self.dobYear = None
        self.today = None

    def checkInpDateFormat(self):

        #strDate = list(self.dob)
        #print('strDate: ', self.dob)

        if '/' in self.dob:
           splitDob = self.dob.split('/')
           year = [i for i in splitDob if len(i) == 4]

        elif '-' in self.dob:
            splitDob = self.dob.split('-')
            year = [i for i in splitDob if len(i) == 4]

        elif '.' in self.dob:
            splitDob = self.dob.split('.')
            year = [i for i in splitDob if len(i) == 4]

        self.dobYear = int(year[0])
        #print('self.dobYear: ', self.dobYear)

    def ageCaluclation(self):

        self.today = date.today()
        currentYear = self.today.year
        #print('currentYear', currentYear)

        self.age = currentYear - self.dobYear
        #print('self.age: ', self.age)

    def printResult(self):

        print('Name: ', self.name)
        print('Country: ', self.country)
        print('Date of birth: ', self.dob)
        print('Age: ', self.age)

    def main(self):
        
        self.checkInpDateFormat()
        self.ageCaluclation()
        self.printResult()

name = input('Enter name:')
country = input("Enter the country: ")
dob = input('Enter date of birth: ')
#personObj = Persion('aditya', 'India', 18/10/1997)
personObj = Persion(name, country, dob)
personObj.main()

