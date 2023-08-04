import os 
import shutil


def makedir(dirname):
    if os.path.isdir(dirname):
        print("Already Exists")
        return
    else:
        os.mkdir(dirname)
def insert_into_dir(currentdir, dirname ,keywords):
    makedir(dirname)
    for file_name in os.listdir(currentdir):
        f = os.path.join(currentdir, file_name)
        if os.path.isfile(f):
            for word in keywords:
                if word in file_name:
                    shutil.move(f, dirname)
def insert_folders_into_dir(folderdirs, final_dir):
    makedir(final_dir)
    for dir in folderdirs:
        shutil.move(dir, final_dir)

