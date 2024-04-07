from setuptools import setup

APP = ['Autoclicker.py']
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'CFBundleName': 'AutoClicker',
        'CFBundleDisplayName': 'AutoClicker',
        'CFBundleGetInfoString': "Auto clicking application",
        'CFBundleIdentifier': "com.example.autoclicker",
        'CFBundleVersion': "0.1",
        'CFBundleShortVersionString': "0.1",
        'iconfile': 'resources/icon(mac).icns'
    }
}

setup(
    app=APP,
    name='AutoClicker',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
