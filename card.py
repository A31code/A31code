import tkinter as tk
from tkinter import simpledialog
import math

def draw_animated_heart(canvas, cx, cy, size, color, outline, pulse_phase, w, h):
    # Draw a heart using parametric equations, with pulsing animation
    points = []
    scale = size * (1 + 0.08 * math.sin(pulse_phase))
    for t in range(0, 360, 2):
        rad = math.radians(t)
        x = 16 * math.sin(rad) ** 3
        y = 13 * math.cos(rad) - 5 * math.cos(2 * rad) - 2 * math.cos(3 * rad) - math.cos(4 * rad)
        px = cx + x * scale
        py = cy - y * scale
        points.append((px, py))
    flat_points = [coord for point in points for coord in point]
    canvas.create_polygon(flat_points, fill=color, outline=outline, width=max(2, int(0.01*w)), smooth=True)

def draw_animated_cake(canvas, flame_phase, w, h):
    # All positions and sizes are relative to canvas size
    left = 0.325 * w
    right = 0.675 * w
    top = 0.57 * h
    bottom = 0.7 * h
    cake_height = bottom - top
    # Cake base
    canvas.create_rectangle(left, top, right, bottom, fill="#fffacd", outline="#deb887", width=max(2, int(0.01*w)))
    # Cake shadow (oval)
    canvas.create_oval(left, bottom-0.1*cake_height, right, bottom+0.2*cake_height, fill="#deb887", outline="#deb887")
    # Candles and animated flames
    candle_count = 4
    candle_width = 0.04 * w
    candle_height = 0.13 * h
    candle_top = top - candle_height
    for i in range(candle_count):
        x = left + (i+1)*(right-left)/(candle_count+1) - candle_width/2
        # Candle
        canvas.create_rectangle(x, candle_top, x+candle_width, top, fill="#87ceeb", outline="#4682b4")
        # Animated flame (flicker)
        flame_y = candle_top - 0.03*h + 0.015*h * math.sin(flame_phase + i)
        flame_color = "#ffd700" if i % 2 == 0 else "#ffec8b"
        canvas.create_oval(x+candle_width/4, flame_y, x+3*candle_width/4, flame_y+0.04*h, fill=flame_color, outline="#ffa500")

def animate(canvas, occ, name, phase=0):
    canvas.delete("all")
    w = canvas.winfo_width()
    h = canvas.winfo_height()
    border = max(4, int(0.015*w))
    # Card background
    if occ == "birthday":
        canvas.create_rectangle(0.125*w, 0.17*h, 0.875*w, 0.83*h, fill="#ffe4e1", outline="#ff69b4", width=border)
        canvas.create_text(w/2, 0.25*h, text="Happy Birthday!", font=("Comic Sans MS", int(0.08*h), "bold"), fill="#ff1493")
        canvas.create_text(w/2, 0.38*h, text=f"Dear {name},", font=("Arial", int(0.06*h)), fill="#8b008b")
        draw_animated_cake(canvas, phase, w, h)
        canvas.create_text(w/2, 0.77*h, text="Wishing you a sweet year ahead!", font=("Arial", int(0.045*h)), fill="#ff69b4")
    elif occ == "anniversary":
        canvas.create_rectangle(0.125*w, 0.17*h, 0.875*w, 0.83*h, fill="#e0ffff", outline="#4682b4", width=border)
        canvas.create_text(w/2, 0.25*h, text="Happy Anniversary!", font=("Georgia", int(0.07*h), "bold"), fill="#4169e1")
        canvas.create_text(w/2, 0.38*h, text=f"To {name},", font=("Arial", int(0.06*h)), fill="#191970")
        # Animated hearts (realistic, pulsing)
        heart_size = 0.07 * min(w, h)
        draw_animated_heart(canvas, w/2 - 0.13*w, 0.68*h, heart_size, "#ffb6c1", "#ff69b4", phase, w, h)
        draw_animated_heart(canvas, w/2 + 0.13*w, 0.68*h, heart_size, "#ffb6c1", "#ff69b4", phase + math.pi, w, h)
        canvas.create_text(w/2, 0.8*h, text="May your love grow stronger!", font=("Arial", int(0.045*h)), fill="#4169e1")
    else:
        canvas.create_text(w/2, h/2, text="Unknown occasion!", font=("Arial", int(0.06*h)), fill="red")
    # Schedule next frame
    canvas.after(50, animate, canvas, occ, name, phase + 0.15)

def main():
    root = tk.Tk()
    root.withdraw()
    occ = simpledialog.askstring("Occasion", "Enter occasion (birthday/anniversary):")
    name = simpledialog.askstring("Name", "Enter the name of the person:")
    if not occ or not name:
        return
    occ = occ.strip().lower()
    root.deiconify()
    root.title("Greeting Card")
    # Make window resizable and start with a reasonable size
    root.geometry("800x600")
    root.minsize(400, 300)
    # Fullscreen toggle with F11
    def toggle_fullscreen(event=None):
        root.attributes("-fullscreen", not root.attributes("-fullscreen"))
    root.bind("<F11>", toggle_fullscreen)
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))
    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill=tk.BOTH, expand=True)
    # Redraw on resize
    def on_resize(event):
        animate(canvas, occ, name)
    canvas.bind("<Configure>", on_resize)
    animate(canvas, occ, name)
    root.mainloop()

if __name__ == "__main__":
    main()


