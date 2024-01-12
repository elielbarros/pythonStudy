"""
os + shutil - Move, Copy, Remove

Move/Rename -> shutil.move
Move/Rename -> os.rename

Copy -> shutil.copy

Delete -> os.unlink
Delete directory recursively -> shutil.rmtree
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
TEST_FOLDER = os.path.join(DESKTOP, 'test_folder')
TEST_FILE = os.path.join(TEST_FOLDER, 'test_file.txt')
NEW_TEST_FOLDER = os.path.join(DESKTOP, 'new_test_folder')

# exist_ok will indicate that if the folder already exists, it is not necessary to create and not necessary to raise
# error
os.makedirs(NEW_TEST_FOLDER, exist_ok=True)

for root, dirs, files in os.walk(TEST_FOLDER):

    for dir_ in dirs:
        new_test_folder_path = os.path.join(
                root.replace(TEST_FOLDER, NEW_TEST_FOLDER),
                dir_
        )

        os.makedirs(new_test_folder_path, exist_ok=True)

    for file_ in files:
        file_path = os.path.join(root, file_)
        new_file_path = os.path.join(
                root.replace(TEST_FOLDER, NEW_TEST_FOLDER),
                file_
        )
        shutil.copy(file_path, new_file_path)

