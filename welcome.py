import tkinter
from customtkinter import *
from PIL import Image, ImageTk

#from MainPage import main

def welcomeFrame():
    global backImage
    welcome_root = CTk()
    welcome_root.title("i-Mage")
    welcome_root.iconbitmap("Image/favicon.ico")
    set_appearance_mode("dark")
    set_default_color_theme("green")

    width = 900
    height = 600
    x = (welcome_root.winfo_screenwidth() / 2) - (width / 2)
    y = (welcome_root.winfo_screenheight() / 2) - (height / 2)
    welcome_root.geometry(f"{width}x{height}+{int(x)}+{int(y)}")
    welcome_root.resizable(width=FALSE, height=FALSE)

    backImage = CTkImage(Image.open("Image/landing_bg.png"), size=(900, 600))
    main_Canva = CTkLabel(welcome_root, image=backImage, text="")
    main_Canva.pack()
    brand = CTkImage(Image.open("Image/i-logo.png"), size=(190, 78))

    w_Frame = CTkFrame(master=main_Canva, width=500, height=350, bg_color="#2B2B2B", border_width=1,
                        border_color="#00A36C", corner_radius=12)
    w_Frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    logo = CTkLabel(master=w_Frame, image=brand, text="")
    logo.place(x=160, y=10)

    header = CTkLabel(master=w_Frame, text="Welcome", font=("Poppins", 38, "bold"), bg_color="transparent",
                        text_color="#ffffff")
    header.place(x=160, y=120)

    subHeader = CTkLabel(master=w_Frame,
                            text=" A program to provide image processing services\n for a wide range of users",
                            font=("Poppins", 16), text_color="#ffffff")

    subHeader.place(x=50, y=184)


    startButton = CTkButton(master=w_Frame, text="Get Started", fg_color="#00A36C", width=160, height=50,
                            font=("Poppins", 16), hover_color="#00A36C")
    startButton.place(x=175, y=260)

    welcome_root.mainloop()

welcomeFrame()



