Import("env", "projenv")
import os, shutil

def before_upload(source, target, env):
    print("Overwriting binaries to upload")
    shutil.copyfile("blackmagic", os.path.join(projenv.subst(projenv.get("BUILD_DIR")), "firmware.elf"))
    shutil.copyfile("blackmagic.bin", os.path.join(projenv.subst(projenv.get("BUILD_DIR")), "firmware.bin"))

env.AddPreAction("upload", before_upload)