from datetime import datetime
with open("log.txt","w") as file:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"\n{now}\n")

