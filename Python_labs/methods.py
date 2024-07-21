def calculate_age(year):
    age = 2022 - int(year)
    return age

while(continue_loop):

    year_born = input("enter the year you were born?:")
    print(calculate_age(year_born) )  

    next_loop = input("continue ? (y or n):")
    if(next_loop == "n"):
        continue_loop = false


