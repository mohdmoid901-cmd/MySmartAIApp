[app]
title = Smart AI Auto Reply
package.name = smartaiapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,requests,urllib3,certifi,idna,charset_normalizer

orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0

# Android specific
android.api = 33
android.minapi = 21
android.sdk_build_tools_version = 33.0.2
android.ndk_api = 21
android.private_storage = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 0
