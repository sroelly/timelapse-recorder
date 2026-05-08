"""
╔══════════════════════════════════════════════════════════════════╗
║          TIMELAPSE RECORDER  –  Configuration                    ║
║  Adjust all settings at the top. Do not modify the code below.  ║
╚══════════════════════════════════════════════════════════════════╝

Dependencies:
    pip install opencv-python pillow requests psutil customtkinter
"""

# ══════════════════════════════════════════════════════════════════
#  GENERAL
# ══════════════════════════════════════════════════════════════════

# Application window title
APP_TITLE               = "Timelapse Recorder"

# Window dimensions in pixels
WINDOW_WIDTH            = 1080
WINDOW_HEIGHT           = 760

# Width of the right settings panel in pixels
PANEL_WIDTH             = 320

# Preview canvas dimensions in pixels
CANVAS_WIDTH            = 700
CANVAS_HEIGHT           = 490

# Default output folder for frames and video files
# Changed to Downloads so recordings are easy to find
DEFAULT_OUTPUT_DIR      = "~/Downloads/timelapse"

# Default capture interval between frames (seconds)
DEFAULT_INTERVAL        = 10.0
INTERVAL_MIN            = 1
INTERVAL_MAX            = 600

# Default frames-per-second for the assembled video
DEFAULT_FPS             = 24
FPS_MIN                 = 6
FPS_MAX                 = 60

# JPEG compression quality for saved frames (1–100, higher = better quality)
JPEG_QUALITY            = 92

# File naming
FRAME_PREFIX            = "frame_"
FRAME_TIMESTAMP_FMT     = "%Y%m%d_%H%M%S"
VIDEO_PREFIX            = "timelapse_"
VIDEO_TIMESTAMP_FMT     = "%Y%m%d_%H%M%S"
SESSION_FOLDER_PREFIX   = "session_"
SESSION_TIMESTAMP_FMT   = "%Y%m%d_%H%M%S"

# Seconds between preview frames (lower = smoother, higher CPU usage)
WEBCAM_PREVIEW_INTERVAL = 0.05
INSTAR_PREVIEW_INTERVAL = 0.08

# Number of frames to flush from RTSP buffer before grabbing (avoids stale frames)
INSTAR_BUFFER_FLUSH     = 2

# How often to refresh the battery display (seconds)
BATTERY_REFRESH         = 30

# Brief pause when stopping preview threads (seconds)
SHUTDOWN_WAIT           = 0.15

# Number of camera indices to probe during auto-detection at startup
CAMERA_PROBE_COUNT      = 6


# ══════════════════════════════════════════════════════════════════
#  ASPECT RATIO
# ══════════════════════════════════════════════════════════════════

# None = no crop, tuple = (width_ratio, height_ratio)
ASPECT_RATIO_OPTIONS = {
    "Original"  : None,
    "16 : 9"    : (16, 9),
    "4 : 3"     : (4,  3),
    "1 : 1"     : (1,  1),
    "9 : 16"    : (9,  16),   # portrait / iPhone vertical
}
DEFAULT_ASPECT_RATIO    = "Original"


# ══════════════════════════════════════════════════════════════════
#  OUTPUT FORMAT
# ══════════════════════════════════════════════════════════════════

# Format label → (fourcc code, file extension)
# ProRes requires macOS; a clear error is shown if unavailable.
OUTPUT_FORMATS = {
    "MP4  –  H.264"    : ("mp4v", ".mp4"),
    "MOV  –  H.264"    : ("mp4v", ".mov"),
    "ProRes  (macOS)"  : ("apcn", ".mov"),
}
DEFAULT_FORMAT          = "MP4  –  H.264"


# ══════════════════════════════════════════════════════════════════
#  OVERLAY
# ══════════════════════════════════════════════════════════════════

# Whether to show the info overlay on the preview by default
OVERLAY_SHOW_DEFAULT    = True

# Visual properties of the overlay text
OVERLAY_TEXT_COLOR      = "white"
OVERLAY_PADDING         = 8


# ══════════════════════════════════════════════════════════════════
#  WEBCAM / iPhone Continuity Camera
# ══════════════════════════════════════════════════════════════════

# Note: When an iPhone is nearby with Continuity Camera enabled, macOS
# promotes it to the default camera (index 0), pushing the built-in
# FaceTime camera to a higher index. The app enumerates all available
# cameras at startup with their real names so you can pick explicitly.

# iPhone lens selection: each lens is activated by requesting a specific
# resolution. Requires iOS 17+ and Continuity Camera (macOS Ventura+).
IPHONE_LENS_OPTIONS = {
    "Auto  (max. resolution)" : (3840, 2160),
    "Ultra Wide  (0.5×)"      : (1280,  720),
    "Main  (1×)"              : (1920, 1080),
    "2×  Zoom"                : (2560, 1440),
    "4K  /  Telephoto"        : (3840, 2160),
}
IPHONE_DEFAULT_LENS     = "Auto  (max. resolution)"


# ══════════════════════════════════════════════════════════════════
#  GOPRO  (Open GoPro HTTP API, Hero 8 and newer)
# ══════════════════════════════════════════════════════════════════

# GoPro's fixed IP address when acting as a WiFi hotspot
GOPRO_IP                = "10.5.5.9"
GOPRO_PORT              = 80

# Request timeouts in seconds
GOPRO_TIMEOUT_SHORT     = 3     # status checks and quick commands
GOPRO_TIMEOUT_LONG      = 5     # shutter and preset commands
GOPRO_TIMEOUT_DOWNLOAD  = 15    # file download

# Timing for the photo shutter sequence
GOPRO_SHUTTER_WAIT      = 1.5   # wait after triggering shutter (GoPro saves file)
GOPRO_SHUTTER_PULSE     = 0.3   # brief pause between shutter start and stop

# Preset ID for single photo mode (65537 = default single photo)
GOPRO_PHOTO_PRESET_ID   = 65537
GOPRO_PRESET_WAIT       = 0.5   # wait after loading preset

# Seconds subtracted from the interval to compensate for shutter + download time
GOPRO_INTERVAL_BUFFER   = 2


# ══════════════════════════════════════════════════════════════════
#  INSTAR IP CAMERA  (RTSP stream)
# ══════════════════════════════════════════════════════════════════

INSTAR_DEFAULT_IP       = "192.168.1.24"
INSTAR_DEFAULT_PORT     = "554"
INSTAR_DEFAULT_USER     = "admin"
INSTAR_DEFAULT_PASS     = "instar"

# Transport protocol: "tcp" (more reliable) or "udp" (lower latency)
INSTAR_RTSP_TRANSPORT   = "tcp"

# OpenCV capture buffer size (1 = always use the most recent frame)
INSTAR_BUFFER_SIZE      = 1

# RTSP path templates per model generation ({q} = quality number)
INSTAR_STREAM_PATHS = {
    "1080p  (IN-6/7/8xxx)"    : "/{q}",
    "WQHD / 4K  (IN-84/94xx)" : "/livestream/{q}",
}
INSTAR_DEFAULT_MODEL    = "WQHD / 4K  (IN-84/94xx)"

# Stream quality levels
INSTAR_QUALITY_OPTIONS = {
    "High  (11)"    : 11,
    "Medium  (12)"  : 12,
    "Low  (13)"     : 13,
}
INSTAR_DEFAULT_QUALITY  = "High  (11)"


# ══════════════════════════════════════════════════════════════════
#  COLORS  (macOS system palette)
# ══════════════════════════════════════════════════════════════════

COLOR_REC               = "#ff453a"   # System Red   – recording indicator
COLOR_GREEN             = "#30d158"   # System Green – start / success
COLOR_ORANGE            = "#ff9f0a"   # System Orange – GoPro
COLOR_BLUE              = "#0a84ff"   # System Blue  – Instar / assemble
COLOR_TEAL              = "#40c8e0"   # System Teal  – Switch Camera button
COLOR_MUTED             = "#636366"   # Secondary label color


