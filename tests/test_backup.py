import unittest
import os
import subprocess

class TestBackupScript(unittest.TestCase):
    
    @classmethod
    # Run script
    def setUpClass(cls):
        subprocess.run(['python', 'script/my-beautiful-script.py'])
    
    # Check if 'data', the backup dir exists or not
    def test_backup_directory_exists(self):
        self.assertTrue(os.path.exists('data'))
    
    def test_commits_backup(self):
        os.chdir('devops-technical-test-data')
        # Get commit hashes
        commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
        os.chdir('..')
        
        # Check if 1 correct dir = 1 correct commit
        for commit in commits:
            commit_dir = os.path.join('data', commit)
            self.assertTrue(os.path.exists(commit_dir))

    # Same principe as test_commits_backup function but with files from commit dirs
    def test_files_backed_up(self):
        os.chdir('devops-technical-test-data')
        commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
        os.chdir('..')
        
        for commit in commits:
            os.chdir('devops-technical-test-data')
            modified_files = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit]).decode('utf-8').splitlines()
            os.chdir('..')
            
            for file in modified_files:
                backup_file = os.path.join('data', commit, file)
                self.assertTrue(os.path.exists(backup_file))

if __name__ == '__main__':
    unittest.main()