from tkinter import *
from tkinter import messagebox
import base64

#encrypt - decrypt function
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

#window
window = Tk()
window.minsize(500,850)
window.title("BT Secret Note's")

font = ("arial",15,"normal")
#labels
label1 = Label(text="Enter Your Title",font=font,bg="gray45")
label1.place(x=180,y=200)

label2 = Label(text="Enter Your Secret Message",font=font,bg="gray46")
label2.place(x=120,y=285)

label3 = Label(text="Enter Master Key !",font=font,bg="gray47")
label3.place(x=165,y=580)

#photo-Add
photo = PhotoImage(file="secret.png")
canvas = Canvas(height=200,width=200)
canvas.create_image(100,100,image=photo)
canvas.pack()

#entry
entry1 = Entry(width=30)
entry1.place(x=157,y=250)
entry1.focus()

entry2 = Entry(width=40)
entry2.place(x=125,y=625)
#text

text =Text(width=40,height=15)
text.place(x=90,y=325)

#botton-functions
def save_encrypt_button():
    title = entry1.get()
    message = text.get("1.0", END)
    master_secret = entry2.get()
    encode_message = encode(master_secret,message)

    if len(title) == 0 or len(message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error !",message="Please enter all info ")

    else:
        #encryption
        try:
            with open("mysecret.txt","a") as f:
                f.write(f"{title}\n{encode_message}\n")

        except FileNotFoundError:
            with open("mysecret.txt","W") as f:
                f.write(f"{title}\n{encode_message}\n")

        finally:
            entry1.delete(0,END)
            text.delete("1.0",END)
            entry2.delete(0,END)
            entry1.focus()

def decrypt_button():
    encrypted_message = text.get("1.0", END)
    master_secret = entry2.get()

    if len(encrypted_message) == 0 or len(master_secret) == 0:
        messagebox.showinfo(title="Error !",message="Please enter all info ")

    else:
        try:
            decrypted_message = decode(master_secret,encrypted_message)
            text.delete("1.0",END)
            text.insert("1.0",decrypted_message)
        except:
            messagebox.showinfo(title="Eror !!",message = "Please enter encrypted text !!")


#button
button = Button(text="Save & Encrypt",font=("times",12,"bold"),bg="gray48",command=save_encrypt_button,width=25,height=1)
button.place(x=130,y=660)

button = Button(text="Decrypt",font=("times",12,"bold"),bg="gray49",command=decrypt_button,width=25,height=1)
button.place(x=130,y=710)

window.mainloop()