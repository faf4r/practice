# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['米奇妙妙屋GUI版.py'],
             pathex=['C:\\Users\\Administrator\\Desktop\\GUI'],
             binaries=[],
             datas=[('F:\Python\Lib\site-packages\pyzbar\libiconv-2.dll','.'),
			 ('F:\Python\Lib\site-packages\pyzbar\libzbar-32.dll','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='米奇妙妙屋GUI版',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
