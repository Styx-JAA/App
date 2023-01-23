[app]
source.dir = .
source.include_exts = py

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

[buildozer]

# Minimum version of python for buildozer
python = 3.7

# Minimum version of kivy for buildozer
kivy = 1.11.1

[requirements]

# List of python packages to be included
python = openpyxl

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
package.name = com.ezekiel.jeg

# Android package domain
package.domain = com.ezekiel

# Android entry point
android.entrypoint = org.renpy.android.PythonActivity

# Android app theme
android.theme = @android:style/Theme.NoTitleBar

[ios]

# Minimum version of ios for buildozer
ios.deployment_target = 12.0

# iOS bundle identifier
ios.identifier = com.ezekiel.jeg

# iOS bundle name
ios.name = ArrangeDotME
