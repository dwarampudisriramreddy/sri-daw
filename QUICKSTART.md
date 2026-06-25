# Quick Start Guide - Music Theory Pad Capacitor App

## 🚀 Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
npm install
```

### Step 2: Build Web Assets
```bash
npm run build
```

### Step 3: Add Platform (Choose one)

**For iOS:**
```bash
npx cap add ios
npm run sync
npm run open:ios
```

**For Android:**
```bash
npx cap add android
npm run sync
npm run open:android
```

### Step 4: Run in IDE
- **iOS**: Opens in Xcode - Click Run ▶
- **Android**: Opens in Android Studio - Click Run ▶

## 📱 What's Different in Capacitor Version?

### Native Features Added:
1. **File System Access** - MIDI files save to device Documents folder
2. **Native Sharing** - Share MIDI files via native share dialog
3. **App Lifecycle** - Handles app backgrounding/foregrounding
4. **Back Button** - Android back button handling
5. **Touch Optimized** - Already optimized for mobile touch

### How It Works:
- **Web**: Works exactly as before - downloads MIDI files
- **Native**: Uses Capacitor Filesystem to save files, then shares them

## 🔧 Development Workflow

1. **Make changes** to `src/index.html`
2. **Build**: `npm run build`
3. **Sync**: `npm run sync`
4. **Test**: Run in simulator/emulator or device

## 📦 Project Structure

```
├── src/
│   └── index.html      ← Your main app (edit this)
├── www/               ← Built files (auto-generated)
├── ios/               ← iOS project (auto-generated)
├── android/           ← Android project (auto-generated)
└── capacitor.config.json  ← Capacitor settings
```

## 🎯 Next Steps

1. Customize `capacitor.config.json` with your app details
2. Add app icons and splash screens
3. Configure app permissions if needed
4. Test on real devices!

## ⚠️ Important Notes

- Always run `npm run sync` after making changes
- The `www/` folder is generated - don't edit it directly
- Edit `src/index.html` and rebuild to see changes
- Native plugins require device/simulator to test















