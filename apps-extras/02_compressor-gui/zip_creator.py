import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zip:
        for file in filepaths:
            file = pathlib.Path(file)
            zip.write(file, arcname=file.name)

if __name__ == "__main__":
    filepaths = ["/home/wecher/Downloads/Artificial - Bilinkis.pdf", "/home/wecher/Downloads/kubectl.sha256"]
    folder = "/home/wecher/Downloads/"
    make_archive(filepaths, folder)