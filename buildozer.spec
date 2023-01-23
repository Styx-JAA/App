[app]
source.dir = .
source.include_exts = py,png

# Application name
title = ArrangeDotME

# Application version
version = 6.9

# Application description
description = A Kivy application that sorts scores in an Excel file.

# Application author
author = Styx-JAA

# Application license
license = Hello, World!

# Application icon (128x128)
icon.filename = index.png

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

requirements = kivy,openpyxl

[buildozer]

# Minimum version of python for buildozer
python = 3.7

# Minimum version of kivy for buildozer
kivy = 1.11.1

log_level = 2

[android]

permissions = android.permission.WRITE_EXTERNAL_STORAGE, android.permission.READ_EXTERNAL_STORAGE


# Minimum version of android for buildozer
android.api = 27

# Minimum version of android sdk for buildozer
android.minapi = 21

# Minimum version of android ndk for buildozer
android.ndk = 21

# Java JDK version
android.jdk = 8

# Android package name
package.name = ArrangeDotMe

# Android package domain
package.domain = sty.Arrange.me

# Android entry point
android.entrypoint = org.renpy.android.PythonActivity

# Android app theme
android.theme = @android:style/Theme.NoTitleBar
