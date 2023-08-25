import urllib.request
import os

repo_url = "https://github.com/MansurAitkul/HomeWorks"

temp_dir = "temp"

os.makedirs(temp_dir, exist_ok=True)

urllib.request.urlretrieve(repo_url + "/file.py", os.path.join(temp_dir, "file.py"))

import_path = os.path.join(temp_dir, "file.py")

import file

def main():
    file.my_function()
if __name__ == "__main__":
    main()