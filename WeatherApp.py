import tkinter as tk
from tkinter import messagebox
import requests
from datetime import datetime

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e3a5f")
        
        # Title
        title = tk.Label(root, text="Weather App", font=("Arial", 28, "bold"), 
                        bg="#1e3a5f", fg="white")
        title.pack(pady=20)
        
        # Search frame
        search_frame = tk.Frame(root, bg="#1e3a5f")
        search_frame.pack(pady=10)
        
        self.city_entry = tk.Entry(search_frame, font=("Arial", 16), width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind('<Return>', lambda e: self.get_weather())
        
        search_btn = tk.Button(search_frame, text="Search", font=("Arial", 14),
                               bg="#4a90e2", fg="white", command=self.get_weather,
                               cursor="hand2", relief=tk.FLAT, padx=20)
        search_btn.pack(side=tk.LEFT)
        
        # Weather display frame
        self.weather_frame = tk.Frame(root, bg="#2c5282", relief=tk.RIDGE, bd=2)
        self.weather_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        # Weather info labels
        self.city_label = tk.Label(self.weather_frame, text="", font=("Arial", 24, "bold"),
                                   bg="#2c5282", fg="white")
        self.city_label.pack(pady=10)
        
        self.temp_label = tk.Label(self.weather_frame, text="", font=("Arial", 48, "bold"),
                                   bg="#2c5282", fg="white")
        self.temp_label.pack()
        
        self.desc_label = tk.Label(self.weather_frame, text="", font=("Arial", 18),
                                   bg="#2c5282", fg="#e0e0e0")
        self.desc_label.pack(pady=5)
        
        # Details frame
        details_frame = tk.Frame(self.weather_frame, bg="#2c5282")
        details_frame.pack(pady=20)
        
        self.feels_like_label = tk.Label(details_frame, text="", font=("Arial", 12),
                                         bg="#2c5282", fg="white")
        self.feels_like_label.grid(row=0, column=0, padx=15, pady=5, sticky="w")
        
        self.humidity_label = tk.Label(details_frame, text="", font=("Arial", 12),
                                       bg="#2c5282", fg="white")
        self.humidity_label.grid(row=1, column=0, padx=15, pady=5, sticky="w")
        
        self.wind_label = tk.Label(details_frame, text="", font=("Arial", 12),
                                   bg="#2c5282", fg="white")
        self.wind_label.grid(row=0, column=1, padx=15, pady=5, sticky="w")
        
        self.pressure_label = tk.Label(details_frame, text="", font=("Arial", 12),
                                       bg="#2c5282", fg="white")
        self.pressure_label.grid(row=1, column=1, padx=15, pady=5, sticky="w")
        
        # Footer
        footer = tk.Label(root, text="Enter a city name and press Search", 
                         font=("Arial", 10), bg="#1e3a5f", fg="#a0aec0")
        footer.pack(side=tk.BOTTOM, pady=10)
        
    def get_weather(self):
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Error", "Please enter a city name")
            return
        
        # Using OpenWeatherMap API (free tier)
        api_key = "795d0d22cf67b728e9f884e11eab217b"  # You need to get a free API key from openweathermap.org
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"
        }
        
        try:
            response = requests.get(base_url, params=params)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather(data)
            elif response.status_code == 401:
                messagebox.showerror("API Error", 
                    "Invalid API key. Please get a free API key from openweathermap.org")
            elif response.status_code == 404:
                messagebox.showerror("Error", "City not found. Please try again.")
            else:
                messagebox.showerror("Error", "Failed to fetch weather data")
                
        except requests.exceptions.RequestException:
            messagebox.showerror("Connection Error", 
                "Unable to connect to weather service. Check your internet connection.")
    
    def display_weather(self, data):
        city = data['name']
        country = data['sys']['country']
        temp = round(data['main']['temp'])
        feels_like = round(data['main']['feels_like'])
        description = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        pressure = data['main']['pressure']
        
        self.city_label.config(text=f"{city}, {country}")
        self.temp_label.config(text=f"{temp}°C")
        self.desc_label.config(text=description)
        self.feels_like_label.config(text=f"Feels like: {feels_like}°C")
        self.humidity_label.config(text=f"Humidity: {humidity}%")
        self.wind_label.config(text=f"Wind: {wind_speed} m/s")
        self.pressure_label.config(text=f"Pressure: {pressure} hPa")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()