import argparse

def sayHI():
    try:
        parser=argparse.ArgumentParser(description="say HI")
        parser.add_argument("name",help="Enter your name !!!",type=str)
        parser.add_argument("--age",type=int,help="This argument is optional for chang your massage!!!")

        arg=parser.parse_args()

        print(f"Hi MR OR MS {arg.name} \n")
        if arg.age>=18:
            print(f"{arg.name} you are older than 18")
        elif arg.age<18:
            print(f"{arg.name} you are teen age")
        

    except:
        print("your argument is not corect")

sayHI()