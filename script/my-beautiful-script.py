import os
import subprocess
import codecs

REPO_URL = 'https://github.com/Purimidiaru/portfolio-website'
BRANCH = 'main'

def clone_repo():
    # Clone the repository (if we didn't clone the repo yet, then it will git clone the repo)
    if not os.path.exists('portfolio-website'):
        subprocess.run(['git', 'clone', REPO_URL])

def checkout_branch():
    # From now on it will just do a git checkout to get the right branch
    os.chdir('portfolio-website')
    subprocess.run(['git', 'checkout', BRANCH])

def get_all_commits():
    # Get all commits
    commits = subprocess.check_output(['git', 'log', '--pretty=format:%H']).decode('utf-8').splitlines()
    return commits

def decode_escaped_path(escaped_path):
    # Decode escaped path to solve path names
    escaped_path = escaped_path.strip('"')
    return codecs.escape_decode(escaped_path)[0].decode('utf-8')

def backup_commit(commit):
    # Checkout all commit
    subprocess.run(['git', 'checkout', commit])

    # Get all modified files in the commit (Used git show instead of git diff-tree to get README.md)
    modified_files = subprocess.check_output(['git', 'show', '--pretty=format:', '--name-only', commit]).decode('utf-8').splitlines()
    print(f"Modified files for commit {commit}: {modified_files}")

    # Define dir to get all backup
    backup_dir = '../data'

    # Create a dir, 1 dir = 1 commit
    commit_dir = os.path.join(backup_dir, commit)
    os.makedirs(commit_dir, exist_ok=True)

    for file in modified_files:
        # Sanitize file naming
        sanitized_file = decode_escaped_path(file)

        # Create dirs
        file_dir = os.path.join(commit_dir, os.path.dirname(sanitized_file))
        os.makedirs(file_dir, exist_ok=True)
        
        # Copying file
        if os.path.exists(sanitized_file):
            subprocess.run(['cp', sanitized_file, file_dir])
            print(f"Copied {sanitized_file} to {file_dir}")
        else:
            print(f"File does not exist: {sanitized_file}")

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
