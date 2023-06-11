import speedtest
from time import sleep

test = speedtest.Speedtest()
print("Welcome to the Internet Speed Test Tool...")

sleep(1)

print("Loading servers!")

test.get_servers()

print("Finding the Best Server!")

best_server = test.get_best_server()

print(f"Selected Server: {best_server['host']}\nCountry: {best_server['country']}")

sleep(0.5)

print("Testing Download Speed...")

download_speed = test.download()

print("Testing Upload Speed...")

upload_speed = test.upload()
ping = test.results.ping

print(f"Download Speed: {download_speed / 1024 / 1024:.1f} Mbps\nUpload Speed: {upload_speed / 1024 / 1024:.1f} Mbps\nPing: {ping:.1f} ms")
