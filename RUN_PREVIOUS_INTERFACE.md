# 🚀 COMPLETE SETUP INSTRUCTIONS - Your Previous Good Interface

## ✅ WHAT YOU NEED

You have **TWO systems** in your project:

### ❌ **CURRENT (Don't use)**: Flask + dashboard.html
- Simple auto-scan mode
- Basic camera interface
- The one you DON'T like

### ✅ **PREVIOUS (Use this!)**: FastAPI + React frontends
- Professional admin dashboard
- Modern gate view with camera
- The one you HAD before and LIKED

---

## 📦 **STEP-BY-STEP SETUP**

### **Step 1: Install Backend Dependencies**

Open PowerShell in `backend/` folder:

```powershell
cd C:\Users\WIS\OneDrive\Desktop\vehicle-auth-system\backend

# Install FastAPI and dependencies
pip install fastapi uvicorn[standard] python-multipart
```

### **Step 2: Start FastAPI Backend**

```powershell
python phase1_app.py
```

**Expected output:**
```
[DB] Connecting to database...
[SECURITY] CORS allowed origins: ['http://localhost:3000', 'http://localhost:3001']
[PHASE 1] Initializing system...
[DB] ✓ Database tables ready
[ANPR] ✓ ANPR processor ready
[PHASE 1] ✓ System operational!
INFO:     Uvicorn running on http://0.0.0.0:5000
```

**If it hangs or fails**, the issue is likely in `anpr.py` (ANPR processor initialization).

---

### **Step 3: Start Admin Frontend** (New Terminal

)

```powershell
cd C:\Users\WIS\OneDrive\Desktop\vehicle-auth-system\admin-frontend

# Install dependencies (first time only)
npm install

# Start development server
npm run dev
```

**Opens at:** http://localhost:5173

This is the **admin dashboard** for managing vehicles!

---

### **Step 4: Start Gate Frontend** (New Terminal)

```powershell
cd C:\Users\WIS\OneDrive\Desktop\vehicle-auth-system\gate-frontend

# Install dependencies (first time only)
npm install

# Start development server  
npm run dev
```

**Opens at:** http://localhost:5174

This is the **gate view** with live camera scanning!

---

## 🔧 **TROUBLESHOOTING**

### Backend won't start (hangs at "python phase1_app.py")

**Problem:** `anpr.py` is trying to load heavy ML models

**Quick Fix:** Comment out ANPR initialization temporarily

Edit `phase1_app.py` lines 60-62:
```python
# Initialize ANPR
# anpr_processor = ANPRProcessor()  # COMMENT THIS OUT
anpr_processor = None  # Use None for now
print("[ANPR] ✓ ANPR processor ready")
```

This lets the backend start, but OCR won't work. You can fix it later.

---

### Frontend can't connect to backend

**Check:**
1. Backend is running on port 5000
2. Check browser console for CORS errors
3. Make sure `phase1_app.py` is running, NOT `app.py`

---

### npm install fails

**Run:**
```powershell
npm cache clean --force
npm install
```

---

## 🎯 **WHAT EACH PART DOES**

| Component | Purpose | URL |
|-----------|---------|-----|
| `phase1_app.py` | FastAPI backend with proper endpoints | http://localhost:5000 |
| `admin-frontend` | React app for admins to manage vehicles | http://localhost:5173 |
| `gate-frontend` | React app for gate operators to scan plates | http://localhost:5174 |

---

## 📝 **API ENDPOINTS (FastAPI)**

Your React frontends need these:

- `GET /api/admin/vehicles/all` - Get all vehicles
- `POST /api/admin/vehicle/register` - Register vehicle
- `DELETE /api/admin/vehicle/{id}` - Delete vehicle
- `POST /api/gate/check-access` - Process plate image at gate

These are **ONLY in phase1_app.py**, NOT in app.py!

---

## ✅ **FINAL CHECKLIST**

Before you can use the good interface:

- [ ] Stop any running `app.py` (Flask) processes
- [ ] Install FastAPI: `pip install fastapi uvicorn python-multipart`
- [ ] Start `phase1_app.py` backend
- [ ] Start `admin-frontend` (npm run dev)
- [ ] Start `gate-frontend` (npm run dev)
- [ ] Open http://localhost:5173 for admin
- [ ] Open http://localhost:5174 for gate view

---

## 🆘 **IF BACKEND STILL WON'T START**

The `anpr.py` file might be loading EasyOCR or other heavy ML libraries that take time or fail.

**Quick temporary fix:**

1. Open `phase1_app.py`
2. Find line 61: `anpr_processor = ANPRProcessor()`
3. Replace with: `anpr_processor = None`
4. Save and restart

This will let you test the frontends, but OCR scanning won't work until you fix the ANPR module.

---

## 📞 **WHAT TO DO NOW**

1. Try starting `phase1_app.py` manually in terminal
2. If it hangs, use Ctrl+C to stop it
3. Apply the temporary fix above (comment out ANPR)
4. Start backend again
5. Then start both frontends

The React interfaces are **MUCH better** than the current one!
