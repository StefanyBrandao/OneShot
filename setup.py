import os

from cx_Freeze import setup, Executable

path = "./asset"
asset_list = [os.path.join(path, asset).replace("\\", "/") for asset in os.listdir(path)]

executables = [Executable("main.py", base=None)]

build_exe_options = {
    "include_files": asset_list,
    "packages": ["pygame"],
    "excludes": [],
    "include_msvcr": True
}

setup(
    name="OneShot",
    version="1.0",
    description="OneShot app",
    options={"build_exe": build_exe_options},
    executables=executables
)