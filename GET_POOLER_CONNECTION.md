# 🔍 Supabase Connection String Finder

## Based on your screenshot, I can see you're on the "Connection String" tab.

Please help me get the CORRECT pooler connection string:

### Option 1: Check the Session Pooler Tab
1. In your Supabase dashboard (where you took the screenshot)  
2. Look for these tabs at the top:
   - Connection String
   - App Frameworks  
   - Mobile Frameworks
   - ORMs
   - MCP

3. **Click on the dropdown where it says "Method: Direct connection"**
4. **Select "Session pooler" instead**
5. The connection string should change to something like:
   ```
   postgresql://postgres.zrojirkuiukrdnbsbokk:[PASSWORD]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
   ```
6. **Copy that entire string and send it to me**

### Option 2: Manual Fix
Based on Supabase documentation, the pooler format should be:
```
postgresql://postgres.PROJECT_REF:[PASSWORD]@aws-0-REGION.pooler.supabase.com:6543/postgres
```

For your project:
```
postgresql://postgres.zrojirkuiukrdnbsbokk:@Amkabu53#1@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
```

Can you click on "Method: Direct connection" dropdown and switch to "Session pooler",  
then send me a screenshot or copy the connection string?

---

## Alternative: Try Transaction Mode

If the above doesn't work, sometimes Supabase Session Pooler needs a connection mode parameter.

Try clicking "Pooler settings" button or look for a "Mode" dropdown that might say:
- Transaction
- Session

Let me know what you see!
