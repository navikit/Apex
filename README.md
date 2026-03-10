# Pi Digits Viewer

A small standalone web page that computes digits of π in the browser using a Web Worker.

## How to run

### Option A (fastest, no server required)
1. Open `pi_digits/pi_digits.html` in your web browser.
2. Enter the number of digits you want to compute.
3. Click **Compute π digits** and watch the progress bar + ETA update in real time.

> ✅ Works in modern browsers (Chrome, Edge, Firefox, Safari). If you see errors due to `file://` restrictions, use Option B.

### Option B (recommended if you run into file:// limitations)
1. From a terminal, run a simple local server in the repository root, e.g.:  
   `python -m http.server 8000`
2. Open your browser and go to:  
   `http://localhost:8000/pi_digits/pi_digits.html`

## Notes
- This is *not* a cryptographically secure generator — it’s an educational/demonstration tool.
- Very large digit counts (tens of thousands+) may take a while depending on your CPU.