# ══════════════════════════════════════════════════════════════════
#  CODE  –  do not modify below this line
# ══════════════════════════════════════════════════════════════════

import os

# Suppress OpenCV's verbose error messages (e.g. "camera failed to initialize").
# Must be set before importing cv2, otherwise it has no effect.
os.environ.setdefault("OPENCV_LOG_LEVEL", "SILENT")

import cv2
import json
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw
import threading
import time
import glob
import subprocess
import requests
import shutil
from datetime import datetime

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# ──────────────────────────────────────────────────────────────
#  Camera enumeration
# ──────────────────────────────────────────────────────────────

# ──────────────────────────────────────────────────────────────
#  Camera enumeration
# ──────────────────────────────────────────────────────────────

def get_avf_camera_names():
    """
    Query AVFoundation directly for the camera device list using the macOS
    system Python (/usr/bin/python3), which always has pyobjc available.

    This is the only reliable source of camera names **in the exact order
    that OpenCV assigns indices**, because OpenCV itself uses the same
    AVFoundation backend. system_profiler uses a different enumeration
    path and gets confused by Continuity Camera (it lists cameras in
    hardware order, while AVFoundation/OpenCV promote the iPhone to
    index 0 when Continuity Camera is active).

    Returns a list of camera names ordered by AVFoundation index (= OpenCV index).
    Returns an empty list on any error.
    """
    avf_script = (
        "import objc; "
        "from AVFoundation import AVCaptureDevice, AVMediaType; "
        "devices = AVCaptureDevice.devicesWithMediaType_("
        "    AVMediaType.AVMediaTypeVideo); "
        "[print(d.localizedName()) for d in devices]"
    )
    try:
        result = subprocess.run(
            ["/usr/bin/python3", "-c", avf_script],
            capture_output=True, text=True, timeout=6)
        if result.returncode == 0 and result.stdout.strip():
            return [l.strip()
                    for l in result.stdout.strip().splitlines()
                    if l.strip()]
    except Exception:
        pass
    return []


def get_avf_camera_names_swift():
    """
    Fallback: query AVFoundation via a temporary Swift script.
    Used when /usr/bin/python3 + pyobjc is unavailable.
    Requires Xcode Command Line Tools (xcrun swift).
    """
    import tempfile
    swift_code = """
import AVFoundation
let devices = AVCaptureDevice.devices(for: AVMediaType.video)
for d in devices { print(d.localizedName) }
"""
    try:
        with tempfile.NamedTemporaryFile(
                suffix=".swift", mode="w", delete=False) as f:
            f.write(swift_code)
            tmp = f.name
        result = subprocess.run(
            ["xcrun", "swift", tmp],
            capture_output=True, text=True, timeout=20)
        os.unlink(tmp)
        if result.returncode == 0 and result.stdout.strip():
            return [l.strip()
                    for l in result.stdout.strip().splitlines()
                    if l.strip()]
    except Exception:
        pass
    return []


def get_system_camera_names():
    """
    Last-resort fallback: query system_profiler for camera names.
    This does NOT reliably match OpenCV indices when Continuity Camera
    is active (the iPhone gets promoted to index 0 by AVFoundation but
    system_profiler keeps it at its hardware position).
    Only used when both AVFoundation methods fail.
    """
    try:
        result = subprocess.run(
            ["system_profiler", "SPCameraDataType", "-json"],
            capture_output=True, text=True, timeout=6)
        data = json.loads(result.stdout)
        return [cam.get("_name", "Camera")
                for cam in data.get("SPCameraDataType", [])]
    except Exception:
        return []


def enumerate_cameras():
    """
    Build the camera list with names and indices that correctly reflect
    the order OpenCV uses.

    Priority:
      1. AVFoundation via system Python + pyobjc  (fast, always correct)
      2. AVFoundation via Swift CLI               (slower, needs CLT)
      3. system_profiler                          (may be in wrong order
                                                   with Continuity Camera)
      4. Hardcoded fallback                       (non-macOS / no tools)

    Returns a dict:  {display_label: opencv_index}
    e.g. {"Simon's iPhone  –  [0]": 0, "FaceTime HD Camera  –  [1]": 1}
    """
    names = (get_avf_camera_names()
             or get_avf_camera_names_swift()
             or get_system_camera_names())

    if not names:
        return {"Default Camera  –  [0]": 0}

    return {f"{name}  –  [{idx}]": idx for idx, name in enumerate(names)}



# ──────────────────────────────────────────────────────────────
#  Battery helpers
# ──────────────────────────────────────────────────────────────

def get_mac_battery():
    """
    Return (percent: int, charging: bool) for the Mac battery via psutil.
    Returns (None, None) if psutil is unavailable or no battery found.
    """
    if not HAS_PSUTIL:
        return None, None
    try:
        b = psutil.sensors_battery()
        return (int(b.percent), b.power_plugged) if b else (None, None)
    except Exception:
        return None, None


def get_iphone_battery():
    """
    Attempt to read the iPhone battery level via ioreg (USB only).
    Continuity Camera over WiFi does not expose battery data to macOS –
    the display will show '–' in that case.
    Returns an int percentage or None.
    """
    try:
        out = subprocess.check_output(
            ["ioreg", "-r", "-c", "IOUSBDevice", "-a"],
            timeout=3, stderr=subprocess.DEVNULL
        ).decode("utf-8", errors="ignore")
        for line in out.splitlines():
            if "BatteryLevel" in line:
                return int(line.split("=")[-1].strip().strip(";"))
    except Exception:
        pass
    return None


def format_bytes(n):
    """Human-readable file size string."""
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.1f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def folder_size(path):
    """Total size of all files in a folder (non-recursive)."""
    total = 0
    try:
        for f in glob.glob(os.path.join(path, "*")):
            if os.path.isfile(f):
                total += os.path.getsize(f)
    except Exception:
        pass
    return total


# ──────────────────────────────────────────────────────────────
#  Frame crop helper
# ──────────────────────────────────────────────────────────────

def crop_frame(frame, ratio_key):
    """
    Crop a frame to the requested aspect ratio (centered).
    ratio_key must be a key from ASPECT_RATIO_OPTIONS.
    Returns the original frame unchanged if ratio is None.
    """
    ratio = ASPECT_RATIO_OPTIONS.get(ratio_key)
    if ratio is None:
        return frame
    h, w   = frame.shape[:2]
    rw, rh = ratio
    target = rw / rh
    current = w / h
    if abs(current - target) < 0.01:
        return frame
    if current > target:
        # Frame is too wide → crop left and right
        new_w = int(h * target)
        x     = (w - new_w) // 2
        return frame[:, x : x + new_w]
    else:
        # Frame is too tall → crop top and bottom
        new_h = int(w / target)
        y     = (h - new_h) // 2
        return frame[y : y + new_h, :]


# ──────────────────────────────────────────────────────────────
#  GoPro controller
# ──────────────────────────────────────────────────────────────

