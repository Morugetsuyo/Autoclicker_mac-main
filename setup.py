from setuptools import setup

APP = ['Autoclicker.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': [],
    'plist': {
        'CFBundleIconFile': 'icon(mac).icns',
        'CFBundleIdentifier': 'com.example.Autoclicker',
        'CFBundleName': 'AutoClicker',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0'
    },
    'iconfile': 'resources/appicon.icns',  
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
