# Function here


def anonymous(question):

    warning = "Do you want to keep going ? "
    valid = False
    while not valid:
        response = input(question)
        if response == "":
            check = False
            print("You have entered blank. This will make you appear as an anonymous")
            while not check:
                answer = input(warning)
                if answer.lower() == "yes":
                    print("You have chosen to be appeared as an anonymous")
                    response = 'anonymous'
                    return response
                elif answer.lower() == "no":
                    print("You have chosen to go back")
                    break
                else:
                    print("Please choose between yes or no")

        else:
            return response


# Main routine goes here
user_name = anonymous("Name: ")
print("Name: {}".format(user_name))