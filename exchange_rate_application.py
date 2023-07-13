import socket, time, requests
from bs4 import BeautifulSoup
import tkinter as tk

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("google.com", 80))
    s.close()
    print("Connecting..")
except:
    print("Please check your internet connection")
    time.sleep(5)
    exit()
    
url = "https://www.doviz.com"
#I chose this site when developing the tool, you can choose any site.
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")
#The site from which we obtained the data gave the data in TL. I converted it to USD accordingly.
data = soup.find("span", {"data-socket-key": "gram-altin"}).text
data1 = soup.find("span", {"data-socket-key": "USD"}).text
data2 = soup.find("span", {"data-socket-key": "EUR"}).text
data3 = soup.find("span", {"data-socket-key": "bitcoin"}).text
data4 = soup.find("span", {"data-socket-key": "XU100"}).text
data5 = soup.find("span", {"data-socket-key": "GBP"}).text
data6 = soup.find("span", {"data-socket-key": "gumus"}).text

# Convert TRY to USD to determine the exchange rate
try_to_usd = float(data1.replace(",", "."))

# Convert the value of gold from grams to USD
dataus = str(round(float(data.replace(".", "").replace(",", ".")) / try_to_usd, 2))

# Convert XU100 value to float
xu100 = float(data4.replace(".", "").replace(",", "."))

# Remove the dollar sign from the BTC value
btc = data3.replace("$", "").strip()

window = tk.Tk()

window.geometry("620x540")
window.title("Exchange Rate Application")
window.configure(background="white")

# Main title label
element = tk.Label(window, text="Exchange Rate Application", bg="red", font="arial 30 bold")
element.pack()

# Gold value
gramsOfGold = tk.Label(window, text="Grams Of Gold", bg="red", font="arial 15 italic")
gramsOfGold.pack()
gramsOfGold.place(x=30, y=290)
goldValue = tk.Label(window, text=dataus + " USD", bg="red", font="arial 15 bold")
goldValue.pack()
goldValue.place(x=180, y=290)

# USD value
dolar = tk.Label(window, text="USD", bg="red", font="arial 15 italic")
dolar.pack()
dolar.place(x=30, y=90)
dolarValue = tk.Label(window, text=data1 + " TRY", bg="red", font="arial 15 bold")
dolarValue.pack()
dolarValue.place(x=180, y=90)

# Euro value
euro = tk.Label(window, text="EUR", bg="red", font="arial 15 italic")
euro.pack()
euro.place(x=30, y=170)
euroValue = tk.Label(window, text=str(round(float(data2.replace(",", ".")) / try_to_usd, 2)) + " USD", bg="red",
                     font="arial 15 bold")
euroValue.pack()
euroValue.place(x=180, y=170)

# BTC value
btc_label = tk.Label(window, text="BTC", bg="red", font="arial 15 italic")
btc_label.pack()
btc_label.place(x=30, y=210)
btcValue = tk.Label(window, text=btc + " USD", bg="red", font="arial 15 bold")
btcValue.pack()
btcValue.place(x=180, y=210)

# XU100 value
xu100_label = tk.Label(window, text="XU100", bg="red", font="arial 15 italic")
xu100_label.pack()
xu100_label.place(x=30, y=250)
xu100Value = tk.Label(window, text=str(xu100) + " TRY", bg="red", font="arial 15 bold")
xu100Value.pack()
xu100Value.place(x=180, y=250)

# GBP value
gbp = tk.Label(window, text="GBP", bg="red", font="arial 15 italic")
gbp.pack()
gbp.place(x=30, y=130)
gbpValue = tk.Label(window, text=str(round(float(data5.replace(",", ".")) / try_to_usd, 2)) + " USD", bg="red",
                    font="arial 15 bold")
gbpValue.pack()
gbpValue.place(x=180, y=130)

# Silver value
silver = tk.Label(window, text="Grams Of Silver", bg="red", font="arial 15 italic")
silver.pack()
silver.place(x=30, y=330)
silverValue = tk.Label(window, text=str(round(float(data6.replace(",", ".")) / try_to_usd, 2)) + " USD", bg="red",
                       font="arial 15 bold")
silverValue.pack()
silverValue.place(x=180, y=330)

window.mainloop()