class GoPro:
    """Communicates with a GoPro Hero 8+ via the Open GoPro HTTP API over WiFi."""

    def __init__(self):
        self.connected = False
        base       = f"http://{GOPRO_IP}:{GOPRO_PORT}"
        self.BASE  = base
        self.MEDIA = f"{base}/gopro/media"
        self.CAM   = f"{base}/gopro/camera"

    def check_connection(self):
        """Ping the camera info endpoint. Sets self.connected."""
        try:
            r = requests.get(f"{self.CAM}/info", timeout=GOPRO_TIMEOUT_SHORT)
            self.connected = r.status_code == 200
        except Exception:
            self.connected = False
        return self.connected

    def get_info(self):
        """Return the camera info dict (model name etc.) or {}."""
        try:
            r = requests.get(f"{self.CAM}/info", timeout=GOPRO_TIMEOUT_SHORT)
            return r.json() if r.ok else {}
        except Exception:
            return {}

    def set_photo_mode(self):
        """Switch GoPro to single photo preset."""
        try:
            requests.get(
                f"{self.CAM}/presets/load?id={GOPRO_PHOTO_PRESET_ID}",
                timeout=GOPRO_TIMEOUT_LONG)
            time.sleep(GOPRO_PRESET_WAIT)
        except Exception:
            pass

    def take_photo(self):
        """Trigger the shutter and release it. Returns True on success."""
        try:
            r = requests.get(f"{self.CAM}/shutter/start",
                             timeout=GOPRO_TIMEOUT_LONG)
            time.sleep(GOPRO_SHUTTER_PULSE)
            requests.get(f"{self.CAM}/shutter/stop",
                         timeout=GOPRO_TIMEOUT_SHORT)
            return r.status_code == 200
        except Exception:
            return False

    def get_last_media(self):
        """Return (folder, filename) of the most recently saved file, or (None, None)."""
        try:
            r   = requests.get(f"{self.MEDIA}/list", timeout=GOPRO_TIMEOUT_LONG)
            med = r.json().get("media", [])
            if not med:
                return None, None
            return med[-1]["d"], med[-1]["fs"][-1]["n"]
        except Exception:
            return None, None

    def download_file(self, folder, filename, dest):
        """Download a file from the GoPro SD card to dest. Returns True on success."""
        url = f"{self.BASE}/videos/DCIM/{folder}/{filename}"
        try:
            with requests.get(url, stream=True, timeout=GOPRO_TIMEOUT_DOWNLOAD) as r:
                if r.ok:
                    with open(dest, "wb") as f:
                        shutil.copyfileobj(r.raw, f)
                    return True
        except Exception:
            pass
        return False


# ──────────────────────────────────────────────────────────────
#  Instar IP camera controller
# ──────────────────────────────────────────────────────────────

class InstarCamera:
    """Connects to an Instar IP camera via RTSP using OpenCV + FFmpeg backend."""

    def __init__(self):
        self.cap       = None
        self.connected = False
        self.url       = ""

    def build_url(self, ip, port, user, password, model_key, quality):
        """Assemble the RTSP URL from the connection parameters."""
        path     = INSTAR_STREAM_PATHS[model_key].format(q=quality)
        self.url = f"rtsp://{user}:{password}@{ip}:{port}{path}"
        return self.url

    def connect(self):
        """
        Open the RTSP stream and read one frame to verify connectivity.
        Sets self.connected and returns True on success.
        """
        if self.cap:
            self.cap.release()
        os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = (
            f"rtsp_transport;{INSTAR_RTSP_TRANSPORT}")
        self.cap = cv2.VideoCapture(self.url, cv2.CAP_FFMPEG)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, INSTAR_BUFFER_SIZE)
        ret, _         = self.cap.read()
        self.connected = ret
        return ret

    def read_frame(self):
        """
        Flush the RTSP buffer and return the latest frame as a numpy array,
        or None if the stream is unavailable.
        """
        if self.cap and self.cap.isOpened():
            for _ in range(INSTAR_BUFFER_FLUSH):
                self.cap.grab()
            ret, frame = self.cap.retrieve()
            return frame if ret else None
        return None

    def release(self):
        """Release the RTSP capture and reset connection state."""
        if self.cap:
            self.cap.release()
            self.cap = None
        self.connected = False


# ──────────────────────────────────────────────────────────────
#  Main application
# ──────────────────────────────────────────────────────────────

