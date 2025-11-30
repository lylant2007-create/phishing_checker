import tkinter as tk
from tkinter import messagebox
import re
import sys
import os
from PIL import Image, ImageTk

# --- CẤU HÌNH MÀU SẮC ---
COLOR_BG_MAIN = '#F687AA'
COLOR_BG_POPUP = '#F3A6C7'

# --- HÀM TẢI TÀI NGUYÊN ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- LOGIC KIỂM TRA PHISHING ---
Fish_Art = r"""
      /`·.¸
     /¸...¸`:·
 ¸.·´  ¸   `·.¸.·´)
: © ):´;      ¸  {
 `·.¸ `·  ¸.·´\`·¸)
     `\\´´\¸.·´
"""

def check_phishing(url):
    if len(url) > 75:
        return f"🚨 WARNING: URL too long!\nPossible Phishing.\n{Fish_Art}"
    if re.search(r'^http://', url):
        return f"⚠️ WARNING: Not Secure (HTTP).\nPossible Phishing.\n{Fish_Art}"
    if re.search(r'@', url):
        return f"🔥 DANGER: URL contains '@'.\nHigh Risk!\n{Fish_Art}"
    if re.search(r'\.(tk|ml|cf|ga|gq)', url):
        return f"🔥 DANGER: Suspicious Domain.\nHigh Risk!\n{Fish_Art}"
    
    return "✅ RESULT: The URL appears to be safe. 😌☕"

# --- CỬA SỔ KẾT QUẢ (POPUP) ---
def open_result_popup():
    url_input = url_entry.get()
    # Kiểm tra đầu vào
    if not url_input.strip() or url_input == "ENTER URL":
        messagebox.showwarning("Oops", "Please enter a URL first!", parent=root)
        return

    result_message = check_phishing(url_input)

    popup = tk.Toplevel(root)
    popup.title("RESULT")
    POPUP_W, POPUP_H = 450, 400 
    popup.geometry(f"{POPUP_W}x{POPUP_H}")
    popup.resizable(False, False)
    popup.config(bg=COLOR_BG_POPUP)

    try:
        bg_path = resource_path("popup_background.png")
        bg_img = Image.open(bg_path).resize((POPUP_W, POPUP_H), Image.Resampling.LANCZOS)
        bg_photo = ImageTk.PhotoImage(bg_img)
        
        canvas_pop = tk.Canvas(popup, width=POPUP_W, height=POPUP_H, highlightthickness=0, bg=COLOR_BG_POPUP)
        canvas_pop.pack(fill="both", expand=True)
        canvas_pop.create_image(0, 0, image=bg_photo, anchor="nw")
        popup.bg_photo = bg_photo
    except:
        canvas_pop = tk.Canvas(popup, width=POPUP_W, height=POPUP_H, bg=COLOR_BG_POPUP, highlightthickness=0)
        canvas_pop.pack(fill="both", expand=True)

    # 1. KHUNG KẾT QUẢ
    txt_result = tk.Text(popup, font=("Courier New", 11), bg="white", fg="black", relief="flat", padx=10, pady=10)
    txt_result.insert(tk.END, result_message)
    txt_result.config(state="disabled")
    canvas_pop.create_window(225, 180, window=txt_result, width=390, height=210, anchor="center")

    # 2. XỬ LÝ CLICK NÚT OK (Tọa độ trên ảnh Popup)
    def on_popup_click(event):
        # Vùng nút OK: Góc dưới phải
        # X: 360 -> 430, Y: 340 -> 375
        if 360 <= event.x <= 430 and 340 <= event.y <= 375:
            popup.destroy()

    canvas_pop.bind("<Button-1>", on_popup_click)
    
    popup.update_idletasks()
    x = (root.winfo_screenwidth() - POPUP_W) // 2
    y = (root.winfo_screenheight() - POPUP_H) // 2
    popup.geometry(f"+{x}+{y}")

# --- CỬA SỔ CHÍNH (MAIN) ---
root = tk.Tk()
root.title("Phishing Checker")
MAIN_W, MAIN_H = 500, 500
root.geometry(f"{MAIN_W}x{MAIN_H}")
root.resizable(False, False)
root.config(bg=COLOR_BG_MAIN)

try:
    main_path = resource_path("main_background.png") 
    main_img = Image.open(main_path).resize((MAIN_W, MAIN_H), Image.Resampling.LANCZOS)
    main_photo = ImageTk.PhotoImage(main_img)

    canvas_main = tk.Canvas(root, width=MAIN_W, height=MAIN_H, highlightthickness=0, bg=COLOR_BG_MAIN)
    canvas_main.pack(fill="both", expand=True)
    canvas_main.create_image(0, 0, image=main_photo, anchor="nw")
    root.main_photo = main_photo
except:
    canvas_main = tk.Canvas(root, width=MAIN_W, height=MAIN_H, bg=COLOR_BG_MAIN, highlightthickness=0)
    canvas_main.pack(fill="both", expand=True)

# 1. Ô NHẬP LIỆU (ENTRY)
url_entry = tk.Entry(root, font=("Courier New", 14), bg="white", fg="black", justify="left", bd=0)
url_entry.insert(0, "ENTER URL")

def on_entry_click(event):
    if url_entry.get() == "ENTER URL":
        url_entry.delete(0, "end")
        url_entry.config(fg='black')
def on_focus_out(event):
    if url_entry.get() == "":
        url_entry.insert(0, "ENTER URL")

url_entry.bind('<FocusIn>', on_entry_click)
url_entry.bind('<FocusOut>', on_focus_out)

# Căn chỉnh vị trí Entry: Dịch phải (320), Rộng (180)
canvas_main.create_window(320, 225, window=url_entry, width=180, height=30, anchor="center")

# 2. XỬ LÝ CLICK NÚT CHECK FISHING (Tọa độ trên ảnh Main)
def on_main_click(event):
    # Vùng nút Check: Ở dưới đáy, giữa màn hình
    # Tọa độ ước tính: X từ 130 đến 370, Y từ 440 đến 490
    if 130 <= event.x <= 370 and 440 <= event.y <= 490:
        open_result_popup()

canvas_main.bind("<Button-1>", on_main_click)

root.mainloop()