def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"
    # When the computer encounters a line that has the word return on it,
    # then it knows that this line is the end of the function


print(format_name(input("Type your first name: "),input("Type your last name: ")))
