# VFS Slot Checker Bot

এই বট VFS Global ওয়েবসাইটে প্রতি মিনিটে লগইন করে স্লট আছে কিনা চেক করে।  
যদি স্লট পাওয়া যায়, সঙ্গে সঙ্গে Telegram এ নোটিফিকেশন পাঠাবে ✅

---

## 🚀 Deploy Steps

### 1. GitHub Repo Setup
- এই ফাইলগুলো GitHub এ আপলোড করো।

### 2. Railway Deploy
- Railway Dashboard → New Project → Deploy from GitHub Repo
- Environment Variables সেট করো:
  - `VFS_EMAIL` = তোমার VFS লগইন ইমেইল
  - `VFS_PASSWORD` = তোমার VFS লগইন পাসওয়ার্ড
  - `BOT_TOKEN` = Telegram BotFather থেকে নেওয়া টোকেন
  - `CHAT_ID` = Telegram User/Group ID

### 3. Run
Railway Worker প্রতি মিনিটে চেক করবে এবং স্লট পাওয়া মাত্র Telegram এ মেসেজ পাঠাবে।