class TimelapseApp(ctk.CTk):
    """
    Main application window.
    Manages camera sources, the preview loop, frame capture, and
    video assembly. All UI is built with CustomTkinter for a
    native macOS dark-mode appearance.
    """

    def __init__(self):
        super().__init__()
        self.title(APP_TITLE)
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.resizable(False, False)

        # Capture state
        self.cap              = None      # OpenCV capture for webcam / iPhone
        self.recording        = False
        self.preview_running  = False
        self._preview_thread  = None      # tracked so we can join() before reopening
        self._camera_lock     = threading.Lock()  # prevents concurrent cap access
        self.frame_count      = 0
        self.output_dir       = ""
        self.start_time       = None

        # Camera controllers
        self.gopro  = GoPro()
        self.instar = InstarCamera()
        self.source = "webcam"           # "webcam" | "gopro" | "instar"

        # UI state variables (set before _build_ui)
        self.overlay_var = tk.BooleanVar(value=OVERLAY_SHOW_DEFAULT)
        self.aspect_var  = ctk.StringVar(value=DEFAULT_ASPECT_RATIO)
        self.format_var  = ctk.StringVar(value=DEFAULT_FORMAT)

        # Enumerate cameras before building the UI so the dropdown is populated
        self.available_cameras = {}   # label → index
        self._refresh_cameras(silent=True)

        self._build_menu()
        self._build_ui()
        self._start_webcam_preview()
        self._start_battery_loop()

    # ──────────────────────────────────────────────
    # Camera enumeration
    # ──────────────────────────────────────────────

    def _refresh_cameras(self, silent=False):
        """
        Re-probe available cameras and update the dropdown.
        silent=True suppresses the "no cameras found" warning (used at startup).
        """
        if not silent:
            self._canvas_msg("Scanning cameras …")
        self.available_cameras = enumerate_cameras()
        if hasattr(self, "cam_combo"):
            self.cam_combo.configure(values=list(self.available_cameras.keys()))
            self.cam_idx_var.set(list(self.available_cameras.keys())[0])

    # ──────────────────────────────────────────────
    # Menu bar
    # ──────────────────────────────────────────────

    def _build_menu(self):
        """Build the native macOS menu bar with keyboard shortcuts."""
        menubar = tk.Menu(self)

        # ── File ──────────────────────────────────
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(
            label="Start / Stop Recording",
            accelerator="⌘R",
            command=self._toggle_recording)
        file_menu.add_command(
            label="Open Output Folder",
            accelerator="⌘O",
            command=self._open_output_folder)
        file_menu.add_separator()
        file_menu.add_command(
            label="Assemble Video",
            accelerator="⌘E",
            command=self._assemble_video)
        file_menu.add_separator()
        file_menu.add_command(
            label="Quit",
            accelerator="⌘Q",
            command=self.on_close)
        menubar.add_cascade(label="File", menu=file_menu)

        # ── View ──────────────────────────────────
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_checkbutton(
            label="Show Info Overlay",
            accelerator="⌘I",
            variable=self.overlay_var,
            onvalue=True, offvalue=False)
        view_menu.add_separator()

        # Aspect ratio sub-menu
        self._aspect_menu_var = tk.StringVar(value=DEFAULT_ASPECT_RATIO)
        aspect_sub = tk.Menu(view_menu, tearoff=0)
        for key in ASPECT_RATIO_OPTIONS:
            aspect_sub.add_radiobutton(
                label=key,
                variable=self._aspect_menu_var,
                value=key,
                command=lambda k=key: self._set_aspect(k))
        view_menu.add_cascade(label="Aspect Ratio", menu=aspect_sub)

        # Output format sub-menu
        self._format_menu_var = tk.StringVar(value=DEFAULT_FORMAT)
        format_sub = tk.Menu(view_menu, tearoff=0)
        for key in OUTPUT_FORMATS:
            format_sub.add_radiobutton(
                label=key,
                variable=self._format_menu_var,
                value=key,
                command=lambda k=key: self._set_format(k))
        view_menu.add_cascade(label="Output Format", menu=format_sub)
        menubar.add_cascade(label="View", menu=view_menu)

        # ── Help ──────────────────────────────────
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(
            label="Keyboard Shortcuts …",
            command=self._show_shortcuts)
        menubar.add_cascade(label="Help", menu=help_menu)

        self.configure(menu=menubar)

        # Bind keyboard shortcuts
        self.bind("<Command-r>", lambda e: self._toggle_recording())
        self.bind("<Command-o>", lambda e: self._open_output_folder())
        self.bind("<Command-e>", lambda e: self._assemble_video())
        self.bind("<Command-i>", lambda e: self.overlay_var.set(
            not self.overlay_var.get()))
        self.bind("<Command-q>", lambda e: self.on_close())

    def _set_aspect(self, key):
        """Sync aspect ratio between menu and panel dropdown."""
        self.aspect_var.set(key)
        self._aspect_menu_var.set(key)
        if hasattr(self, "aspect_combo"):
            self.aspect_combo.set(key)

    def _set_format(self, key):
        """Sync output format between menu and panel dropdown."""
        self.format_var.set(key)
        self._format_menu_var.set(key)
        if hasattr(self, "format_combo"):
            self.format_combo.set(key)

    def _show_shortcuts(self):
        messagebox.showinfo("Keyboard Shortcuts", (
            "⌘R   Start / stop recording\n"
            "⌘O   Open output folder in Finder\n"
            "⌘E   Assemble video from frames\n"
            "⌘I   Toggle info overlay\n"
            "⌘Q   Quit"
        ))

    def _open_output_folder(self):
        """Open the current session folder (or base folder) in Finder."""
        path = self.output_dir if self.output_dir else \
               os.path.expanduser(self.dir_var.get())
        if os.path.isdir(path):
            subprocess.run(["open", path])
        else:
            messagebox.showwarning("Folder not found",
                f"The folder does not exist yet:\n{path}")

    # ──────────────────────────────────────────────
    # UI layout
    # ──────────────────────────────────────────────

    def _build_ui(self):
        """Construct the full application UI using CustomTkinter widgets."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)   # toolbar
        self.grid_rowconfigure(1, weight=1)   # main content

        # ── Toolbar ─────────────────────────────────
        toolbar = ctk.CTkFrame(self, height=52, corner_radius=0,
                               fg_color=("#e8e8ed", "#1c1c1e"))
        toolbar.grid(row=0, column=0, columnspan=2, sticky="ew")
        toolbar.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(toolbar, text=APP_TITLE,
                     font=ctk.CTkFont(size=18, weight="bold")).grid(
                         row=0, column=0, padx=18, pady=14, sticky="w")

        # Battery indicators (top-right)
        batt_frame = ctk.CTkFrame(toolbar, fg_color="transparent")
        batt_frame.grid(row=0, column=2, padx=16, sticky="e")
        self.mac_batt_var    = ctk.StringVar(value="🔋 –")
        self.iphone_batt_var = ctk.StringVar(value="📱 –")
        ctk.CTkLabel(batt_frame, textvariable=self.mac_batt_var,
                     font=ctk.CTkFont(size=12),
                     text_color=COLOR_MUTED).pack(side="left", padx=(0, 12))
        ctk.CTkLabel(batt_frame, textvariable=self.iphone_batt_var,
                     font=ctk.CTkFont(size=12),
                     text_color=COLOR_MUTED).pack(side="left")

        # ── Preview area ────────────────────────────
        preview_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="black")
        preview_frame.grid(row=1, column=0, sticky="nsew")

        self.canvas = tk.Canvas(preview_frame, bg="black",
                                highlightthickness=0,
                                width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack(expand=True)
        self._canvas_msg("Initializing camera …")

        # Status bar below the preview
        status_bar = ctk.CTkFrame(preview_frame, height=36, corner_radius=0,
                                  fg_color=("#d1d1d6", "#2c2c2e"))
        status_bar.pack(fill="x", side="bottom")
        status_bar.pack_propagate(False)

        self.rec_dot = ctk.CTkLabel(status_bar, text="●",
                                    font=ctk.CTkFont(size=13),
                                    text_color=COLOR_MUTED)
        self.rec_dot.pack(side="left", padx=(10, 4))

        self.status_var = ctk.StringVar(value="Ready")
        ctk.CTkLabel(status_bar, textvariable=self.status_var,
                     font=ctk.CTkFont(size=13)).pack(side="left")

        self.counter_var = ctk.StringVar(value="")
        ctk.CTkLabel(status_bar, textvariable=self.counter_var,
                     font=ctk.CTkFont(size=13),
                     text_color=COLOR_MUTED).pack(side="left", padx=10)

        self.elapsed_var = ctk.StringVar(value="")
        ctk.CTkLabel(status_bar, textvariable=self.elapsed_var,
                     font=ctk.CTkFont(size=13, family="Menlo"),
                     text_color=COLOR_MUTED).pack(side="right", padx=12)

        # ── Settings panel (scrollable) ─────────────
        panel = ctk.CTkScrollableFrame(self, width=PANEL_WIDTH,
                                       corner_radius=0,
                                       fg_color=("#f2f2f7", "#1c1c1e"))
        panel.grid(row=1, column=1, sticky="nsew")

        # ── Panel helper closures ────────────────────

        def section_label(text):
            ctk.CTkLabel(panel, text=text,
                         font=ctk.CTkFont(size=11, weight="bold"),
                         text_color=COLOR_MUTED,
                         anchor="w").pack(fill="x", padx=16, pady=(14, 2))

        def separator():
            ctk.CTkFrame(panel, height=1,
                         fg_color=("#c6c6c8", "#38383a"),
                         corner_radius=0).pack(fill="x")

        def card():
            f = ctk.CTkFrame(panel, corner_radius=10,
                             fg_color=("#ffffff", "#2c2c2e"))
            f.pack(fill="x", padx=12, pady=(4, 0))
            return f

        def row(parent, label, widget_fn, pady=(8, 0)):
            """One label + widget row inside a card."""
            r = ctk.CTkFrame(parent, fg_color="transparent")
            r.pack(fill="x", padx=12, pady=pady)
            r.grid_columnconfigure(1, weight=1)
            ctk.CTkLabel(r, text=label,
                         font=ctk.CTkFont(size=12),
                         text_color=("#3c3c43", "#ebebf5"),
                         anchor="w", width=110).grid(row=0, column=0, sticky="w")
            widget_fn(r).grid(row=0, column=1, sticky="ew", padx=(8, 0))

        def combo(parent, var, values):
            return ctk.CTkComboBox(parent, variable=var, values=values,
                                   state="readonly",
                                   font=ctk.CTkFont(size=12),
                                   dropdown_font=ctk.CTkFont(size=12),
                                   height=30)

        def entry_field(parent, var, show=None):
            return ctk.CTkEntry(parent, textvariable=var,
                                font=ctk.CTkFont(size=12),
                                height=30, show=show or "")

        def spin_row(parent, label, var, lo, hi):
            """− value + stepper row (replaces the non-native Spinbox)."""
            r = ctk.CTkFrame(parent, fg_color="transparent")
            r.pack(fill="x", padx=12, pady=(8, 0))
            r.grid_columnconfigure(1, weight=1)
            ctk.CTkLabel(r, text=label,
                         font=ctk.CTkFont(size=12),
                         text_color=("#3c3c43", "#ebebf5"),
                         anchor="w", width=110).grid(row=0, column=0, sticky="w")
            sf = ctk.CTkFrame(r, fg_color="transparent")
            sf.grid(row=0, column=1, sticky="e")
            ctk.CTkButton(sf, text="−", width=28, height=28,
                          font=ctk.CTkFont(size=16),
                          command=lambda: self._spin(var, -1, lo, hi)).pack(side="left")
            ctk.CTkLabel(sf, textvariable=var,
                         font=ctk.CTkFont(size=13, weight="bold"),
                         width=52, anchor="center").pack(side="left", padx=2)
            ctk.CTkButton(sf, text="+", width=28, height=28,
                          font=ctk.CTkFont(size=16),
                          command=lambda: self._spin(var, +1, lo, hi)).pack(side="left")

        # ══ CAMERA ════════════════════════════════
        section_label("CAMERA")
        separator()
        cam_card = card()

        # Segmented source selector
        self.source_seg = ctk.CTkSegmentedButton(
            cam_card,
            values=["Webcam / iPhone", "GoPro", "Instar"],
            command=self._on_source_seg,
            font=ctk.CTkFont(size=12),
            height=32)
        self.source_seg.set("Webcam / iPhone")
        self.source_seg.pack(fill="x", padx=12, pady=(12, 8))

        # ── Webcam sub-panel ──
        self.pnl_webcam = ctk.CTkFrame(cam_card, fg_color="transparent")
        self.pnl_webcam.pack(fill="x")

        self.cam_idx_var = ctk.StringVar(
            value=list(self.available_cameras.keys())[0]
            if self.available_cameras else "No cameras found")

        def make_cam_combo(parent):
            self.cam_combo = ctk.CTkComboBox(
                parent, variable=self.cam_idx_var,
                values=list(self.available_cameras.keys()),
                state="readonly",
                font=ctk.CTkFont(size=12),
                dropdown_font=ctk.CTkFont(size=12),
                height=30,
                command=lambda _: self._on_camera_selected())
            return self.cam_combo

        row(self.pnl_webcam, "Device", make_cam_combo)

        # Buttons row: Switch + Rescan
        btn_row = ctk.CTkFrame(self.pnl_webcam, fg_color="transparent")
        btn_row.pack(fill="x", padx=12, pady=(6, 0))

        self.btn_switch_cam = ctk.CTkButton(
            btn_row, text="⏎  Switch Camera",
            height=30, font=ctk.CTkFont(size=12),
            fg_color=COLOR_TEAL, hover_color="#30a8c0",
            command=self._on_camera_selected)
        self.btn_switch_cam.pack(side="left", fill="x", expand=True, padx=(0, 4))

        ctk.CTkButton(
            btn_row, text="↺  Rescan",
            height=30, font=ctk.CTkFont(size=12),
            fg_color=("gray80", "gray30"),
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray40"),
            command=self._on_rescan_cameras).pack(side="left")

        # Note about Continuity Camera
        ctk.CTkLabel(self.pnl_webcam,
                     text="ⓘ  If iPhone shows up instead of the built-in camera:\n"
                          "disconnect Continuity Camera via iPhone Control Centre,\n"
                          "then click ↺ Rescan.",
                     font=ctk.CTkFont(size=10), text_color=COLOR_MUTED,
                     wraplength=PANEL_WIDTH - 40,
                     justify="left").pack(anchor="w", padx=12, pady=(6, 10))

        # ── GoPro sub-panel ──
        self.pnl_gopro = ctk.CTkFrame(cam_card, fg_color="transparent")
        ctk.CTkLabel(self.pnl_gopro,
                     text=f"Connects to {GOPRO_IP} via WiFi hotspot",
                     font=ctk.CTkFont(size=11),
                     text_color=COLOR_MUTED).pack(anchor="w", padx=12, pady=(6, 2))
        self.gopro_status_lbl = ctk.CTkLabel(
            self.pnl_gopro, text="Not connected",
            font=ctk.CTkFont(size=11), text_color=COLOR_MUTED)
        self.gopro_status_lbl.pack(anchor="w", padx=12)
        self.btn_gopro = ctk.CTkButton(
            self.pnl_gopro, text="Connect to GoPro",
            height=34, font=ctk.CTkFont(size=13),
            fg_color=COLOR_ORANGE, hover_color="#e08c00",
            command=self._connect_gopro)
        self.btn_gopro.pack(fill="x", padx=12, pady=(8, 12))

        # ── Instar sub-panel ──
        self.pnl_instar = ctk.CTkFrame(cam_card, fg_color="transparent")
        self.instar_ip_var      = ctk.StringVar(value=INSTAR_DEFAULT_IP)
        self.instar_port_var    = ctk.StringVar(value=INSTAR_DEFAULT_PORT)
        self.instar_user_var    = ctk.StringVar(value=INSTAR_DEFAULT_USER)
        self.instar_pass_var    = ctk.StringVar(value=INSTAR_DEFAULT_PASS)
        self.instar_model_var   = ctk.StringVar(value=INSTAR_DEFAULT_MODEL)
        self.instar_quality_var = ctk.StringVar(value=INSTAR_DEFAULT_QUALITY)
        row(self.pnl_instar, "IP Address", lambda p: entry_field(p, self.instar_ip_var))
        row(self.pnl_instar, "Port",       lambda p: entry_field(p, self.instar_port_var))
        row(self.pnl_instar, "Username",   lambda p: entry_field(p, self.instar_user_var))
        row(self.pnl_instar, "Password",   lambda p: entry_field(p, self.instar_pass_var, show="●"))
        row(self.pnl_instar, "Model",      lambda p: combo(p, self.instar_model_var, list(INSTAR_STREAM_PATHS.keys())))
        row(self.pnl_instar, "Quality",    lambda p: combo(p, self.instar_quality_var, list(INSTAR_QUALITY_OPTIONS.keys())))
        self.instar_status_lbl = ctk.CTkLabel(
            self.pnl_instar, text="Not connected",
            font=ctk.CTkFont(size=11), text_color=COLOR_MUTED)
        self.instar_status_lbl.pack(anchor="w", padx=12, pady=(6, 0))
        self.btn_instar = ctk.CTkButton(
            self.pnl_instar, text="Connect to Instar",
            height=34, font=ctk.CTkFont(size=13),
            fg_color=COLOR_BLUE, hover_color="#0070e0",
            command=self._connect_instar)
        self.btn_instar.pack(fill="x", padx=12, pady=(6, 12))

        # ══ RECORDING ═════════════════════════════
        section_label("RECORDING")
        separator()
        rec_card = card()
        self.interval_var = ctk.StringVar(value=str(int(DEFAULT_INTERVAL)))
        self.fps_var      = ctk.StringVar(value=str(DEFAULT_FPS))
        spin_row(rec_card, "Interval  (s)", self.interval_var, INTERVAL_MIN, INTERVAL_MAX)
        spin_row(rec_card, "Video FPS",     self.fps_var,      FPS_MIN,      FPS_MAX)
        ctk.CTkFrame(rec_card, height=8, fg_color="transparent").pack()

        # ══ IMAGE ═════════════════════════════════
        section_label("IMAGE")
        separator()
        img_card = card()

        def make_aspect_combo(parent):
            self.aspect_combo = ctk.CTkComboBox(
                parent, variable=self.aspect_var,
                values=list(ASPECT_RATIO_OPTIONS.keys()),
                state="readonly",
                font=ctk.CTkFont(size=12),
                dropdown_font=ctk.CTkFont(size=12),
                height=30,
                command=lambda v: self._set_aspect(v))
            return self.aspect_combo

        def make_format_combo(parent):
            self.format_combo = ctk.CTkComboBox(
                parent, variable=self.format_var,
                values=list(OUTPUT_FORMATS.keys()),
                state="readonly",
                font=ctk.CTkFont(size=12),
                dropdown_font=ctk.CTkFont(size=12),
                height=30,
                command=lambda v: self._set_format(v))
            return self.format_combo

        row(img_card, "Aspect Ratio",   make_aspect_combo, pady=(8, 0))
        row(img_card, "Output Format",  make_format_combo, pady=(8, 0))

        # Info overlay toggle
        ov_row = ctk.CTkFrame(img_card, fg_color="transparent")
        ov_row.pack(fill="x", padx=12, pady=(8, 10))
        ctk.CTkLabel(ov_row, text="Info Overlay",
                     font=ctk.CTkFont(size=12),
                     text_color=("#3c3c43", "#ebebf5"),
                     anchor="w", width=110).pack(side="left")
        ctk.CTkSwitch(ov_row, text="", variable=self.overlay_var,
                      onvalue=True, offvalue=False,
                      width=44, height=22).pack(side="left", padx=(8, 0))

        # ══ OUTPUT ════════════════════════════════
        section_label("OUTPUT")
        separator()
        out_card = card()
        self.dir_var = ctk.StringVar(value=os.path.expanduser(DEFAULT_OUTPUT_DIR))
        ctk.CTkEntry(out_card, textvariable=self.dir_var,
                     font=ctk.CTkFont(size=11),
                     height=30).pack(fill="x", padx=12, pady=(10, 6))
        ctk.CTkButton(out_card, text="Choose Folder …",
                      height=30, font=ctk.CTkFont(size=12),
                      fg_color=("gray80", "gray30"),
                      text_color=("gray10", "gray90"),
                      hover_color=("gray70", "gray40"),
                      command=self._choose_dir).pack(
                          fill="x", padx=12, pady=(0, 10))

        # ══ ACTIONS ═══════════════════════════════
        section_label("RECORDING")
        separator()
        act_card = card()
        self.btn_start = ctk.CTkButton(
            act_card, text="▶   Start Recording",
            height=44, font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COLOR_GREEN, hover_color="#28b84e",
            text_color="white", command=self._toggle_recording)
        self.btn_start.pack(fill="x", padx=12, pady=(12, 6))
        ctk.CTkButton(act_card, text="🎞   Assemble Video",
                      height=36, font=ctk.CTkFont(size=13),
                      fg_color=COLOR_BLUE, hover_color="#0070e0",
                      command=self._assemble_video).pack(
                          fill="x", padx=12, pady=(0, 12))

        ctk.CTkFrame(panel, height=20, fg_color="transparent").pack()

    # ──────────────────────────────────────────────
    # Spin stepper helper
    # ──────────────────────────────────────────────

    def _spin(self, var, delta, lo, hi):
        """Increment or decrement a StringVar within [lo, hi]."""
        try:
            val = float(var.get()) + delta
            val = max(lo, min(hi, val))
            var.set(str(int(val)) if val == int(val) else str(val))
        except ValueError:
            var.set(str(lo))

    # ──────────────────────────────────────────────
    # Canvas and overlay rendering
    # ──────────────────────────────────────────────

    def _canvas_msg(self, text, color=None):
        """Display a centered text message on the preview canvas."""
        self.canvas.delete("all")
        self.canvas.create_text(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
            text=text, fill=color or "#636366",
            font=("Helvetica Neue", 14),
            width=CANVAS_WIDTH - 60, justify="center")

    def _push_frame(self, frame):
        """
        Convert a raw OpenCV frame to a PhotoImage and send it to the canvas.
        Draws crop guide lines and – during recording – the info overlay.
        """
        display = frame.copy()

        # Draw crop guide lines and darken the outside area
        ratio_key = self.aspect_var.get()
        ratio     = ASPECT_RATIO_OPTIONS.get(ratio_key)
        if ratio is not None:
            fh, fw = display.shape[:2]
            rw, rh = ratio
            target  = rw / rh
            current = fw / fh
            if current > target:
                new_w = int(fh * target)
                x1    = (fw - new_w) // 2
                x2    = fw - x1
                display[:, :x1]  = (display[:, :x1]  * 0.35).astype("uint8")
                display[:, x2:]  = (display[:, x2:]  * 0.35).astype("uint8")
                cv2.line(display, (x1, 0), (x1, fh), (255, 255, 255), 1)
                cv2.line(display, (x2, 0), (x2, fh), (255, 255, 255), 1)
            else:
                new_h = int(fw / target)
                y1    = (fh - new_h) // 2
                y2    = fh - y1
                display[:y1, :]  = (display[:y1, :]  * 0.35).astype("uint8")
                display[y2:, :]  = (display[y2:, :]  * 0.35).astype("uint8")
                cv2.line(display, (0, y1), (fw, y1), (255, 255, 255), 1)
                cv2.line(display, (0, y2), (fw, y2), (255, 255, 255), 1)

        img = Image.fromarray(cv2.cvtColor(display, cv2.COLOR_BGR2RGB))
        img.thumbnail((CANVAS_WIDTH, CANVAS_HEIGHT))
        pw, ph = img.size

        # Overlay: drawn on the PIL image so it scales with the preview
        if self.overlay_var.get() and self.recording:
            draw    = ImageDraw.Draw(img)
            elapsed = int(time.time() - self.start_time) if self.start_time else 0
            h, r    = divmod(elapsed, 3600)
            m, s    = divmod(r, 60)
            size_str = format_bytes(folder_size(self.output_dir)) \
                       if self.output_dir else "–"
            lines = [
                f"● REC   {h:02d}:{m:02d}:{s:02d}",
                f"Frames:  {self.frame_count}",
                f"Size:    {size_str}",
                f"Format:  {self.format_var.get().split('–')[0].strip()}",
                f"Ratio:   {self.aspect_var.get()}",
            ]
            text = "\n".join(lines)
            pad  = OVERLAY_PADDING
            bbox = draw.textbbox((0, 0), text, font=None)
            tw   = bbox[2] - bbox[0]
            th   = bbox[3] - bbox[1]
            x0   = pad
            y0   = ph - th - pad * 3
            draw.rectangle(
                [x0 - pad, y0 - pad, x0 + tw + pad, y0 + th + pad],
                fill=(0, 0, 0, 180))
            draw.text((x0, y0), text, fill=OVERLAY_TEXT_COLOR)

        photo = ImageTk.PhotoImage(img)
        self.canvas.after(0, self._update_canvas, photo)

    def _update_canvas(self, photo):
        self.canvas.image = photo
        self.canvas.create_image(
            CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, image=photo)

    # ──────────────────────────────────────────────
    # Camera source switching
    # ──────────────────────────────────────────────

    def _on_source_seg(self, value):
        """Handle segmented button tap to switch the active camera source."""
        mapping = {"Webcam / iPhone": "webcam",
                   "GoPro": "gopro", "Instar": "instar"}
        self._stop_preview()
        self.pnl_webcam.pack_forget()
        self.pnl_gopro.pack_forget()
        self.pnl_instar.pack_forget()
        self.source = mapping[value]
        if self.source == "webcam":
            self.pnl_webcam.pack(fill="x")
            self._start_webcam_preview()
        elif self.source == "gopro":
            self.pnl_gopro.pack(fill="x")
            self._canvas_msg(
                "Connect Mac to GoPro WiFi hotspot,\nthen click 'Connect to GoPro'.")
        elif self.source == "instar":
            self.pnl_instar.pack(fill="x")
            self._canvas_msg(
                "Enter credentials,\nthen click 'Connect to Instar'.")

    def _stop_preview(self):
        """
        Signal the preview thread to stop and wait for it to finish
        before releasing the capture.

        cap.read() on macOS/AVFoundation can block for up to ~2 seconds
        waiting for the next camera frame. If we release the capture while
        a thread is blocked inside read(), AVFoundation's internal state
        gets corrupted, causing the SIGTRAP / pointer-authentication crash
        seen in the crash report (Thread 13, cameraQueue).

        Solution: set the flag, join() with a generous timeout, then release.
        """
        self.preview_running = False

        if self._preview_thread and self._preview_thread.is_alive():
            # Give the thread up to 3 s to exit its current cap.read() call
            self._preview_thread.join(timeout=3.0)
        self._preview_thread = None

        # Now safe to release – no thread is touching the capture
        with self._camera_lock:
            if self.cap:
                self.cap.release()
                self.cap = None

        if self.instar.cap:
            self.instar.release()

        # Small buffer for AVFoundation to fully relinquish the device
        time.sleep(0.3)

    # ──────────────────────────────────────────────
    # Webcam / iPhone
    # ──────────────────────────────────────────────

    def _on_camera_selected(self):
        """
        Called when the user picks a different camera from the dropdown
        or clicks 'Switch Camera'. Runs the stop/restart sequence in a
        background thread so the UI stays responsive during the ~3 s join.
        """
        self.btn_switch_cam.configure(state="disabled", text="Switching …")
        self.status_var.set("Switching camera …")

        def do_switch():
            self._stop_preview()
            self.after(0, self._start_webcam_preview)
            self.after(0, lambda: self.btn_switch_cam.configure(
                state="normal", text="⏎  Switch Camera"))

        threading.Thread(target=do_switch, daemon=True).start()

    def _on_rescan_cameras(self):
        """Re-enumerate cameras and restart the preview with the first result."""
        self.status_var.set("Scanning …")

        def do_rescan():
            self._stop_preview()
            self.available_cameras = enumerate_cameras()
            self.after(0, self._finish_rescan)

        threading.Thread(target=do_rescan, daemon=True).start()

    def _finish_rescan(self):
        """Update the dropdown after a rescan and restart preview."""
        labels = list(self.available_cameras.keys())
        self.cam_combo.configure(values=labels)
        self.cam_idx_var.set(labels[0] if labels else "No cameras found")
        self._start_webcam_preview()
        self.status_var.set("Ready")

    def _start_webcam_preview(self):
        """Open the selected camera index and start the preview loop."""
        label = self.cam_idx_var.get()
        idx   = self.available_cameras.get(label, 0)
        with self._camera_lock:
            if self.cap:
                self.cap.release()
            self.cap = cv2.VideoCapture(idx)
            if not self.cap.isOpened():
                self.cap = None
                self._canvas_msg(f"Camera [{idx}] not available", "#ff453a")
                return
        self.preview_running  = True
        self._preview_thread  = threading.Thread(
            target=self._webcam_preview_loop, daemon=True)
        self._preview_thread.start()

    def _webcam_preview_loop(self):
        """
        Continuously read frames from the webcam and push them to the canvas.
        Uses _camera_lock so that cap.read() and cap.release() never run
        concurrently (which caused the AVFoundation SIGTRAP crash).
        """
        consecutive_failures = 0
        while self.preview_running:
            frame = None
            with self._camera_lock:
                if self.cap and self.cap.isOpened():
                    ret, frame = self.cap.read()
                    if not ret:
                        frame = None
            if frame is not None:
                consecutive_failures = 0
                self._push_frame(frame)
            else:
                consecutive_failures += 1
                if consecutive_failures >= 5:
                    self.preview_running = False
                    self.after(0, self._on_camera_lost)
                    return
            time.sleep(WEBCAM_PREVIEW_INTERVAL)

    def _on_camera_lost(self):
        """
        Called on the main thread when the preview loop detects that the
        camera has stopped delivering frames (e.g. iPhone disconnected).
        """
        with self._camera_lock:
            if self.cap:
                self.cap.release()
                self.cap = None
        self._preview_thread = None
        self.status_var.set("Camera disconnected")
        self._canvas_msg(
            "Camera disconnected.\n\nClick  ↺ Rescan Cameras  to reconnect\n"
            "or select a different device.",
            color="#ff9f0a")
        if self.recording:
            self._stop_recording()

    # ──────────────────────────────────────────────
    # ──────────────────────────────────────────────

    def _connect_instar(self):
        """Start the Instar RTSP connection attempt in a background thread."""
        self.instar_status_lbl.configure(text="Connecting …")
        self.btn_instar.configure(state="disabled")
        quality = INSTAR_QUALITY_OPTIONS[self.instar_quality_var.get()]
        url = self.instar.build_url(
            self.instar_ip_var.get().strip(),
            self.instar_port_var.get().strip(),
            self.instar_user_var.get().strip(),
            self.instar_pass_var.get(),
            self.instar_model_var.get(), quality)

        def try_connect():
            ok = self.instar.connect()
            self.after(0, self._instar_ok if ok else self._instar_fail, url)

        threading.Thread(target=try_connect, daemon=True).start()

    def _instar_ok(self, url):
        self.instar_status_lbl.configure(text="✓  Connected",
                                         text_color=COLOR_GREEN)
        self.btn_instar.configure(fg_color=COLOR_GREEN, hover_color="#28b84e",
                                  text="✓  Connected", state="normal")
        self.status_var.set("Instar ready")
        self.preview_running = True
        threading.Thread(target=self._instar_preview_loop, daemon=True).start()

    def _instar_fail(self, url):
        self.instar_status_lbl.configure(text="Connection failed",
                                         text_color="#ff453a")
        self.btn_instar.configure(state="normal")
        messagebox.showerror("Instar: Connection failed",
            f"Could not open RTSP stream:\n{url}\n\n"
            "Check:\n"
            "• IP address correct?\n"
            "• Username / password correct?\n"
            "• Correct model selected (1080p vs WQHD/4K)?\n"
            "• Mac and camera on the same network?\n"
            "• RTSP enabled? → Camera web UI → Network → RTSP")

    def _instar_preview_loop(self):
        """Continuously read frames from the Instar RTSP stream."""
        while self.preview_running:
            frame = self.instar.read_frame()
            if frame is not None:
                self._push_frame(frame)
            time.sleep(INSTAR_PREVIEW_INTERVAL)

    # ──────────────────────────────────────────────
    # GoPro
    # ──────────────────────────────────────────────

    def _connect_gopro(self):
        """Start the GoPro connection attempt in a background thread."""
        self.gopro_status_lbl.configure(text="Connecting …")
        self.btn_gopro.configure(state="disabled")

        def try_connect():
            ok = self.gopro.check_connection()
            if ok:
                info  = self.gopro.get_info()
                model = info.get("info", {}).get("model_name", "GoPro")
                self.after(0, self._gopro_ok, model)
            else:
                self.after(0, self._gopro_fail)

        threading.Thread(target=try_connect, daemon=True).start()

    def _gopro_ok(self, model):
        self.gopro_status_lbl.configure(text=f"✓  {model}",
                                        text_color=COLOR_GREEN)
        self.btn_gopro.configure(fg_color=COLOR_GREEN, hover_color="#28b84e",
                                 text="✓  Connected", state="normal")
        self.gopro.set_photo_mode()
        self.status_var.set("GoPro ready")

    def _gopro_fail(self):
        self.gopro_status_lbl.configure(text="Connection failed",
                                        text_color="#ff453a")
        self.btn_gopro.configure(state="normal")
        messagebox.showerror("GoPro not found",
            f"Could not reach {GOPRO_IP}.\n\n"
            "Check:\n"
            "• GoPro powered on?\n"
            "• Mac connected to GoPro WiFi hotspot?\n"
            "• Hero 8+: Connections → Enable WiFi\n"
            "• Quit the GoPro Quik app (it blocks the port)")

    # ──────────────────────────────────────────────
    # Battery display
    # ──────────────────────────────────────────────

    def _start_battery_loop(self):
        """Refresh battery once immediately, then on a background timer."""
        self._update_battery()
        threading.Thread(target=self._battery_loop, daemon=True).start()

    def _battery_loop(self):
        while True:
            time.sleep(BATTERY_REFRESH)
            self.after(0, self._update_battery)

    def _update_battery(self):
        pct, charging = get_mac_battery()
        self.mac_batt_var.set(
            f"{'⚡' if charging else '🔋'} {pct}%" if pct is not None else "🔋 –")
        ipct = get_iphone_battery()
        self.iphone_batt_var.set(f"📱 {ipct}%" if ipct else "📱 –")

    # ──────────────────────────────────────────────
    # Recording
    # ──────────────────────────────────────────────

    def _toggle_recording(self):
        if not self.recording:
            self._start_recording()
        else:
            self._stop_recording()

    def _start_recording(self):
        """Validate state, create session folder, and start the capture loop."""
        if self.source == "gopro" and not self.gopro.connected:
            messagebox.showwarning("GoPro not connected",
                "Please connect to the GoPro first.")
            return
        if self.source == "instar" and not self.instar.connected:
            messagebox.showwarning("Instar not connected",
                "Please connect to the Instar camera first.")
            return

        ts              = datetime.now().strftime(SESSION_TIMESTAMP_FMT)
        base            = os.path.expanduser(self.dir_var.get())
        self.output_dir = os.path.join(base, f"{SESSION_FOLDER_PREFIX}{ts}")
        os.makedirs(self.output_dir, exist_ok=True)

        self.recording   = True
        self.frame_count = 0
        self.start_time  = time.time()

        self.btn_start.configure(text="⏹   Stop Recording",
                                 fg_color=COLOR_REC, hover_color="#e03030")
        self.rec_dot.configure(text_color=COLOR_REC)
        labels = {"webcam": "Webcam", "gopro": "GoPro", "instar": "Instar"}
        self.status_var.set(f"REC  ·  {labels[self.source]}")

        loops = {"webcam": self._loop_webcam,
                 "gopro":  self._loop_gopro,
                 "instar": self._loop_instar}
        threading.Thread(target=loops[self.source], daemon=True).start()
        threading.Thread(target=self._update_elapsed, daemon=True).start()

    def _stop_recording(self):
        self.recording = False
        self.btn_start.configure(text="▶   Start Recording",
                                 fg_color=COLOR_GREEN, hover_color="#28b84e")
        self.rec_dot.configure(text_color=COLOR_MUTED)
        self.status_var.set("Stopped")
        self.elapsed_var.set("")

    def _loop_webcam(self):
        """Capture loop for webcam / iPhone Continuity Camera."""
        while self.recording:
            if self.cap and self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    self._save_frame(frame)
            time.sleep(float(self.interval_var.get()))

    def _loop_instar(self):
        """Capture loop for Instar RTSP stream."""
        while self.recording:
            frame = self.instar.read_frame()
            if frame is not None:
                self._save_frame(frame)
            else:
                self.after(0, self.status_var.set, "⚠  Instar: frame error")
            time.sleep(float(self.interval_var.get()))

    def _loop_gopro(self):
        """Capture loop for GoPro: trigger shutter → download → crop → save."""
        while self.recording:
            if self.gopro.take_photo():
                time.sleep(GOPRO_SHUTTER_WAIT)
                folder, filename = self.gopro.get_last_media()
                if folder and filename:
                    ts   = datetime.now().strftime(FRAME_TIMESTAMP_FMT)
                    dest = os.path.join(
                        self.output_dir,
                        f"{FRAME_PREFIX}{ts}_{self.frame_count:06d}.jpg")
                    if self.gopro.download_file(folder, filename, dest):
                        # Apply crop to the downloaded file
                        img = cv2.imread(dest)
                        if img is not None:
                            cv2.imwrite(dest,
                                        crop_frame(img, self.aspect_var.get()),
                                        [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
                        self.frame_count += 1
                        self.after(0, self.counter_var.set,
                                   f"{self.frame_count} frames")
                    else:
                        self.after(0, self.status_var.set,
                                   "⚠  GoPro: download error")
            time.sleep(max(1, float(self.interval_var.get()) - GOPRO_INTERVAL_BUFFER))

    def _save_frame(self, frame):
        """Crop and save a single frame with a timestamp filename."""
        frame = crop_frame(frame, self.aspect_var.get())
        ts    = datetime.now().strftime(FRAME_TIMESTAMP_FMT)
        path  = os.path.join(
            self.output_dir,
            f"{FRAME_PREFIX}{ts}_{self.frame_count:06d}.jpg")
        cv2.imwrite(path, frame, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
        self.frame_count += 1
        self.after(0, self.counter_var.set, f"{self.frame_count} frames")

    def _update_elapsed(self):
        """Update the elapsed time display every second while recording."""
        while self.recording:
            e    = int(time.time() - self.start_time)
            h, r = divmod(e, 3600)
            m, s = divmod(r, 60)
            self.after(0, self.elapsed_var.set, f"{h:02d}:{m:02d}:{s:02d}")
            time.sleep(1)

    # ──────────────────────────────────────────────
    # Video assembly
    # ──────────────────────────────────────────────

    def _assemble_video(self):
        """
        Combine all saved frames in the session folder into a video file.
        Uses the codec and container from the selected output format.
        """
        src    = getattr(self, "output_dir", None) or \
                 os.path.expanduser(self.dir_var.get())
        frames = sorted(glob.glob(os.path.join(src, f"{FRAME_PREFIX}*.jpg")))
        if not frames:
            messagebox.showwarning("No frames found",
                f"No frames were found in:\n{src}")
            return

        fps             = int(self.fps_var.get())
        fourcc_str, ext = OUTPUT_FORMATS[self.format_var.get()]
        ts              = datetime.now().strftime(VIDEO_TIMESTAMP_FMT)
        out_path        = os.path.join(src, f"{VIDEO_PREFIX}{ts}{ext}")

        first = cv2.imread(frames[0])
        h, w  = first.shape[:2]

        try:
            fourcc = cv2.VideoWriter_fourcc(*fourcc_str)
            writer = cv2.VideoWriter(out_path, fourcc, fps, (w, h))
            if not writer.isOpened():
                raise RuntimeError("VideoWriter could not be opened")
        except Exception as e:
            messagebox.showerror("Codec error",
                f"Codec '{fourcc_str}' is not available:\n{e}\n\n"
                "Tip: ProRes requires macOS. Please select MP4 or MOV instead.")
            return

        def run():
            total = len(frames)
            for i, f in enumerate(frames):
                img = cv2.imread(f)
                if img is not None:
                    if img.shape[:2] != (h, w):
                        img = cv2.resize(img, (w, h))
                    writer.write(img)
                self.after(0, self.status_var.set,
                           f"Rendering … {i + 1} / {total}")
            writer.release()
            self.after(0, self._assembly_done, out_path, total)

        threading.Thread(target=run, daemon=True).start()

    def _assembly_done(self, path, total):
        self.status_var.set("Ready")
        secs = total // max(1, int(self.fps_var.get()))
        messagebox.showinfo("Done",
            f"Video saved:\n{path}\n\n"
            f"{total} frames  ·  {self.fps_var.get()} FPS  ·  ~{secs} s\n"
            f"Format: {self.format_var.get()}")

    # ──────────────────────────────────────────────
    # Utility
    # ──────────────────────────────────────────────

    def _choose_dir(self):
        d = filedialog.askdirectory(initialdir=os.path.expanduser("~/Downloads"))
        if d:
            self.dir_var.set(d)

    def on_close(self):
        """Cleanly stop all threads and release hardware before quitting."""
        self.recording       = False
        self.preview_running = False
        time.sleep(SHUTDOWN_WAIT)
        if self.cap:
            self.cap.release()
        self.instar.release()
        self.destroy()


# ══════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    app = TimelapseApp()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()
