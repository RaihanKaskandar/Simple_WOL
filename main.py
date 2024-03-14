import tkinter  
import customtkinter
import pickle
from wakeonlan import send_magic_packet

def send_wol_packet(mac_address):
    try:
        send_magic_packet(mac_address)
        print("Turned on the server!")
    except:
        print("Couldn't turn on server!")

def main():
    print("Running WOL Application!")

    # # DEZE WERKT!!!
    # send_magic_packet('C8:7F:54:0B:A0:C7')
    
    # System Settings
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    # Create the main window
    app = customtkinter.CTk() 
    app.geometry("1280x720")
    app.title("Raihan-Odin WOL App") 

    # Adding UI elements
    title = customtkinter.CTkLabel(app, text="Raihan-Odin", font=("Arial", 50, "bold"))
    title.pack(padx=20, pady=10)

    # MAC Address
    mac_address = 'C8:7F:54:0B:A0:C7'

    # Power button
    power = customtkinter.CTkButton(app, text="Turn On", height=50, width=300, fg_color="green", font=("Arial", 20, "bold"), command=lambda: send_wol_packet(mac_address))
    power.place(relx=0.5, rely=0.5, anchor="center")

    app.mainloop()

    


if __name__ == "__main__":
    main()