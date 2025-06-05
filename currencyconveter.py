from currency_converter import CurrencyConverter
import tkinter as tk

# Create currency converter object
c = CurrencyConverter()

# Create GUI window
window = tk.Tk()
window.geometry("500x360")
window.title("Currency Converter")

# Function to convert currency
def clicked():
    try:
        amount = float(entry1.get())
        cur1 = entry2.get().upper()
        cur2 = entry3.get().upper()
        result = c.convert(amount, cur1, cur2)
        label_result.config(text=f"{amount} {cur1} = {round(result, 2)} {cur2}")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

# Title Label
label = tk.Label(window, text="Currency Converter", font="Times 20 bold")
label.place(x=100, y=40)

# Amount
label1 = tk.Label(window, text="Enter Amount:", font="Times 16 bold")
label1.place(x=70, y=100)
entry1 = tk.Entry(window)
entry1.place(x=270, y=105)

# From Currency
label2 = tk.Label(window, text="From Currency (e.g. USD):", font="Times 16 bold")
label2.place(x=30, y=150)
entry2 = tk.Entry(window)
entry2.place(x=270, y=155)

# To Currency
label3 = tk.Label(window, text="To Currency (e.g. INR):", font="Times 16 bold")
label3.place(x=20, y=200)
entry3 = tk.Entry(window)
entry3.place(x=270, y=205)

# Convert Button
button = tk.Button(window, text="Convert", font="Times 16 bold", command=clicked)
button.place(x=200, y=250)

# Result Label
label_result = tk.Label(window, text="", font="Times 16 bold")
label_result.place(x=150, y=300)

# Run the GUI
window.mainloop()
