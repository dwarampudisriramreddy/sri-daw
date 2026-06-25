# Music Theory Pad - Capacitor App

A cross-platform music composition app built with Capacitor, featuring chord progressions, melody creation, and drum programming.

## Features

- 🎹 **Chord Progression Piano Roll** - Create and visualize chord progressions
- 🎵 **Melody Piano Roll** - Compose melodies with music theory guidance
- 🥁 **Drum Piano Roll** - Program drums with 9 different sounds
- 💾 **MIDI Export/Import** - Export and import MIDI files
- 🎼 **Music Theory Guidance** - Scale-aware note suggestions

## Prerequisites

- Node.js 16+ and npm
- For iOS: Xcode and CocoaPods
- For Android: Android Studio and Android SDK

## Installation

1. Install dependencies:
```bash
npm install
```

2. Sync Capacitor:
```bash
npm run sync
```

## Development

1. Build the app:
```bash
npm run build
```

2. Sync with native projects:
```bash
npm run sync
```

3. Open in your IDE:
```bash
# iOS
npm run open:ios

# Android
npm run open:android
```

## Building for Production

### iOS
1. Open Xcode:
```bash
npm run open:ios
```

2. In Xcode, select your target device/simulator
3. Click Run or press Cmd+R

### Android
1. Open Android Studio:
```bash
npm run open:android
```

2. In Android Studio, click Run or press Shift+F10

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
└── README.md             # This file
```

## Capacitor Plugins Used

- `@capacitor/app` - App lifecycle and back button handling
- `@capacitor/filesystem` - File system operations
- `@capacitor/share` - Native sharing functionality

## License

MIT















# sri-daw
