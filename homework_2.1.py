#unit converter

print("Hi there. Let me help you to convert kilometers into meters.")

#first_calc
kilometers = int(input("Please enter kilometers: "))
print("Converted to meters: " + str(kilometers * 1000))

#continue_calc
while True:
    user_answer = input("Continue? If so, type 'yes': ")

    if user_answer == "yes":
        # calculation
        kilometers = int(input("Please enter kilometers: "))
        print("Converted to meters: " + str(kilometers * 1000))
    else:
        print("OK, goodbye.")
        break




