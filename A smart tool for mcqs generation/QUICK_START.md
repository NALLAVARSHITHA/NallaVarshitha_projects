# 🚀 Quick Start Guide - Authentication System

## ⚡ Get Started in 3 Steps

### 1️⃣ Install Dependencies
```bash
cd backend
npm install bcryptjs jsonwebtoken
```

### 2️⃣ Add to `.env` file
```env
JWT_SECRET=your-super-secret-key-change-in-production
MONGO_URI=your-mongodb-connection-string
```

### 3️⃣ Start Both Servers
```bash
# Terminal 1 - Backend
cd backend
npm start

# Terminal 2 - Frontend
cd frontend-react
npm run dev
```

## 🎯 First Use

1. Open `http://localhost:5173`
2. Click **"Sign up"** to create account
3. Fill in: Username, Email, Password
4. Click **"Create Account"**
5. You're in! Start generating quizzes 🎉

## 🔑 Key Features

✅ **Secure Authentication** - JWT tokens with bcrypt password hashing  
✅ **User Isolation** - Each user has private data  
✅ **Auto-Login** - Stay logged in for 7 days  
✅ **Protected Routes** - All pages require authentication  
✅ **User Menu** - Profile info and logout in header  

## 📁 New Files Created

**Backend:**
- `backend/models/User.js` - User model
- `backend/middleware/auth.js` - JWT middleware

**Frontend:**
- `frontend-react/src/contexts/AuthContext.tsx` - Auth state
- `frontend-react/src/pages/Login.tsx` - Login page
- `frontend-react/src/pages/Register.tsx` - Register page
- `frontend-react/src/components/ProtectedRoute.tsx` - Route guard

## 🔐 API Changes

**New Endpoints:**
- `POST /auth/register` - Create account
- `POST /auth/login` - Login
- `GET /auth/verify` - Verify token
- `GET /auth/profile` - Get user info

**Updated Endpoints (Now Protected):**
- `POST /generateQuiz` - Requires auth token
- `GET /my-history` - Get your history
- `GET /my-notes` - Get your notes
- `POST /history` - Save quiz result
- `DELETE /notes/:noteId` - Delete note

## ✨ What Changed

**Before:** Everyone used `demo_user` (shared data)  
**After:** Each user has their own account and private data

**Before:** No login required  
**After:** Must register/login to use the app

**Before:** All data was public  
**After:** Complete user data isolation

## 🎨 UI Updates

- **Login Page** - Beautiful gradient design
- **Register Page** - Form validation
- **Header** - User profile menu with logout
- **Protected Routes** - Auto-redirect to login

## 📞 Need Help?

See `AUTHENTICATION_SETUP.md` for detailed documentation!

---

**That's it! Your app now has complete user authentication! 🎉**
