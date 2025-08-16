from datetime import datetime , timedelta
def time ():
    try:
        now = datetime.now()
        now_time =now.strftime("%Y - %m - %d")
        print (f"Today: {now_time}")
    
        date=float(input("how many day latar : "))
        if date >0:
            future = now + timedelta(days=date)
            print (f"{date} days later : {future.strftime("%Y - %m - %d")}")
        else:
            raise ValueError("number of the days must be positive !!!")
    except ValueError as e :
        print (f"Error {e}")

time()