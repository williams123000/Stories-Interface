# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['story_generator_gui.py'],
    pathex=[],
    binaries=[],
    datas=[('background2.jpg', '.'), ('Characters.json', '.'), ('CharactersTreasure.json', '.'), ('History.txt', '.'), ('Font', 'Font/'), ('logs', 'logs/'), ('HistoryFinal.py', '.'), ('History.py', '.'), ('Traslate.py', '.'), ('CharactersTreasure.json', '.')],
    hiddenimports=[],
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
    name='story_generator_gui',
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
)
