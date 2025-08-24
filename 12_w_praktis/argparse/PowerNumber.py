import argparse
def PowerNumber():
    try:
        parser=argparse.ArgumentParser(description="Calculate power of a number")
        parser.add_argument("base",type=float,help="Base number")
        parser.add_argument("exponent",type=float,help="Exponent number")
        parser.add_argument("-v","--verbos",action="store_true",help="Show verbose output")

        arg=parser.parse_args()

        result=arg.base**arg.exponent

        if arg.verbos:
            print(f"Calculating {arg.base} raised to the power of {arg.exponent}...")
            print(f"Result: {result}")
        else:
            print(f"Result: {result}") 
    except:
        print("your input is not valid")
PowerNumber()