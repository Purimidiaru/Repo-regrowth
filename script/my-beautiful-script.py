import os
import subprocess

REPO_URL = 'https://github.com/descartes-underwriting/devops-technical-test-data.git'
BRANCH = '01-01-2022-test'

def clone_repo():
    # Clone the repository (if we didn't clone the repo yet, then it will git clone the repo)
    if not os.path.exists('devops-technical-test-data'):
        subprocess.run(['git', 'clone', REPO_URL])

def checkout_branch():
    # From now on it will just do a git checkout to get the right branch
    os.chdir('devops-technical-test-data')
    subprocess.run(['git', 'checkout', BRANCH])

def get_all_commits():
    # Get all commits
    commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
    return commits

def backup_commit(commit):
    # Checkout all commit
    subprocess.run(['git', 'checkout', commit])

    # Get all modified files in the commit
    modified_files = subprocess.check_output(['git', 'diff-tree', '--no-commit-id', '--name-only', '-r', commit]).decode('utf-8').splitlines()

    # Define dir to get all backup
    backup_dir = '../data'

    # Create a dir, 1 dir = 1 commit
    commit_dir = os.path.join(backup_dir, commit)
    os.makedirs(commit_dir, exist_ok=True)

    for file in modified_files:
        # Create dirs
        file_dir = os.path.join(commit_dir, os.path.dirname(file))
        os.makedirs(file_dir, exist_ok=True)
        
        # Copying file
        if os.path.exists(file):
            subprocess.run(['cp', file, file_dir])

def reset_branch_state():
    # Reset branch state
    subprocess.run(['git', 'checkout', BRANCH])

def main():
    clone_repo()
    checkout_branch()
    commits = get_all_commits()
    backup_dir = '../data'
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    for commit in commits:
        commit_dir = os.path.join(backup_dir, commit)
        # Verify if there is no new commit to backup to avoid errors
        if not os.path.exists(commit_dir):
            backup_commit(commit)
    reset_branch_state()

if __name__ == '__main__':
    main()