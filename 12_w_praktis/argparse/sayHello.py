import argparse

def sayheloo():
    try:
        parser=argparse.ArgumentParser(description="Print a greeting message")
        parser.add_argument("name",help="your name ")
        arg=parser.parse_args()

        print(f"heloo ,{arg.name}!!!")
    except:
        print(f"your name : {arg.name} is not corect")

sayheloo()
