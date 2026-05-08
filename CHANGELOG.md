# Changelog

All notable changes to Timelapse Recorder are documented here.

---

## [0.5] – 2026-05-08

### Initial release

**Camera sources**
- Webcam and iPhone via Continuity Camera (macOS Ventura+)
- GoPro Hero 8+ via WiFi using the Open GoPro HTTP API
- Instar IP cameras via RTSP (1080p and WQHD/4K model series)

**Recording**
- Configurable capture interval (1–600 seconds)
- Timestamped session folders – each recording gets its own subfolder
- Timestamped frame filenames to prevent overwrites
- Aspect ratio crop applied at capture time: Original, 16:9, 4:3, 1:1, 9:16

**Video assembly**
- One-click assembly from saved frames
- Output formats: MP4 (H.264), MOV (H.264), ProRes (macOS only)
- Configurable output FPS (6–60)

**UI**
- macOS dark mode design using CustomTkinter
- Live camera preview with crop guide overlay
- Info overlay during recording (frame count, elapsed time, folder size)
- Battery display for MacBook and iPhone (USB) in the toolbar
- macOS menu bar with keyboard shortcuts (⌘R, ⌘O, ⌘E, ⌘I, ⌘Q)
- Segmented control for camera source selection
- ↺ Rescan and ⏎ Switch Camera buttons for camera management

**Camera detection**
- AVFoundation-based camera enumeration via system Python + pyobjc
- Correct index mapping when Continuity Camera reorders devices
- Swift fallback if pyobjc is unavailable
- system_profiler as last resort

### Known limitations

- Camera switching with Continuity Camera requires disconnecting the iPhone first
- iPhone battery only readable via USB (not over WiFi / Continuity Camera)
- ProRes requires macOS; a clear error is shown if the codec is unavailable
