import tkinter as tk
from time import strftime
import math

class CircularClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Circular Digital Clock")
        self.root.geometry("400x400")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="black")
        self.canvas.pack()

        self.clock_text = self.canvas.create_text(
            200, 200, text="", font=("Helvetica", 28, "bold"), fill="white"
        )
        
        # Draw the circular design
        self.draw_circle()
        self.update_clock()
        
        self.root.mainloop()

    def draw_circle(self):
        """Draw a colorful circular frame."""
        colors = ["cyan", "magenta", "lime", "orange", "blue"]
        for i, color in enumerate(colors):
            radius = 150 - i * 10
            self.canvas.create_oval(
                200 - radius, 200 - radius, 200 + radius, 200 + radius,
                outline=color, width=2
            )

    def update_clock(self):
        current_time = strftime("%H:%M:%S")
        self.canvas.itemconfig(self.clock_text, text=current_time)
        self.clock_text
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    CircularClock()
