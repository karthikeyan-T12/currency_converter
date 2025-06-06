import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

import requests

converter = CurrencyConverter()

#btc=BtcConverter()

currency_list = sorted(converter.currencies)

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_cur = combo_from.get()
        to_cur = combo_to.get()
        result = converter.convert(amount, from_cur, to_cur)
        label_result.config(text=f"{amount} {from_cur}  =  {round(result, 2)} {to_cur}")
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
    except ValueError:
        label_btc_result.config(text="Enter a valid BTC number.")
    except Exception as e:
        label_btc_result.config(text=f"Error: {e}")
# GUI SETUP

window = tk.Tk()
window.title("💱 Currency Converter ")
window.geometry("700x650")
window.configure(bg="#fafcf7")


# TITLE

tk.Label(
    window,
    text="Currency Converter ( CURRENCY+ BITCOINE)",
    font="Helvetica 22 bold",
    bg="#f7f9fc"
).pack(pady=20)

# Amount Label & Entry
tk.Label(
    window,
    text="Amount:",
    font="Helvetica 14",
    bg="#f7f9fc"
).place(x=40, y=80)

entry_amount = tk.Entry(window, width=25, font="Helvetica 12")
entry_amount.place(x=250, y=85)

# From‐Currency Dropdown
tk.Label(
    window,
    text="From (select):",
    font="Helvetica 14",
    bg="#f7f9fc"
).place(x=40, y=130)

combo_from = ttk.Combobox(
    window,
    values=currency_list,
    state="readonly",
    width=22,
    font="Helvetica 12"
)
combo_from.place(x=250, y=135)
combo_from.set("USD")  # default

# To‐Currency Dropdown
tk.Label(
    window,
    text="To (select):",
    font="Helvetica 14",
    bg="#f7f9fc"
).place(x=40, y=180)

combo_to = ttk.Combobox(
    window,
    values=currency_list,
    state="readonly",
    width=22,
    font="Helvetica 12"
)
combo_to.place(x=250, y=185)
combo_to.set("INR")  # default

# Convert & Swap Buttons
tk.Button(
    window,
    text="Convert ",
    font="Helvetica 12",
    width=12,
    command=convert_currency
).place(x=250, y=235)

tk.Button(
    window,
    text="Swap",
    font="Helvetica 12",
    width=8,
    command=swap_currency
).place(x=370, y=235)

# Result label for fiat conversion
label_result = tk.Label(
    window,
    text="",
    font="Helvetica 14 bold",
    fg="darkgreen",
    bg="#f7f9fc",
    wraplength=600
)
label_result.place(x=40, y=290)


#BTC → INR SECTION 

tk.Label(
    window,
    text="Bitcoin → INR Conversion",
    font="Helvetica 18 bold underline",
    bg="#f7f9fc"
).place(x=40, y=350)

# BTC Amount Label & Entry
tk.Label(
    window,
    text="BTC Amount:",
    font="Helvetica 14",
    bg="#f7f9fc"
).place(x=40, y=390)

entry_btc = tk.Entry(window, width=25, font="Helvetica 12")
entry_btc.place(x=250, y=395)

# Convert BTC Button
tk.Button(
    window,
    text="Convert BTC → INR",
    font="Helvetica 12",
    width=16,
    command=convert_bitcoine
).place(x=250, y=445)

# Result label for BTC conversion
label_btc_result = tk.Label(
    window,
    text="",
    font="Helvetica 14 bold",
    fg="darkred",
    bg="#f7f9fc",
    wraplength=600
)
label_btc_result.place(x=40, y=500)


#CONVERSION HISTORY 

tk.Label(
    window,
    text="Conversion History:",
    font="Helvetica 14",
    bg="#f5f8f8"
).place(x=40, y=550)

listbox_history = tk.Listbox(window, width=80, height=6, font="Helvetica 12")
listbox_history.place(x=40, y=580)

#clearhistroy
def clear_history():
    listbox_history.delete(0, tk.END)

tk.Button(
    window,
    text="Clear History",
    font="Helvetica 12",
    command=clear_history
).place(x=570, y=580)

#START MAIN LOOP 

window.mainloop()
