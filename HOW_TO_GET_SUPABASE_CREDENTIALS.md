# 🔑 How to Get Your Real Supabase Connection String

## Step-by-Step Guide:

### 1. Open Supabase Dashboard
Go to: https://supabase.com/dashboard/projects

### 2. Select Your Project
- Click on your project from the list
- OR create a new project if you don't have one

### 3. Get Connection String
1. Click **"Project Settings"** (gear icon in the left sidebar)
2. Click **"Database"** in the settings menu
3. Scroll down to **"Connection string"** section
4. Click on the **"URI"** tab
5. You'll see a string that looks like:
   ```
   postgresql://postgres.xxxxxxxxxxxxxx:[YOUR-PASSWORD]@aws-0-us-east-1.pooler.supabase.com:6543/postgres
   ```
6. **IMPORTANT**: We need the **DIRECT** connection (not pooler):
   - Look for "Connection parameters" section on the same page
   - Find the **Host** field - it should look like: `db.xxxxxxxxxxxxxx.supabase.co`
   - The `xxxxxxxxxxxxxx` part is your PROJECT REFERENCE

### 4. What to Send Me
Please provide EXACTLY what you see:

**Option A - Send the full connection string:**
Copy the entire connection string from Supabase dashboard and send it to me

**Option B - Send individual components:**
- Project Reference: `xxxxxxxxxxxxxx` (found in Host: `db.xxxxxxxxxxxxxx.supabase.co`)
- Password: `your-password-here`
- Region: `us-east-1` (or whatever region your project is in)

---

## 🚨 Common Issues:

### "I can't find my project"
- Your project might be paused due to inactivity
- You might be logged into the wrong Supabase account
- The project might have been deleted

### "My project is paused"
- Click on the project
- Click "Restore project" or "Resume"
- Wait a few minutes for it to become active

### "I don't have a Supabase project"
**Create a new one:**
1. Go to https://supabase.com/dashboard
2. Click **"New Project"**
3. Choose:
   - Name: `VehicleAuthSystem`
   - Database Password: Create a SIMPLE password (avoid `@` and `#` if possible)
   - Region: Choose closest to Malaysia (e.g., `ap-southeast-1` Singapore)
4. Click **"Create new project"**
5. Wait 2-3 minutes for setup
6. Then get the connection string as described above

---

## 📝 Example of what I need:

**Example connection string:**
```
postgresql://postgres:[password]@db.zrojirkuiukrdnbsbokk.supabase.co:5432/postgres
```

The important part is **`zrojirkuiukrdnbsbokk`** - this is the PROJECT REFERENCE.

It's typically a 20-character random string like:
- `zrojirkuiukrdnbsbokk`
- `abcdefghijklmnopqrst` ❌ (This is just an example, not a real one)
- `xyzabc1234567890abcd`

---

## ⏭️ Once You Provide the Correct Info:

I will:
1. ✅ Update your `.env` file with correct credentials
2. ✅ Test the database connection
3. ✅ Initialize database tables (staff, visitor, access_log)
4. ✅ Start the backend server
5. ✅ Set up and test the frontends
6. ✅ Run complete end-to-end tests

**Just need your real Supabase project details!** 🚀
