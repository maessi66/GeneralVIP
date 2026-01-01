[app]
title = GeneralVIP
package.name = generalvip
package.domain = org.general.vip

source.dir = .
source.include_exts = py,kv,png,jpg,ttf

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_SMS,SEND_SMS

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True
android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 0
