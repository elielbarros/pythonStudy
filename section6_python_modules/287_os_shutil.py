"""
os + shutil - Move, Copy, Remove

Move/Rename -> shutil.move
Move/Rename -> os.rename

Copy -> shutil.copy

Delete FILE -> os.unlink
Delete directory recursively -> shutil.rmtree
"""
import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
TEST_FOLDER = os.path.join(DESKTOP, 'test_folder')
TEST_FILE = os.path.join(TEST_FOLDER, 'test_file.txt')
NEW_TEST_FOLDER = os.path.join(DESKTOP, 'new_test_folder')

# Delete directory recursively, it will garantee that this new test folder does not exist
shutil.rmtree(NEW_TEST_FOLDER, ignore_errors=True)

# Copy file from folder to another and new folder, creating this new folder
shutil.copytree(TEST_FOLDER, NEW_TEST_FOLDER)

shutil.move(NEW_TEST_FOLDER, NEW_TEST_FOLDER + '_WHAT')