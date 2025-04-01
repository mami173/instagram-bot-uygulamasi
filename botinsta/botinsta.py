import instaloader
import tkinter as tk
from tkinter import messagebox


def download_post():
    #kullanıcı adını alma 
    username = mmtn199.get()

    try:
        #nesne oluştur
        bot = instaloader.Instaloader()
        # profil nesnesi oluşturma
        profile = instaloader.Profile.from_username(https://www.instagram.com/mmtn199?igsh=MTBwaDQ1NzN0OGd4OA%3D%3D&utm_source=qr)
        #kullanıcı gönderilerini al 
        posts = profile.get_posts()
        #gönderileri indir

        for index,post in enumerate(posts,1):
            bot.download_post(post, target=f"{profile.username}_{index}")
        #başarı mesajı
        messagebox.showinfo("Başarılı","Gönderiler İndirildi")
    except Exception as e:
        messagebox.showerror("Hata",str(e))



root = tk.Tk()
root.title("Instagram Gönderi İndirici")
root.geometry("300x200")

#kullanıcı adını iste
label = tk.Label(root, text="Kulladını adı:")
label.pack(pady=10)
#kullanıcı adı giriş 
entry_username = tk.Entry(root)
entry_username.pack()
#indirme butonu
download_button  = tk.Button(root, text="Bilgileri İndir", command=download_post )
download_button.pack()
root.mainloop()
