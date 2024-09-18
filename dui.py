import tkinter as tk
from gpiozero import LED

red_led = LED(17)
green_led = LED(27)
blue_led = LED(22)

def update_led():
    color = led_choice.get()
    if color == "Red":
        red_led.on()
        green_led.off()
        blue_led.off()
    elif color == "Green":
        red_led.off()
        green_led.on()
        blue_led.off()
    elif color == "Blue":
        red_led.off()
        green_led.off()
        blue_led.on()

root = tk.Tk()
root.title("LED Controller")

led_choice = tk.StringVar(value="Red") 

tk.Label(root, text="Select LED to Turn On:").grid(row=0, column=0, padx=20, pady=10, sticky="w")
tk.Radiobutton(root, text="Red", variable=led_choice, value="Red", command=update_led).grid(row=1, column=0, sticky="w")
tk.Radiobutton(root, text="Green", variable=led_choice, value="Green", command=update_led).grid(row=2, column=0, sticky="w")
tk.Radiobutton(root, text="Blue", variable=led_choice, value="Blue", command=update_led).grid(row=3, column=0, sticky="w")

tk.Button(root, text="Exit", command=root.quit).grid(row=4, column=0, pady=20)

root.mainloop()
