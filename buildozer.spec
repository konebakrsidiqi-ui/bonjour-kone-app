[app]

# (string) Title of your application
title = Bonjour KONE

# (string) Package name
package.name = bonjourkone

# (string) Package domain (needed for android packaging)
package.domain = org.kone

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv

# (string) Application version
version = 1.0

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3, kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK API to use
android.ndk_api = 21

# (bool) If True, then skip trying to update the Android sdk licenses
android.accept_sdk_license = True

# (list) The Android architectures to build for
android.archs = armeabi-v7a, arm64-v8a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
