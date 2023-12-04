from ast import main
from operator import le

- Ex2. Leap Year checker (function must return a boolean)

	To determine whether a year is a leap year, follow these steps:

    	If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
    	If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
    	If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
    	The year is a leap year (it has 366 days).
  	The year is not a leap year (it has 365 days).

def leap_year(year):
    return None

if __name__ == "__main__":
    print(leap_year(0)) # change the paramter to test the outcome
