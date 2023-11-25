# weather_app.py
import tkinter as tk
from weather_api import get_weather
from weather_data import WeatherData

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("400x300")
        self.root.configure(bg="#3498db")  # Set background color

        self.create_widgets()

    def create_widgets(self):
        # Entry for city name
        self.city_entry = tk.Entry(self.root, font=("Helvetica", 16), width=20, bd=2, relief="flat", justify="center")
        self.city_entry.pack(pady=20)

        # Button to get weather
        self.get_weather_button = tk.Button(self.root, text="Get Weather", command=self.get_weather,
                                            font=("Helvetica", 14), bg="#2ecc71", fg="#ffffff", padx=10, pady=5)
        self.get_weather_button.pack(pady=10)

        # Label to display weather information
        self.weather_label = tk.Label(self.root, text="", font=("Helvetica", 16), bg="#3498db", fg="#ffffff")
        self.weather_label.pack(pady=20)

    def get_weather(self):
        city_name = self.city_entry.get()
        if city_name:
            weather_data = get_weather(city_name)
            if weather_data:
                weather_info = f"Temperature: {weather_data.temperature}°C\nDescription: {weather_data.description}"
                self.weather_label.config(text=weather_info)
            else:
                self.weather_label.config(text="City not found. Please try again.")
        else:
            self.weather_label.config(text="Please enter a city name.")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
