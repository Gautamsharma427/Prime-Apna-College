# Match case isn't Used as much 

#Traffic Light
light =input("COLOR: ")
match light:
    case "red":
        print("STOP")
    case "green":
        print("GO")
    case "yellow":
        print("WAIT")
    case _:
        print("wrong colour")