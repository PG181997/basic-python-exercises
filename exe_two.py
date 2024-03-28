'Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.'

class CalAreaAndPerim:

    def __init__(self, radius):

        self.radius = radius
        self.area = None
        self.perim = None

    def calculateArea(self):
        
        self.area = 3.1415 * (self.radius**2)

    def perimOfCircle(self):

        self.perim = 2 * 3.1415 * self.radius
    
    def resultPrint(self):

        print('The area of circle is: ', round(self.area, 2))
        print('The perimiter of circle is: ', round(self.perim, 2))

    def main(self): 

        self.calculateArea()
        self.perimOfCircle()
        self.resultPrint()


radius = int(input('Enter the radius: '))
obj = CalAreaAndPerim(radius)
obj.main()
