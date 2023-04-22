import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# تعيين حجم النافذة
root = tk.Tk()
root.geometry("259x482")

# حدد مجلد الصور
def select_folder():
    global folder_path
    folder_path = filedialog.askdirectory()

# تحديد مجلد التصدير
def select_export_folder():
    global export_folder_path
    export_folder_path = filedialog.askdirectory()

# تغيير حجم الصور
def resize_images():
    # الحصول على القيم المدخلة من المستخدم
    width = int(entry_x.get())
    height = int(entry_y.get())
    dim = (width, height)

    # حساب عدد الصور في المجلد
    num_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

    # إنشاء شريط التقدم
    progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
    progress_bar.pack(pady=20)

    # حلقة لتطبيق الأمر على جميع الصور في المجلد
    count = 0
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"): 
            # تحميل الصورة
            img = cv2.imread(os.path.join(folder_path, filename))

            # تغيير حجم الصورة
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

            # حفظ الصورة الجديدة في المجلد المحدد
            if export_folder_path:
                cv2.imwrite(os.path.join(export_folder_path, filename), resized)
            else:
                cv2.imwrite(os.path.join(folder_path, filename), resized)
        else:
            continue

        # تحديث قيمة شريط التقدم
        count += 1
        progress_bar['value'] = (count / num_files) * 100
        root.update_idletasks()

    # إخفاء شريط التقدم بعد الانتهاء من تغيير حجم الصور
    progress_bar.pack_forget()

# إنشاء الزر لتحديد المجلد
button1 = tk.Button(root, text='Select image Folder', command=select_folder)
button1.pack(pady=20)

# إنشاء مربعات النص لإدخال الأبعاد الجديدة
label_x = tk.Label(root, text="New Width:")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

label_y = tk.Label(root, text="New Height:")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()

# إنشاء زر لتحديد مجلد التصدير
button2 = tk.Button(root, text='Select Export Folder', command=select_export_folder)
button2.pack(pady=20)

# إنشاء الزر لتغيير حجم الصور وإضافة شريط التقدم
button3 = tk.Button(root, text='Resize Images', command=resize_images)
button3.pack(pady=20)

# إضافة توقيع
signature = tk.Label(root, text="By Bigwolf", font=("Arial Bold", 10))
signature.pack(side="bottom")

root.title("ResizeImage")
root.mainloop()
