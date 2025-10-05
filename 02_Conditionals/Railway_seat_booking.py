seat_type=input("Enter seat type (sleeper/AC/general/luxary)").lower()
match seat_type:
    case "sleeper":
        print("sleeper")
    case "ac":
        print("ac")
    case "general":
        print("general")
    case "luxary":
        print("luxary")
    case _:
        print("inavlid")
