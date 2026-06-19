def NULL_not_found(object : any) -> int :
    if (object == None) :
        print(f"Nothing: None {type(object)}")
    elif (type(object) == float) :
        print(f"Chesse: nan {type(object)}")
    elif (type(object) == int) :
        print(f"Zero : 0 {type(object)}")
    elif (type(object) == str and object == "") :
        print(f"Empty: {type(object)}")
    elif (type(object) == bool) :
        print(f"Fake: False {type(object)}")
    elif (object == "Brian") :
        print("Type not Found")
    return (1)

