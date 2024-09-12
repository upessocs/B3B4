def showDetails(*args):
    for i in range(len(args)):
        variable = args[i]
        print(f"The Value of { i+1 } variable is \t{variable }\t its id is \t {id(variable)}")
    
    print("\n\n")


PI = 5