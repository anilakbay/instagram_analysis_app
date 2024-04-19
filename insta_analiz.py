import instaloader
import tkinter as tk
from tkinter import ttk, messagebox

# kullanıcı bilgilerini çek
def get_user_info(username):
    bot = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(bot.context, username)

    # bir sözlük oluştur
    user_info = {
        "Username": profile.username,
        "Followers": profile.followers,
        "Followees": profile.followees,
        "Post Count": profile.mediacount,
        "Last Post Date": get_last_post_date(profile)
    }
    return user_info

# kullanıcının son gönderi tarihi çekme
def get_last_post_date(profile):
    last_post = None

    for post in profile.get_posts():
        if not last_post or post.date_utc > last_post.date_utc:
            last_post = post
    return last_post.date_utc.strftime("%Y-%m-%d  %H:%M:%S")

# kulllanıcı bilgilerini görüntüle
def show_user():
    username = entry_username.get()
    user_info = get_user_info(username)
    if isinstance(user_info, dict):
        for widget in tree.get_children():
            tree.delete(widget)
        # tabloya kullanıcı verilerini ekle.
        tree.insert("", "end", values=(
            user_info["Username"],
            user_info["Followers"],
            user_info["Followees"],
            user_info["Post Count"],
            user_info["Last Post Date"]
        ))
    else:
        # hata mesajı gönder
        messagebox.showerror("Hata", user_info)

# tkinter arayüzü
root = tk.Tk()
root.title("Instagram Kullanıcı  Bilgi Görüntüleyicisi")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# kullanıcı adı etiket

label = tk.Label(frame, text="Kullanıcı Adı:")
label.grid(row=0, column=0, padx=5, pady=5)

# kullanıcı adı giriş kutusu

entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=5, pady=5)

# bilgi görüntüleme kutusu

search_button = tk.Button(frame, text="Bilgileri Görüntüle", command=show_user)
search_button.grid(row=2, column=2, padx=5, pady=5)

# bilgi tablosu

tree = ttk.Treeview(root, columns=("Username", "Followers", "Followees", "Post Count", "Last Post Date"))
tree.heading("Username", text="Kullanıcı Adı")
tree.heading("Followers", text="Takipçiler")
tree.heading("Followees", text="Takip Edilenler")
tree.heading("Post Count", text="Gönderi Sayısı")
tree.heading("Last Post Date", text="Son Gönderi Tarihi")
tree.pack(padx=20, pady=20)

root.mainloop()
