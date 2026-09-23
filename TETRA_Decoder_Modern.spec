# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/PHA/Desktop/TetraEar-master/tetraear/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/PHA/Desktop/TetraEar-master/tetraear/bin/librtlsdr.dll', 'tetraear/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/bin/libusb-1.0.dll', 'tetraear/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/tetra_codec/bin/ccoder.exe', 'tetraear/tetra_codec/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/tetra_codec/bin/cdecoder.exe', 'tetraear/tetra_codec/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/tetra_codec/bin/scoder.exe', 'tetraear/tetra_codec/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/tetra_codec/bin/sdecoder.exe', 'tetraear/tetra_codec/bin'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/assets/banner.png', 'tetraear/assets'), ('C:/Users/PHA/Desktop/TetraEar-master/tetraear/assets/icon_preview.png', 'tetraear/assets')],
    hiddenimports=['tetraear', 'tetraear.audio.export', 'tetraear.audio.voice', 'tetraear.core.crypto', 'tetraear.core.decoder', 'tetraear.core.protocol', 'tetraear.signal.capture', 'tetraear.signal.processor', 'tetraear.signal.scanner', 'tetraear.ui.modern', 'numpy', 'scipy', 'PyQt6', 'PyQt6.QtCore', 'PyQt6.QtGui', 'PyQt6.QtWidgets', 'sounddevice', 'rtlsdr', 'bitstring'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='TETRA_Decoder_Modern',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:/Users/PHA/Desktop/TetraEar-master/tetraear/assets/icon_preview.png'],
)
