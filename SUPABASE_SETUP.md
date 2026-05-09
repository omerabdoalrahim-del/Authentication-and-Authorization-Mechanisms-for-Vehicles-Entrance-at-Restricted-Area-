# Supabase Configuration Guide

## ✅ Configuration Complete!

Your Supabase credentials have been configured across all components of the vehicle authentication system.

## 📋 Credentials Summary

- **Supabase URL**: `https://zrojirkuiukrdnbsbokk.supabase.co`
- **Anon Key**: Configured (public key for client-side operations)
- **Service Role Key**: Configured (private key for server-side operations)

## 📁 Configuration Files Created/Updated

### Backend
- **File**: `backend/.env`
- **Variables**:
  - `SUPABASE_URL`: Your Supabase project URL
  - `SUPABASE_KEY`: Anon key for basic operations
  - `SUPABASE_SERVICE_ROLE_KEY`: Service role key for admin operations
  - `DATABASE_URL`: Currently using SQLite, can be switched to Supabase PostgreSQL

### Gate Frontend (Vite + React)
- **File**: `gate-frontend/.env`
- **Variables**:
  - `VITE_SUPABASE_URL`: Your Supabase project URL
  - `VITE_SUPABASE_ANON_KEY`: Anon key for client operations
- **Note**: Vite requires the `VITE_` prefix to expose env variables to the browser

### Admin Frontend (Vite + React)
- **File**: `admin-frontend/.env`
- **Variables**:
  - `VITE_SUPABASE_URL`: Your Supabase project URL
  - `VITE_SUPABASE_ANON_KEY`: Anon key for client operations

### Frontend (Plain HTML/JS)
- **File**: `frontend/js/config.js`
- **Variables**: Global `window.SUPABASE_CONFIG` object with `url` and `anonKey`
- **Usage**: Include this script before other JS files in your HTML

## 🔐 Security Notes

### Important Security Considerations:

1. **Anon Key (Public)**: 
   - Safe to expose in frontend applications
   - Has Row Level Security (RLS) restrictions
   - Used for client-side operations

2. **Service Role Key (Private)**:
   - ⚠️ **NEVER expose this in frontend code**
   - Only use in backend/server-side code
   - Has full database access, bypasses RLS
   - Keep it in `.env` files that are NOT committed to git

3. **Git Security**:
   - Ensure `.env` files are in `.gitignore`
   - Only commit `.env.example` files (with placeholder values)
   - Never commit actual API keys to version control

## 🚀 Next Steps

### 1. Install Supabase Client Libraries

#### For Backend (Python):
```bash
cd backend
pip install supabase
```

#### For Vite Frontends (gate-frontend, admin-frontend):
```bash
cd gate-frontend  # or admin-frontend
npm install @supabase/supabase-js
```

#### For Plain HTML Frontend:
Add the Supabase JS library via CDN in your HTML:
```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script src="js/config.js"></script>
```

### 2. Initialize Supabase Clients

#### Backend (Python) Example:
```python
import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)
```

#### Frontend (Vite) Example:
```javascript
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_ANON_KEY
)
```

#### Frontend (Plain HTML/JS) Example:
```javascript
// After including the CDN script and config.js
const supabase = window.supabase.createClient(
  window.SUPABASE_CONFIG.url,
  window.SUPABASE_CONFIG.anonKey
)
```

### 3. Set Up Database Schema

You'll need to create tables in Supabase for:
- `staff` - Permanent vehicle registrations
- `visitors` - Temporary vehicle registrations with expiry
- `access_logs` - Entry/exit tracking

### 4. Configure Row Level Security (RLS)

Enable RLS policies in Supabase to secure your data:
1. Go to Supabase Dashboard → Authentication → Policies
2. Create policies for each table
3. Define who can read/write data

## 🔄 Switching from SQLite to Supabase PostgreSQL

To use Supabase as your primary database instead of SQLite:

1. **Update DATABASE_URL** in `backend/.env`:
```
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.zrojirkuiukrdnbsbokk.supabase.co:5432/postgres
```

2. **Get your database password**:
   - Go to Supabase Dashboard → Project Settings → Database
   - Find your database password (or reset it if needed)

3. **Test the connection**:
```bash
cd backend
python test_supabase_connection.py
```

## 📚 Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase JavaScript Client](https://supabase.com/docs/reference/javascript/introduction)
- [Supabase Python Client](https://supabase.com/docs/reference/python/introduction)
- [Row Level Security Guides](https://supabase.com/docs/guides/auth/row-level-security)

## ⚠️ Troubleshooting

### Frontend can't access environment variables
- **Vite**: Make sure variables start with `VITE_`
- **Plain HTML**: Include `config.js` before other scripts
- Restart dev server after changing `.env` files

### Backend can't connect to Supabase
- Check that credentials are correct in `.env`
- Ensure `supabase` Python package is installed
- Verify network connectivity to Supabase

### CORS errors
- Configure allowed origins in Supabase Dashboard
- Update backend CORS settings to match frontend URLs

## 📝 Environment Variables Template

For reference, here's what each `.env` file should contain:

### backend/.env
```bash
SUPABASE_URL=https://zrojirkuiukrdnbsbokk.supabase.co
SUPABASE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
DATABASE_URL=sqlite:///vehicle_auth.db
OPENROUTER_API_KEY=sk-or-v1-...
OCR_SPACE_API_KEY=K87666639088957
```

### gate-frontend/.env and admin-frontend/.env
```bash
VITE_SUPABASE_URL=https://zrojirkuiukrdnbsbokk.supabase.co
VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

---

**Last Updated**: January 3, 2026  
**Status**: ✅ All credentials configured and ready to use
