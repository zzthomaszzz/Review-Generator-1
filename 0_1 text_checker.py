# Function
def not_blank(question):

    error = "Sorry, responses to this question must not be blank"

    valid = False
    while not valid:
        response = input(question)
        if response == "":
            print(error)
            continue
        else:
            return response




# Main Routine goes here

text_name = not_blank("Title: ")

print("You are about to review {}".format(text_name))




