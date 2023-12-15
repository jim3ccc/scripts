import os
import subprocess

def git_pull_in_directories(root_dir='.'):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '.git' in dirnames:
            git_directory = os.path.join(dirpath, '.git')
            try:
                # Stash changes
                subprocess.run(['git', 'stash', '.'], cwd=dirpath, check=True)
                # Checkout the main branch
                subprocess.run(['git', 'checkout', 'main'], cwd=dirpath, check=True)
                # Pull new changes
                subprocess.run(['git', 'pull'], cwd=dirpath, check=True)
                print(f"Git pull successful in {dirpath}")
            except subprocess.CalledProcessError as e:
                print(f"Error in {dirpath}: {e}")
        else:
            continue

if __name__ == "__main__":
    root_directory = input("Enter the root directory (default is current directory): ").strip()
    if not root_directory:
        root_directory = '.'

    git_pull_in_directories(root_directory)
