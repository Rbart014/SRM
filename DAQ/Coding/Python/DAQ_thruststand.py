import tkinter as tk
from tkinter import messagebox
import serial
import time
import csv
import threading
import matplotlib.pyplot as plt

class ThrustLoggerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚀 Rocket Thrust Logger")
        self.root.geometry("400x350")
        self.root.configure(bg="#f0f0f0")
        
        self.is_recording = False
        self.serial_port = None
        self.data_thread = None
        self.start_time = 0
        self.csv_file = None
        self.csv_writer = None
        
        # --- NEW: Variable to hold our unique filename for each run ---
        self.current_filename = "" 
        
        # --- UI Elements ---
        tk.Label(root, text="COM Port:", font=("Arial", 12), bg="#f0f0f0").pack(pady=(20, 5))
        
        self.port_entry = tk.Entry(root, font=("Arial", 12), justify="center")
        self.port_entry.insert(0, "COM7") # Updated default to your working COM7!
        self.port_entry.pack(pady=5)
        
        self.thrust_label = tk.Label(root, text="0.000 N", font=("Courier", 40, "bold"), fg="#0052cc", bg="#f0f0f0")
        self.thrust_label.pack(pady=20)
        
        self.status_label = tk.Label(root, text="Status: Ready", font=("Arial", 10, "italic"), fg="gray", bg="#f0f0f0")
        self.status_label.pack(pady=5)
        
        # --- Buttons ---
        self.start_btn = tk.Button(root, text="🟢 Start Recording", font=("Arial", 14, "bold"), bg="#a8e6cf", command=self.start_recording)
        self.start_btn.pack(pady=5, fill="x", padx=60)
        
        self.stop_btn = tk.Button(root, text="🛑 Stop, Save & Graph", font=("Arial", 14, "bold"), bg="#ff8b94", state=tk.DISABLED, command=self.stop_recording)
        self.stop_btn.pack(pady=5, fill="x", padx=60)
        
    def start_recording(self):
        port = self.port_entry.get()
        
        try:
            self.serial_port = serial.Serial(port, 115200, timeout=1)
            time.sleep(1) 
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not open {port}.\n\nError: {e}")
            return
            
        # --- NEW: Create a unique file based on the exact date and time ---
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.current_filename = f"thrust_data_{timestamp}.csv"
        
        self.csv_file = open(self.current_filename, "w", newline="")
        self.csv_writer = csv.writer(self.csv_file)
        self.csv_writer.writerow(["Time (s)", "Thrust (N)"])
        
        self.is_recording = True
        self.start_time = time.time()
        
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.port_entry.config(state=tk.DISABLED)
        self.status_label.config(text="Status: 🔴 RECORDING...", fg="red")
        
        self.data_thread = threading.Thread(target=self.read_serial_data, daemon=True)
        self.data_thread.start()
        
    def read_serial_data(self):
        while self.is_recording and self.serial_port.is_open:
            try:
                if self.serial_port.in_waiting > 0:
                    line = self.serial_port.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        try:
                            thrust = float(line)
                            current_time = time.time() - self.start_time
                            
                            self.csv_writer.writerow([f"{current_time:.3f}", f"{thrust:.3f}"])
                            self.root.after(0, self.update_thrust_label, f"{thrust:.3f} N")
                            
                        except ValueError:
                            pass
            except Exception as e:
                print(f"Lost connection: {e}")
                break

    def update_thrust_label(self, text):
        self.thrust_label.config(text=text)

    def stop_recording(self):
        if not self.is_recording:
            return
            
        self.is_recording = False
        
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        if self.csv_file:
            self.csv_file.close()
            
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.port_entry.config(state=tk.NORMAL)
        
        # --- NEW: Update the label to show the exact file it just saved ---
        self.status_label.config(text=f"Status: 💾 Saved to {self.current_filename}", fg="green")
        
        self.plot_data()

    def plot_data(self):
        time_data = []
        thrust_data = []
        
        # --- NEW: Tell the graph to open the specific file we just created ---
        try:
            with open(self.current_filename, "r") as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    time_data.append(float(row[0]))
                    thrust_data.append(float(row[1]))
                    
            plt.figure(figsize=(10, 6))
            plt.plot(time_data, thrust_data, color='red', linewidth=2)
            plt.title("Rocket Motor Thrust Curve", fontsize=16, fontweight='bold')
            plt.xlabel("Time (Seconds)", fontsize=12)
            plt.ylabel("Thrust (Newtons)", fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.fill_between(time_data, thrust_data, color='red', alpha=0.1) 
            
            plt.show()
            
        except Exception as e:
            messagebox.showerror("Graphing Error", f"Could not generate graph.\n\nError: {e}")

def on_closing():
    if app.is_recording:
        app.stop_recording()
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThrustLoggerGUI(root)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()