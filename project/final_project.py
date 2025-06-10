import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter
import requests

# Currency converter setup
converter = CurrencyConverter()
currency_list = sorted(converter.currencies)

# -------- FUNCTIONS --------
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_cur = combo_from.get()
        to_cur = combo_to.get()
        result = converter.convert(amount, from_cur, to_cur)
        label_result.config(text=f"{amount} {from_cur} = {round(result, 2)} {to_cur}")
        listbox_history.insert(tk.END, f"{amount} {from_cur} ➜ {round(result, 2)} {to_cur}")
    except ValueError:
        label_result.config(text="Error: Enter a valid number for amount.")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

def swap_currency():
    a = combo_from.get()
    b = combo_to.get()
    combo_from.set(b)
    combo_to.set(a)

def clear_history():
    listbox_history.delete(0, tk.END)

def convert_bitcoine():
    try:
        btc_amount = float(entry_btc.get())
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr"
        response = requests.get(url, timeout=5)
        data = response.json()
        rate_btc_to_inr = data["bitcoin"]["inr"]
        inr_value = btc_amount * rate_btc_to_inr
        label_btc_result.config(
            text=f"{btc_amount} BTC = ₹{round(inr_value, 2)} INR"
        )
        listbox_history.insert(
            tk.END, f"{btc_amount} BTC ➜ ₹{round(inr_value, 2)} INR"
        )
    except requests.exceptions.HTTPError as errh:
        label_btc_result.config(text="The server said: This page doesn’t exist (like 404, 500)..") 
    except requests.exceptions.ConnectionError as errc:
        label_btc_result.config(text="Your internet is off, or the server is unreachable.")
    except requests.exceptions.Timeout as errt:
        label_btc_result.config(text="API took too long to reply.")
    except requests.exceptions.RequestException as err:
        label_btc_result.config(text="Any unknown error. Catch-all.")
    except ValueError:
        label_btc_result.config(text="Enter a valid BTC number.")
    except Exception as e:
        label_btc_result.config(text=f"Error: {e}")

#----------- GUI SETUP -----------#
window = tk.Tk()
window.title("💱 Currency Converter ")
window.geometry("700x680")
window.configure(bg="#eaf6f6") 

# Title
tk.Label(
    window,
    text="Currency Converter ( CURRENCY + BITCOIN )",
    font="Helvetica 22 bold",
    fg="#003366",
    bg="#eaf6f6"
).pack(pady=20)

# Amount Entry
tk.Label(
    window, 
    text="Amount:", 
    font="Helvetica 14", 
    bg="#eaf6f6", 
    fg="#333"
).place(x=40, y=80)

entry_amount = tk.Entry(window, width=25, font="Helvetica 12", bg="#f9ffff", fg="#000")
entry_amount.place(x=250, y=85)

# From Currency
tk.Label(
    window, 
    text="From (select):", 
    font="Helvetica 14", 
    bg="#eaf6f6", 
    fg="#333"
).place(x=40, y=130)

combo_from = ttk.Combobox(window, values=currency_list, state="readonly", width=22, font="Helvetica 12")
combo_from.place(x=250, y=135)
combo_from.set("USD")

# To Currency
tk.Label(
    window,
    text="To (select):",
    font="Helvetica 14", 
    bg="#eaf6f6", 
    fg="#333"
).place(x=40, y=180)

combo_to = ttk.Combobox(window, values=currency_list, state="readonly", width=22, font="Helvetica 12")
combo_to.place(x=250, y=185)
combo_to.set("INR")

# Convert and Swap Buttons

tk.Button(
    window, 
    text="Convert", 
    font="Helvetica 12 bold", 
    bg="#cce7ff", 
    relief=tk.FLAT,
    fg="#003366", 
    width=12, 
    command=convert_currency
).place(x=250, y=235)

tk.Button(
    window, 
    text="Swap", 
    font="Helvetica 12 bold", 
    bg="#d0f0c0", 
    fg="#2d572c", 
    relief=tk.FLAT,
    width=8, 
    command=swap_currency
).place(x=370, y=235)

# Result
label_result = tk.Label(window, text="", font="Helvetica 14 bold", fg="#006400", bg="#eaf6f6", wraplength=600)
label_result.place(x=40, y=290)

# -------- BTC SECTION --------#

btc_frame = tk.Frame(window, bg="#f1fbfa", bd=2, relief=tk.GROOVE)
btc_frame.place(x=40, y=340, width=620, height=170)

tk.Label(
    btc_frame, 
    text="Bitcoin → INR Conversion", 
    font="Helvetica 16 bold underline",
    bg="#f1fbfa", 
    fg="#003366"
).place(x=10, y=10)

tk.Label(
    btc_frame, 
    text="BTC Amount:", 
    font="Helvetica 13", 
    bg="#f1fbfa", 
    fg="#333"
).place(x=10, y=60)

entry_btc = tk.Entry(btc_frame, width=25, font="Helvetica 12", bg="#f9ffff", fg="#000")
entry_btc.place(x=150, y=60)

tk.Button(
    btc_frame, 
    text="Convert BTC → INR", 
    font="Helvetica 12 bold", 
    bg="#ffe6e6", 
    fg="#800000",
    relief=tk.FLAT, 
    width=16, 
    command=convert_bitcoine
).place(x=150, y=100)

label_btc_result = tk.Label(btc_frame, text="", font="Helvetica 13 bold", fg="#800000", bg="#f1fbfa", wraplength=560)
label_btc_result.place(x=140, y=135)

# -------- History --------#

tk.Label(
    window, 
    text="Conversion History:", 
    font="Helvetica 14", 
    bg="#eaf6f6",
    fg="#333"
).place(x=40, y=530)

listbox_history = tk.Listbox(window, 
                             width=69, 
                             height=6, 
                             font="Helvetica 12", 
                             bg="#ffffff", 
                             fg="#333",
                             bd=0, 
                             highlightthickness=1, 
                             highlightbackground="#cfcfcf")
listbox_history.place(x=40, y=560)

tk.Button(
    window,
    text="Clear History",
    font="Helvetica 12",
    bg="yellow",
    fg="#000000",
    relief=tk.FLAT,
    command=clear_history
).place(x=558, y=530)

# Main loop
window.mainloop()
