def fullname(first_name, last_name):
    return first_name + " " + last_name

def string_alternative(text):
    return text[::2]

if __name__ == "__main__":
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    full = fullname(first, last)
    print("Full Name:", full)
    print("Alternate chars:", string_alternative(full))
