# 🎬 Timelapse Recorder

A macOS timelapse recording app built with Python and CustomTkinter.  
Supports the built-in webcam, iPhone via Continuity Camera, GoPro (WiFi), and Instar IP cameras.

![Platform](https://img.shields.io/badge/platform-macOS-lightgrey)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Version](https://img.shields.io/badge/version-0.5-green)
![License](https://img.shields.io/badge/license-MIT-brightgreen)

---

## Screenshots

> _Add screenshots here once available_

---

## Features

- **Live preview** of the selected camera source
- **Three camera sources:**
  - Webcam / iPhone via Continuity Camera (macOS Ventura+)
  - GoPro Hero 8+ via WiFi (Open GoPro HTTP API)
  - Instar IP cameras via RTSP (1080p and WQHD/4K models)
- **Aspect ratio crop** – Original, 16:9, 4:3, 1:1, 9:16 (portrait)
- **Info overlay** – live frame count, elapsed time, folder size, format and ratio
- **Output format** – MP4, MOV, or ProRes (macOS only)
- **Session folders** – each recording gets its own timestamped folder
- **Timestamped frame filenames** – no accidental overwrites
- **Battery display** – MacBook and iPhone (USB only) in the toolbar
- **macOS menu bar** with keyboard shortcuts (⌘R, ⌘O, ⌘E, ⌘I, ⌘Q)
- **Video assembly** – combine all saved frames into a video with one click

---

## Requirements

- macOS 12 Monterey or later (macOS 13 Ventura+ recommended for Continuity Camera)
- Python 3.10 or later
- Xcode Command Line Tools (for AVFoundation camera detection)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/timelapse-recorder.git
cd timelapse-recorder
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install opencv-python pillow requests psutil customtkinter
```

### 4. Run

```bash
python timelapse.py
```

Or create a double-click launcher:

```bash
cat > "Start Timelapse.command" << 'EOF'
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
python timelapse.py
EOF
chmod +x "Start Timelapse.command"
```

---

## Camera Setup

### Webcam / iPhone (Continuity Camera)

The app detects all available cameras at startup using AVFoundation and displays them by their real names (e.g. "FaceTime HD Camera" or "Simon's iPhone").

> **Note:** When Continuity Camera is active, macOS promotes the iPhone to camera index 0 and pushes the built-in FaceTime camera to index 1. The app accounts for this automatically. If a camera switch does not work as expected, disconnect Continuity Camera via iPhone Control Centre, then click **↺ Rescan**.

**First launch:** macOS will ask for camera permission. Click **Allow**, or go to **System Settings → Privacy & Security → Camera → Terminal**.

### GoPro (Hero 8 and newer)

1. Power on the GoPro
2. On the GoPro: **Connections → Connect Device → GoPro App** → enable WiFi
3. On your Mac: **System Settings → WiFi** → connect to the `GOPRO-XXXX` network
4. In the app: select **GoPro**, then click **Connect to GoPro**

> While connected to the GoPro WiFi hotspot the Mac has no internet access. Quit GoPro Quik before connecting as it blocks the API port.

### Instar IP Camera

1. Open the camera's web interface (enter its IP in a browser)
2. Go to **Network → RTSP** and make sure RTSP is enabled
3. In the app: select **Instar**, enter IP, port (default 554), username, password, and model series
4. Click **Connect to Instar**

Supported models:
| Series | RTSP path |
|---|---|
| 1080p (IN-6/7/8xxx) | `/{quality}` |
| WQHD/4K (IN-84/94xx) | `/livestream/{quality}` |

Quality levels: `11` = high, `12` = medium, `13` = low

---

## Usage

### Recording a timelapse

1. Select a camera source using the segmented control
2. Connect the camera if needed (GoPro / Instar)
3. Set the **interval** (seconds between frames) and **video FPS**
4. Choose an **aspect ratio** and **output format** if needed
5. Select an output folder (default: `~/Downloads/timelapse`)
6. Press **▶ Start Recording** or use **⌘R**
7. Press **⏹ Stop Recording** when done

### Assembling the video

After recording, click **🎞 Assemble Video** (or **⌘E**).  
The video is saved in the same session folder as the frames.

### Estimating recording duration and storage

| Duration | Interval | Frames | Video at 24 fps |
|---|---|---|---|
| 4 h | 10 s | 1 440 | ~60 s |
| 8 h | 10 s | 2 880 | ~2 min |
| 8 h | 5 s | 5 760 | ~4 min |

Storage at 1080p (~400 KB/frame): 8 h at 10 s ≈ **1.1 GB** for frames, ~**100 MB** for the final video.

---

## Keyboard Shortcuts

| Shortcut | Action |
|---|---|
| ⌘R | Start / stop recording |
| ⌘O | Open output folder in Finder |
| ⌘E | Assemble video |
| ⌘I | Toggle info overlay |
| ⌘Q | Quit |

---

## Output Structure

Each recording session creates a timestamped subfolder:

```
~/Downloads/timelapse/
└── session_20240508_143022/
    ├── frame_20240508_143025_000001.jpg
    ├── frame_20240508_143035_000002.jpg
    ├── frame_20240508_143045_000003.jpg
    └── timelapse_20240508_163022.mp4
```

---

## Configuration

All settings are at the top of `timelapse.py` – no code changes needed:

```python
DEFAULT_OUTPUT_DIR   = "~/Downloads/timelapse"
DEFAULT_INTERVAL     = 10.0      # seconds between frames
DEFAULT_FPS          = 24        # output video FPS
JPEG_QUALITY         = 92        # frame image quality (1–100)
DEFAULT_ASPECT_RATIO = "Original"
DEFAULT_FORMAT       = "MP4  –  H.264"

GOPRO_IP             = "10.5.5.9"
INSTAR_DEFAULT_IP    = "192.168.1.24"
```

---

## Known Limitations

- **Camera switching with Continuity Camera:** When the iPhone is connected via Continuity Camera, macOS holds an exclusive AVFoundation session for the iPhone. The built-in FaceTime camera may not be accessible until Continuity Camera is disconnected.
- **Lens selection removed:** iPhone lens switching via resolution hints was unreliable and has been removed in v0.5.
- **ProRes:** Only available on macOS. A fallback error is shown if the codec is unavailable.
- **iPhone battery:** Only readable when the iPhone is connected via USB. Shows `–` over WiFi/Continuity Camera.

---

## Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` | Camera capture, frame saving, video writing |
| `pillow` | Image processing, overlay rendering |
| `customtkinter` | Modern macOS-style UI |
| `requests` | GoPro HTTP API |
| `psutil` | MacBook battery level |

---

## License

MIT License – feel free to use, modify, and distribute.

---

## Acknowledgements

Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky.  
GoPro integration uses the [Open GoPro API](https://gopro.github.io/OpenGoPro/).
