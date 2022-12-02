# Importing requests module to send HTTP request 
import requests

# Importing customtkintyer library to create gui
import customtkinter

# Storing the API Key inside a variable
API_KEY = 'Enter you API Key Here'

# Url of the API provider website
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Setting the appearance mode to dark
customtkinter.set_appearance_mode("dark")

# Setting the default color there to dark-blue
customtkinter.set_default_color_theme("dark-blue")

# Creating an instance of CTk class  
root = customtkinter.CTk()

# Specifying the width and height of the window 
root.geometry("250x250")

# Specifying the name of the window
root.title("Weather App")

# Making the window un-resizable
root.resizable(0,0)

# Setting an icon for the window
root.iconbitmap("Enter the full path to the icon")

# Creating an entry field to take input from the user
CITY_NAME = customtkinter.CTkEntry(master=root, placeholder_text="Enter City Name", width=150)
CITY_NAME.pack(pady = 20, padx =10)

# Creating a variable to store the number of times the button is clicked
clicks = 0

def get_details():
    global output_frame
    global output_label
    global clicks

    clicks = clicks + 1
    
    REQUEST_URL = f"{BASE_URL}?appid={API_KEY}&q={CITY_NAME.get().lower()}"
    RESPONSE = requests.get(REQUEST_URL)

    if clicks > 1 and output_frame.winfo_exists():
        output_frame.destroy()

    output_frame = customtkinter.CTkFrame(master=root, fg_color="#1a1b1b")
    output_frame.pack()

    #Checking if the connection was successful
    if RESPONSE.status_code == 200:
        DATA = RESPONSE.json()

        DATA_VALUE = {"Weather": DATA["weather"][0]["main"],
                    "Temperature": str(round(DATA["main"]["temp"] - 273.15,1)) + "°C",
                    "Humidity": str(DATA["main"]['humidity']) + "%"
                       }

        for name, value in DATA_VALUE.items():
            output_label = customtkinter.CTkLabel(master=output_frame, text=f"{name}: {value}", text_font=("Oswald", 12))
            output_label.pack()

    else:
        output_label = customtkinter.CTkLabel(master=output_frame, text="Kindly Enter Valid Details", text_color="red")
        output_label.pack()

# Creating a button
BTN = customtkinter.CTkButton(master=root, text="GET DETAILS", command=get_details)
BTN.pack(padx =10, pady =(0,30), ipadx=5)


root.mainloop()
