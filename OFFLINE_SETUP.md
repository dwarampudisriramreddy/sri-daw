# Offline Setup Guide

## Current Status

The app currently loads SoundFont from a CDN, which requires internet connection. However, the app has a **fallback oscillator system** that works completely offline for basic playback.

## Making SoundFont Work Offline

### Option 1: Download SoundFont Library (Recommended)

Run this command to download the SoundFont library locally:

```bash
npm run download-soundfont
```

This will:
- Download `soundfont-player.min.js` to `www/js/`
- Enable offline use of the SoundFont library

**Note:** Instrument soundfont files (piano, guitar, etc.) are still downloaded from CDN on first use, but they are cached by your browser for offline access.

### Option 2: Full Offline Setup (Advanced)

For complete offline support including instrument files:

1. Download instrument soundfont files manually
2. Place them in `www/soundfonts/` directory
3. Update the `nameToUrl` function in the code to point to local files

## How It Works

1. **First Load (Online):**
   - SoundFont library loads from local file (if downloaded) or CDN
   - Instrument files download from CDN on first use
   - Browser caches everything

2. **Subsequent Loads (Offline):**
   - SoundFont library loads from local file
   - Instrument files load from browser cache
   - App works completely offline!

3. **Fallback:**
   - If SoundFont fails to load, the app uses oscillator-based synthesis
   - This works offline but sounds less realistic

## Testing Offline Mode

1. Run `npm run download-soundfont`
2. Load the app in your browser
3. Play some music (this downloads and caches instruments)
4. Disconnect from internet
5. Reload the app - it should work offline!

## Browser Cache

Modern browsers automatically cache the SoundFont instrument files. To ensure offline access:

- **Chrome/Edge:** Settings → Privacy → Clear browsing data → Cached images and files (keep this)
- **Firefox:** Settings → Privacy → Cached Web Content (keep enabled)

The app will work offline once instruments are cached!















