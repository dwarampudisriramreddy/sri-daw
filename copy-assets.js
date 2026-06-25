const fs = require('fs');
const path = require('path');

// Ensure www directory exists
const wwwDir = path.join(__dirname, 'www');
if (!fs.existsSync(wwwDir)) {
    fs.mkdirSync(wwwDir, { recursive: true });
}

// Copy index.html from src to www
const sourceHtml = path.join(__dirname, 'src', 'index.html');
const destHtml = path.join(wwwDir, 'index.html');

if (fs.existsSync(sourceHtml)) {
    fs.copyFileSync(sourceHtml, destHtml);
    console.log('✓ Copied index.html from src/ to www/');
} else {
    // Fallback: try copying from root
    const rootHtml = path.join(__dirname, 'hookpad-theory.html');
    if (fs.existsSync(rootHtml)) {
        fs.copyFileSync(rootHtml, destHtml);
        console.log('✓ Copied hookpad-theory.html to www/index.html');
    } else {
        console.log('⚠ index.html not found in src/ or root directory');
    }
}

// Copy js directory if it exists (for offline soundfont support)
const jsSourceDir = path.join(__dirname, 'www', 'js');
const jsDestDir = path.join(wwwDir, 'js');
if (fs.existsSync(jsSourceDir)) {
    if (!fs.existsSync(jsDestDir)) {
        fs.mkdirSync(jsDestDir, { recursive: true });
    }
    const files = fs.readdirSync(jsSourceDir);
    files.forEach(file => {
        const sourceFile = path.join(jsSourceDir, file);
        const destFile = path.join(jsDestDir, file);
        fs.copyFileSync(sourceFile, destFile);
    });
    console.log('✓ Copied soundfont library files');
}

// Copy js-synthesizer files from node_modules if they don't exist in www/js
const jsSynthesizerSource = path.join(__dirname, 'node_modules', 'js-synthesizer', 'dist');
if (fs.existsSync(jsSynthesizerSource)) {
    if (!fs.existsSync(jsDestDir)) {
        fs.mkdirSync(jsDestDir, { recursive: true });
    }
    const synthesizerFiles = ['js-synthesizer.min.js', 'js-synthesizer.worklet.min.js'];
    synthesizerFiles.forEach(file => {
        const sourceFile = path.join(jsSynthesizerSource, file);
        const destFile = path.join(jsDestDir, file);
        if (fs.existsSync(sourceFile)) {
            fs.copyFileSync(sourceFile, destFile);
            console.log(`✓ Copied ${file}`);
        }
    });
}

// Copy libfluidsynth files (required dependency for js-synthesizer)
const libfluidsynthSource = path.join(__dirname, 'node_modules', 'js-synthesizer', 'externals');
if (fs.existsSync(libfluidsynthSource)) {
    if (!fs.existsSync(jsDestDir)) {
        fs.mkdirSync(jsDestDir, { recursive: true });
    }
    const libfluidsynthFiles = ['libfluidsynth-2.4.6.js'];
    libfluidsynthFiles.forEach(file => {
        const sourceFile = path.join(libfluidsynthSource, file);
        const destFile = path.join(jsDestDir, file);
        if (fs.existsSync(sourceFile)) {
            fs.copyFileSync(sourceFile, destFile);
            console.log(`✓ Copied ${file}`);
        }
    });
}

console.log('✓ Build complete!');

