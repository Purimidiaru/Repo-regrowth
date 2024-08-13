import unittest
import os
import subprocess
import codecs
import re

class TestBackupScript(unittest.TestCase):

    @classmethod
    # Run script by defining the command to run
    def setUpClass(cls):
        subprocess.run(['python3', 'script/my-beautiful-script.py'])

    def octal_to_utf8(self, octal_string):
        # Find all octal sequences in the format \xxx and also keep track of normal characters
        # The regex captures either octal sequences (\xxx) or single characters (.)
        octal_matches = re.split(r'(\\\d{3})', octal_string)

        # Create a bytearray to store the resulting bytes
        byte_array = bytearray()

        for part in octal_matches:
            if part.startswith('\\') and len(part) == 4:
                # Convert each octal sequence to its byte value
                byte_array.append(int(part[1:], 8))
            else:
                # Append the regular characters as is
                byte_array.extend(part.encode('utf-8'))

        # Decode the byte array to a UTF-8 string
        utf8_string = byte_array.decode('utf-8')
        
        return utf8_string

    def test_backup_directory_exists(self):
        # Check if 'data', the backup dir exists or not
        self.assertTrue(os.path.exists('data'))

    def test_commits_backup(self):
        os.chdir('portfolio-website')
        # Get commit hashes
        commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
        os.chdir('..')
        # Check if 1 correct dir = 1 correct commit
        for commit in commits:
            commit_dir = os.path.join('data', commit)
            self.assertTrue(os.path.exists(commit_dir))

    def sanitize_filename(self, filename):
        if filename.startswith('"') and filename.endswith('"'):
            filename = filename[1:-1]
            filename = self.octal_to_utf8(filename)
        # Replace escaped quotes with actual quotes
        filename = filename.replace('\\"', '"')
        # Handle escaped backslashes
        filename = filename.replace('\\\\', '\\')
        return filename

    def get_files_from_commit(self, commit):
        # Getting files to backup with git show command
        os.chdir('portfolio-website')
        commit_files_output = subprocess.check_output(['git', 'show', '--pretty=format:', '--name-only', commit]).decode('utf-8')
        os.chdir('..')
        return commit_files_output.splitlines()

    # Same principe as test_commits_backup function but with files from commit dirs
    def test_files_backed_up(self):
        os.chdir('portfolio-website')
        commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
        os.chdir('..')
        for commit in commits:
            modified_files = self.get_files_from_commit(commit)
            for file in modified_files:
                sanitized_file = self.sanitize_filename(file)
                backup_file = os.path.join('data', commit, sanitized_file)
                if not os.path.exists(backup_file):
                    print(f"Missing file: {backup_file}")
                self.assertTrue(os.path.exists(backup_file))

if __name__ == '__main__':
    unittest.main()
