# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['story_generator_gui.py'],
             pathex=[],
             binaries=[],
             datas=[
                 ('background2.jpg', '.'),  # Incluye archivos necesarios
                 ('Font/ProductSans.ttf', 'Font'),
                 ('HistoryFinal.py', '.'),
                 ('History.py', '.'),
                 ('CharactersTreasure.json', '.'),
                 ('Characters.json', '.'),
                 ('Traslate.py', '.'),
                 ('icono.ico', '.')
             ],
             hiddenimports=['pyttsx3.drivers', 'pyttsx3.drivers.sapi5'],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='StoryGenerator',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,  # Para aplicaciones GUI
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='icono.ico')
