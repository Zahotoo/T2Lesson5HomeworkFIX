# Get an empty list
myData = []

# LOOP
while True:
    # Get user's input
    userinput = input("Please enter a number: ")

    # Judge
    try:
        number = float(userinput)
        # Convert string to float
        userinput = float(userinput)
        # ADD number in to the empty list
        myData.append(userinput)
    except:
        # END LOOP
        break

print("It is your list: ", myData)

# Calculate the average
result = sum(myData) / len(myData)
print("It calculates a mean average: ", result)

quit()