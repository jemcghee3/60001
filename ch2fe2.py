# Introduction to Computation and Programming Using Python (2021)
# Chapter 2, Finger Exercise 2
# Write code that asks the user to enter their
# birthday in the form mm/dd/yyyy, and then prints a string of the
# form ‘You were born in the year yyyy.’

dob = input("When were you born? (mm/dd/yyyy): ")
print(f"You were born in the year {dob[-4:]}.")

# note: no input checking
