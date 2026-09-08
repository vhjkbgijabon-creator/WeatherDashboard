import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime
from PIL import Image, ImageTk
from io import BytesIO
import threading
import os
import sys

class WeatherDashboardEXE:
    """Weather Dashboard - Standalone EXE Version"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Dashboard")
        self.root.geometry("1000x750")
        self.root.resizable(False, False)
        
        # Center window on screen
        self.center_window()
        
        # API Settings
        self.api_key = "0e20130330e2500c4751724b80400158"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        
        # Colors
        self.bg_color = "#1a1a2e"
        self.fg_color = "#ffffff"
        self.accent_color = "#00d4ff"
        self.card_bg = "#16213e"
        
        self.root.configure(bg=self.bg_color)
        self.root.iconbitmap()  # Remove default icon
        
        # Create UI
        self.create_ui()
        
        # Load default city
        self.root.after(500, lambda: self.search_weather_city("Tehran"))
        
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
    def create_ui(self):
        """Create user interface"""
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.accent_color, height=100)
        header_frame.pack(fill=tk.X)
        header_frame.pack_propagate(False)
        
        title = tk.Label(
            header_frame, 
            text="🌤️  Weather Dashboard  🌍",
            font=("Segoe UI", 28, "bold"),
            bg=self.accent_color,
            fg="#000000"
        )
        title.pack(pady=20)
        
        # Search Frame
        search_frame = tk.Frame(self.root, bg=self.bg_color)
        search_frame.pack(pady=20)
        
        tk.Label(
            search_frame,
            text="🔍 Search City:",
            font=("Segoe UI", 12, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        ).pack(side=tk.LEFT, padx=10)
        
        self.city_entry = tk.Entry(
            search_frame,
            width=30,
            font=("Segoe UI", 12),
            bg="#2d3561",
            fg=self.fg_color,
            insertbackground=self.accent_color,
            relief=tk.FLAT,
            bd=5
        )
        self.city_entry.pack(side=tk.LEFT, padx=5)
        self.city_entry.bind("<Return>", lambda e: self.search_weather())
        
        search_btn = tk.Button(
            search_frame,
            text="Search",
            command=self.search_weather,
            bg=self.accent_color,
            fg="#000000",
            font=("Segoe UI", 11, "bold"),
            cursor="hand2",
            relief=tk.FLAT,
            bd=0,
            padx=20,
            pady=5
        )
        search_btn.pack(side=tk.LEFT, padx=5)
        
        # Main Content Frame
        content_frame = tk.Frame(self.root, bg=self.bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Weather Info Card
        self.weather_frame = tk.Frame(
            content_frame,
            bg=self.card_bg,
            relief=tk.FLAT,
            bd=0
        )
        self.weather_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Weather Details Label
        self.weather_label = tk.Label(
            self.weather_frame,
            font=("Segoe UI", 13),
            bg=self.card_bg,
            fg=self.fg_color,
            justify=tk.LEFT,
            wraplength=900,
            padx=30,
            pady=30
        )
        self.weather_label.pack(fill=tk.BOTH, expand=True)
        
        # Status Label
        self.status_label = tk.Label(
            self.root,
            text="Loading weather data...",
            font=("Segoe UI", 10),
            bg=self.bg_color,
            fg=self.accent_color
        )
        self.status_label.pack(pady=10)
        
    def search_weather(self):
        """Search weather for entered city"""
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name!")
            return
        self.search_weather_city(city)
        
    def search_weather_city(self, city):
        """Fetch weather data"""
        def fetch():
            try:
                self.status_label.config(text=f"Fetching weather for {city}...")
                self.root.update()
                
                params = {
                    "q": city,
                    "appid": self.api_key,
                    "units": "metric"
                }
                
                response = requests.get(self.base_url, params=params, timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    self.display_weather(data, city)
                    self.status_label.config(text="✓ Weather data updated successfully")
                elif response.status_code == 404:
                    self.status_label.config(text="✗ City not found!")
                    messagebox.showerror("Error", "City not found! Please try another city.")
                else:
                    self.status_label.config(text=f"✗ Error: {response.status_code}")
                    messagebox.showerror("Error", f"Error: {response.status_code}")
                    
            except requests.exceptions.Timeout:
                self.status_label.config(text="✗ Request timeout")
                messagebox.showerror("Error", "Request timeout. Check your internet connection!")
            except Exception as e:
                self.status_label.config(text="✗ Error occurred")
                messagebox.showerror("Error", f"Error: {str(e)}")
        
        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()
        
    def display_weather(self, data, city):
        """Display weather information"""
        try:
            city_name = data["name"]
            country = data["sys"]["country"]
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind_speed = data["wind"]["speed"]
            wind_deg = data["wind"].get("deg", "N/A")
            description = data["weather"][0]["description"]
            
            # Wind direction
            directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                         "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
            if wind_deg != "N/A":
                dir_idx = int((wind_deg + 11.25) / 22.5) % 16
                wind_dir = directions[dir_idx]
            else:
                wind_dir = "N/A"
            
            weather_text = f"""
╔══════════════════════════════════════════════════════════════╗
║                    WEATHER INFORMATION                       ║
╚══════════════════════════════════════════════════════════════╝

🌍 Location:
   {city_name}, {country}

🌡️  Temperature:
   Current: {temp}°C
   Feels Like: {feels_like}°C
   Min: {temp_min}°C  |  Max: {temp_max}°C

📝 Condition:
   {description.capitalize()}

💧 Humidity:
   {humidity}%

🔽 Atmospheric Pressure:
   {pressure} hPa

💨 Wind:
   Speed: {wind_speed} m/s
   Direction: {wind_dir} ({wind_deg}°)

⏰ Last Updated:
   {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

╚══════════════════════════════════════════════════════════════╝
            """
            
            self.weather_label.config(text=weather_text)
            self.city_entry.delete(0, tk.END)
            self.city_entry.insert(0, city_name)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error displaying weather: {str(e)}")
            self.status_label.config(text="✗ Error displaying data")

def main():
    root = tk.Tk()
    app = WeatherDashboardEXE(root)
    root.mainloop()

if __name__ == "__main__":
    main()
