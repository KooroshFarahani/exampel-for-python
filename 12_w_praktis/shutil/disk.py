import os
import shutil

def make_folder():
    src = r"E:/exampel for python/12_w_praktis/shutil/archive"
    dst = r"E:/exampel for python/12_w_praktis/shutil/temp_folder"

    # بررسی وجود پوشه مبدأ
    if not os.path.exists(src):
        print(f"❌pooshe mabda peyda nashode {src}")
        return

    # اگر پوشه مقصد وجود دارد، اول پاکش کن
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"🗑️ pooshe ghadimi pak shode {dst}")

    # copytree خودش پوشه مقصد رو می‌سازه، نیازی به mkdir نیست
    try:
        shutil.copytree(src, dst)
        print(f"✅ copy sucsses {src} → {dst}")
    except Exception as e:
        print(f"❌ Error copy {e}")

def disk_usage():
    folder = r"E:/exampel for python/12_w_praktis/shutil/temp_folder"  # مسیر درست

    if not os.path.exists(folder):
        print(f"❌ pooshe vojood nadarad {folder}")
        return

    # قبل از حذف
    total, used, free = shutil.disk_usage(folder)
    print("=== ghab az hazf ===")
    print(f"total {total // (2**30)} GB")
    print(f"used {used // (2**30)} GB")
    print(f"free {free // (2**30)} GB")

    # فرض می‌کنیم یک زیرپوشه یا فایل داریم به نام مثلاً 'sample' درون temp_folder
    item_to_delete = os.path.join(folder, "sample")  # مثال: فرض می‌کنیم چیزی برای حذف کردن داریم
    if os.path.exists(item_to_delete):
        if os.path.isfile(item_to_delete):
            os.remove(item_to_delete)
        else:
            shutil.rmtree(item_to_delete)
        print(f"🗑️ {item_to_delete} delet")
    else:
        print(f"⚠️ {item_to_delete} vojood nadarad va hich chizi hazf nashode")

    # بعد از حذف
    total_new, used_new, free_new = shutil.disk_usage(folder)
    print("=== after delete===")
    print(f"total {total_new // (2**30)} GB")
    print(f"used {used_new // (2**30)} GB")
    print(f"free {free_new // (2**30)} GB")

# اجرا


make_folder()
disk_usage()  # حالا فعال شد (اگر مسیر درست باشد)