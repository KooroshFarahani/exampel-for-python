import os
import shutil

# تعریف مسیرهای منبع و مقصد
src = os.path.join(os.getcwd(), "12_w_praktis", "shutil", "project")
dst = os.path.join(os.getcwd(), "12_w_praktis", "shutil", "project_backup")

adress_of_log=os.path.join(os.getcwd(),"12_w_praktis", "shutil", "project","logs")
adress_of_log_old=os.path.join(os.getcwd(), "12_w_praktis", "shutil", "project_backup","old_logs")
def mak_folder():
    try:
        os.makedirs(os.path.join(src, "logs"), exist_ok=True)
        with open(os.path.join(src, "main.py"), "w") as f:
            f.write("print('Hello')")
        with open(os.path.join(src, "logs", "log1.txt"), "w") as f:
            f.write("Log 1")
        with open(os.path.join(src, "logs", "log2.txt"), "w") as f:
            f.write("Log 2")
    except Exception as e:
        print(f"Error dar sakht log {e}")

def copy():
    try:
        # اگر پوشه مقصد وجود دارد، آن را حذف می‌کنیم تا از خطای موجود بودن جلوگیری شود
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        print(f"pooshe {src} ba movafaghatian {dst} copy shod.")
    except Exception as e:
        print(f"Error : {e}")
def diskusage():
    try:
        total,used,free=shutil.disk_usage(src)
        print(f"Total space: {total} bytes")
        print(f"Used space: {used} bytes")
        print(f"Free space: {free} bytes")
    except:
        print("cant find directory too show space")

def move():
    try :
        shutil.move(adress_of_log,adress_of_log_old)
        print ("file haye log move shod")
    except:
        print ("file haye log move nashde")

def zip():
    try:
        shutil.make_archive("project_backup",'zip',dst)
        print ("project_backup zip shod")
    except:
        print("project_backup zip nashod")

def delet():
    try:
        shutil.rmtree(dst)
        print ("pooshe project_backup bamovafaghiate hazf shod ")
    except:
        print ("pooshe hazf nashode ya nist")
mak_folder()
copy()
move()
zip()
delet()