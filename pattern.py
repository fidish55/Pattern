try:
    random_num = int(input("Enter a number: "))

     # Check if the entered number is less than or equal to 5
    
    if 1<= random_num <= 5:
        stars=""
        # Loop to iterate through each row of the star pattern
        for i in range(1,random_num * 2):
             # If i is less than or equal to the entered number, add an asterisk
            if i<= random_num:
                stars += "*"
            else:
                 # If i is greater than the entered number, remove the last asterisk
                stars = stars[:-1]

            # Print the current row of the star pattern    
            print(stars)
    else:
        # If the entered number is greater than 5, print a message
        print("Please enter a number less than or equal to 5.")

except ValueError:
    # If there is a ValueError (non-numeric input), print an error message
    print("Invalid input. Please enter a numeric value.")
