# Capacitor App Setup Guide

## Prerequisites

1. **Node.js** (v16 or higher)
   - Download from: https://nodejs.org/

2. **For iOS Development:**
   - macOS with Xcode
   - CocoaPods: `sudo gem install cocoapods`

3. **For Android Development:**
   - Android Studio
   - Android SDK
   - Java JDK

## Installation Steps

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Build the web assets:**
   ```bash
   npm run build
   ```

3. **Add Capacitor platforms:**
   ```bash
   # For iOS
   npx cap add ios

   # For Android
   npx cap add android
   ```

4. **Sync Capacitor:**
   ```bash
   npm run sync
   ```

## Development

1. **Build and sync:**
   ```bash
   npm run build
   npm run sync
   ```

2. **Open in native IDE:**
   ```bash
   # iOS
   npm run open:ios

   # Android
   npm run open:android
   ```

## Building for Production

### iOS
1. Open Xcode: `npm run open:ios`
2. Select your target device
3. Product → Archive
4. Distribute via App Store or TestFlight

### Android
1. Open Android Studio: `npm run open:android`
2. Build → Generate Signed Bundle / APK
3. Follow the wizard to create your APK or AAB

## Project Structure

```
.
├── src/
│   └── index.html          # Main app file
├── www/                    # Built files (generated)
├── ios/                    # iOS native project (generated)
├── android/                # Android native project (generated)
├── package.json           # Dependencies
├── capacitor.config.json  # Capacitor configuration
└── README.md             # Documentation
```

## Capacitor Plugins Used

- **@capacitor/app** - App lifecycle and back button handling
- **@capacitor/filesystem** - File system operations for MIDI export
- **@capacitor/share** - Native sharing functionality

## Notes

- The app uses Web Audio API which works on both web and native platforms
- MIDI export uses Capacitor Filesystem on native platforms and download on web
- Touch events are already handled for mobile devices
- The app is responsive and works on tablets and phones















