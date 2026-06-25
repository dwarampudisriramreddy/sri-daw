const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const wwwDir = path.join(__dirname, 'www');

const mimeTypes = {
    '.html': 'text/html',
    '.js': 'text/javascript',
    '.css': 'text/css',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.gif': 'image/gif',
    '.svg': 'image/svg+xml',
    '.wav': 'audio/wav',
    '.mp4': 'video/mp4',
    '.woff': 'application/font-woff',
    '.ttf': 'application/font-ttf',
    '.eot': 'application/vnd.ms-fontobject',
    '.otf': 'application/font-otf',
    '.wasm': 'application/wasm',
    '.mid': 'audio/midi',
    '.midi': 'audio/midi',
    '.sf2': 'application/octet-stream'
};

// Set cache headers for offline support
const cacheHeaders = {
    '.js': { 'Cache-Control': 'public, max-age=31536000' }, // 1 year
    '.css': { 'Cache-Control': 'public, max-age=31536000' },
    '.html': { 'Cache-Control': 'no-cache' } // Always check for HTML updates
};

const server = http.createServer((req, res) => {
    console.log(`${req.method} ${req.url}`);

    // Parse URL
    let filePath = '.' + req.url;
    if (filePath === './') {
        filePath = './index.html';
    }

    const fullPath = path.join(wwwDir, filePath);
    const extname = String(path.extname(fullPath)).toLowerCase();
    const contentType = mimeTypes[extname] || 'application/octet-stream';

    fs.readFile(fullPath, (error, content) => {
        if (error) {
            if (error.code === 'ENOENT') {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.end('<h1>404 - File Not Found</h1>', 'utf-8');
            } else {
                res.writeHead(500);
                res.end(`Server Error: ${error.code}`, 'utf-8');
            }
            } else {
                const headers = { 'Content-Type': contentType };
                // Add cache headers if applicable
                if (cacheHeaders[extname]) {
                    Object.assign(headers, cacheHeaders[extname]);
                }
                res.writeHead(200, headers);
                res.end(content, 'utf-8');
            }
    });
});

server.listen(PORT, () => {
    console.log(`\n🚀 Server running at http://localhost:${PORT}/`);
    console.log(`📱 Open your browser and navigate to: http://localhost:${PORT}/\n`);
});

