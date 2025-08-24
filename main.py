import os
import time
import requests
from bs4 import BeautifulSoup

# --- Environment Variables ---
VFS_EMAIL = os.getenv("VFS_EMAIL")
VFS_PASSWORD = os.getenv("VFS_PASSWORD")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# --- Telegram Alert Function ---
def send_telegram(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Telegram Error:", e)

# --- VFS Slot Checker (Demo) ---
def check_vfs_slot():
    try:
        # Example VFS URL (replace with actual)
        url = "https://visa.vfsglobal.com/sgp/en/xyz/login"
        session = requests.Session()

        # Login (Demo only – update with actual form fields)
        login_payload = {
            "Email": VFS_EMAIL,
            "Password": VFS_PASSWORD
        }
        session.post(url, data=login_payload)

        # After login, check appointment page
        appointment_url = "https://visa.vfsglobal.com/sgp/en/xyz/appointment"
        res = session.get(appointment_url)
        soup = BeautifulSoup(res.text, "html.parser")

        if "No appointment slots" in res.text:
            print("❌ No slots available")
        else:
            print("✅ Slot Found!")
            send_telegram("✅ VFS Slot Available! Check now")

    except Exception as e:
        print("Error:", e)

# --- Worker Loop ---
if __name__ == "__main__":
    while True:
        check_vfs_slot()
        time.sleep(60)  # প্রতি ১ মিনিটে চেক করবে
