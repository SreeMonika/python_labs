class House:
    windows = 1
    doors = 1
    colour = "white"
    rooms = 1

    def __init__(self,drs):
        self.doors = drs
        print(" a house is built")
    def changecolour(self,new_colour):
        self.colour = new_colour

print("Welcome we r building a house")

house_1 = House(5)
house_2 = House(2)


print("colour of house 1 is " + house_1.colour)
print("colour of house 2 is " + house_2.colour)

house_1.changecolour("pink")

print("colour of house 1 is " + house_1.colour)
print("colour of house 2is " + house_2.colour)



#print(" amount of doors :" +str(house_1.doors))

        

 