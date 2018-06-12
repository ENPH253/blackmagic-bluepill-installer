Import("env")
import os, shutil

print os.path.join(env.get("PROJECTBUILD_DIR"), env.get("PIOENV"), "blackmagic.elf")

def before_upload(source, target, env):
    print "Overwriting binaries to upload"
    shutil.copyfile("blackmagic", os.path.join(env.get("PROJECTBUILD_DIR"), env.get("PIOENV"), "firmware.elf"))
    shutil.copyfile("blackmagic.bin", os.path.join(env.get("PROJECTBUILD_DIR"), env.get("PIOENV"), "firmware.bin"))

env.AddPreAction("upload", before_upload)