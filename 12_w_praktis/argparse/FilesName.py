import argparse

def ChangNameFile():
    try:

        parser=argparse.ArgumentParser(description="Process a list of files")
        # Positional arguments
        parser.add_argument("file",nargs="+",help="List of file names")
        # Optional arguments
        parser.add_argument("-u","--uppercase",action="store_true",help="Convert names to uppercase")
        parser

        arg=parser.parse_args()


        for file in arg.file:
            if arg.uppercase:
                name = file.upper()
                print(f"name : {name}\nLength : {len(file)}")
            else:
                print (f"file:{file}")
    except Exception as e:
        print(f"Error {e}")

ChangNameFile()

