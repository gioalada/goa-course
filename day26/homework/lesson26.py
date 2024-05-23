def ask_yes_no_question(question):
    while True:
        response = input(question + " (yes/no): ").strip().lower()
        if response in {"yes", "no"}:
            return response
        
        studying_in_goa = ask_yes_no_question("Are you studying in Goa?")

        if studying_in_goa == "yes":
            group = input("Which group are you in? ").strip().lower()
            if group == "group 13":
                mentor = ask_yes_no_question("Is Gabriel your mentor?")

                if mentor == "yes":
                 print("We both study here! Indeed, Gabriel is the mentor of both of us.")
        else:
            print("You are lying and not really in group 13! 😄")
    else:
        print("You are lying and not really in group 13! 😄")

print("You are lying and not really studying in Goa! 😄")