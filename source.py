import requests
import json

url = "https://clientsettings.roblox.com/v2/client-version/WindowsPlayer"
r = requests.get(url)
data = r.json()

print("Available data:")
for key, value in data.items():
    print(f"{key}: {value}")

v = data.get("version", "N/A")
cv = data.get("clientVersionUpload", "N/A")
bv = data.get("bootstrapperVersion", "N/A")

print(f"\nVersion: {v}")
print(f"Client Version Upload: {cv}")
print(f"Bootstrapper Version: {bv}")

# construct the download URL using the clientVersionUpload
if cv != "N/A":
    api = f"https://setup.rbxcdn.com/{cv}-Roblox.exe"
    r2 = requests.head(api)
    if r2.status_code == 200:
        size = int(r2.headers.get("Content-Length", 0))
        print(f"Download Size: {size / 1024 / 1024:.2f} MB")
        print(f"Download URL: {api}")
    else:
        print(f"Unable to fetch download information. Status code: {r2.status_code}")
else:
    print("Unable to construct download URL due to missing clientVersionUpload")
