import argparse
def numberx2():
    try:    
        parser=argparse.ArgumentParser(description="program for make moraba")
        parser.add_argument("number",type=int,help="input number for check")
        arg=parser.parse_args()
        print(f"your number : {arg.number}")
        print(f"number resalt :{arg.number**2}")
    except:
        print("number is uncore")