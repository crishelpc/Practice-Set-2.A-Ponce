def leap_year(year: int):     
    '''
    Calculate the leap year that divisible by 4. 

    Args: 
         year = leap year 

    Return 
         The calculated leap year by divisible by 4.
    '''
    if (year % 4) == 0:
        if (year % 100  == 0) and (year % 400 != 0):
            return "not a leap year"
        else: 
            return "leap year"
    else:
        return "not a leap year"
    
input_year = int(input("Year: "))
print(leap_year(input_year))