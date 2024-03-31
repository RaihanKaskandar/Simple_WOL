import tkinter  
import customtkinter
from PIL import Image
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
    
    # System Settings
    customtkinter.set_appearance_mode("light")
    customtkinter.set_default_color_theme("green")

    # Create the main window
    app = customtkinter.CTk() 
    app.geometry("1024x576")
    app.title("Raihan-Odin WOL App") 

    app.resizable(False, False)


    # UI Elements

    # Left Frame
    left_frame = customtkinter.CTkFrame(master=app, fg_color="#700097", corner_radius=0)
    left_frame.pack(side="left", fill="y")

    # Right Frame
    right_frame = customtkinter.CTkFrame(master=app, fg_color="#F5F5F5", corner_radius=0)
    right_frame.pack(side="left", fill="both", expand=True)

    # Raihan-Odin Frame
    device_frame = customtkinter.CTkFrame(master=right_frame, fg_color="#D9D9D9", width=668, height=175, corner_radius=20)
    # device_frame.pack(side="top", fill="x", expand=True, padx=70, pady=20)
    device_frame.place(relx=0.5, rely=0.3, anchor="center")


    server_logo = customtkinter.CTkImage(light_image=Image.open("img/server-icon.png"), size=(83, 83))
    server_logo_label = customtkinter.CTkLabel(master=device_frame, image=server_logo, text="")
    server_logo_label.place(relx=0.07, rely=0.5, anchor="w")

    device_name = customtkinter.CTkLabel(master=device_frame, text="Raihan-Odin", font=("Inter", 25, "bold"))
    device_name.place(relx=0.23, rely=0.2, anchor="w")

    device_mac = customtkinter.CTkLabel(master=device_frame, text="C8:7F:54:0B:A0:C7", font=("Inter", 15))
    device_mac.place(relx=0.23, rely=0.36, anchor="w")

    device_ip = customtkinter.CTkLabel(master=device_frame, text="192.168.178.12", font=("Inter", 15))
    device_ip.place(relx=0.23, rely=0.52, anchor="w")

    device_status = customtkinter.CTkLabel(master=device_frame, text="Status: Online", font=("Inter", 15, "bold"))
    device_status.place(relx=0.23, rely=0.68, anchor="w")

    power_logo = customtkinter.CTkImage(light_image=Image.open("img/power-button-icon.png"), size=(75, 75))
    power_button = customtkinter.CTkButton(master=device_frame, image=power_logo, text="", fg_color="transparent", command=lambda: send_wol_packet('C8:7F:54:0B:A0:C7'))
    power_button.place(relx=0.85, rely=0.5, anchor="center")







    # End of UI Elements

    # MAC Address Variable
    mac_address = 'C8:7F:54:0B:A0:C7'

    # # Power button
    # power_button = customtkinter.CTkButton(app, text="Turn On", height=50, width=300, fg_color="green", font=("Arial", 20, "bold"), command=lambda: send_wol_packet(mac_address))
    # power_button.place(relx=0.5, rely=0.5, anchor="center")

    app.mainloop()

    


if __name__ == "__main__":
    main()