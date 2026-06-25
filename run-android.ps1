# Script to build and run the app on Android device via ADB

Write-Host "`n=== Building and Installing Android App ===" -ForegroundColor Cyan

# Set Android SDK path (adjust if needed)
$env:ANDROID_HOME = $env:LOCALAPPDATA + "\Android\Sdk"
$adbPath = "$env:ANDROID_HOME\platform-tools\adb.exe"

# Check if ADB exists
if (-not (Test-Path $adbPath)) {
    Write-Host "`n❌ ADB not found at: $adbPath" -ForegroundColor Red
    Write-Host "Please install Android SDK Platform Tools or set ANDROID_HOME environment variable." -ForegroundColor Yellow
    exit 1
}

# Check device connection
Write-Host "`n📱 Checking for connected devices..." -ForegroundColor Cyan
$devices = & $adbPath devices
Write-Host $devices

$unauthorized = $devices | Select-String "unauthorized"
if ($unauthorized) {
    Write-Host "`n⚠️  Device is unauthorized!" -ForegroundColor Yellow
    Write-Host "Please authorize USB debugging on your Android device:" -ForegroundColor Yellow
    Write-Host "1. On your device, tap 'Allow USB debugging' when prompted" -ForegroundColor White
    Write-Host "2. Check 'Always allow from this computer' if you want" -ForegroundColor White
    Write-Host "3. Tap 'OK'" -ForegroundColor White
    Write-Host "`nWaiting for authorization..." -ForegroundColor Cyan
    
    # Wait for device to be authorized
    $maxWait = 60
    $waited = 0
    while ($waited -lt $maxWait) {
        Start-Sleep -Seconds 2
        $waited += 2
        $devices = & $adbPath devices
        $authorized = $devices | Select-String "device$"
        if ($authorized) {
            Write-Host "✅ Device authorized!" -ForegroundColor Green
            break
        }
        Write-Host "." -NoNewline
    }
    Write-Host ""
}

# Build web assets
Write-Host "`n🔨 Building web assets..." -ForegroundColor Cyan
node copy-assets.js
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Build failed!" -ForegroundColor Red
    exit 1
}

# Sync Capacitor
Write-Host "`n🔄 Syncing Capacitor..." -ForegroundColor Cyan
npx cap sync android
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Sync failed!" -ForegroundColor Red
    exit 1
}

# Build and run
Write-Host "`n🚀 Building and installing app on device..." -ForegroundColor Cyan
Write-Host "This may take a few minutes on first build..." -ForegroundColor Yellow
npx cap run android

Write-Host "`n✅ Done! The app should now be running on your device." -ForegroundColor Green










