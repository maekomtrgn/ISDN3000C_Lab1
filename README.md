# Task 0 requirements:  a. Use the terminal with an account with "sudo" or admin access b. Grant the terminal Full Disk Access 
# Install Command Line tools. Usually, a popup will say this already exists
xcode-select --install
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install dependencies using Homebrew
brew install openssl readline sqlite3 xz zlib
# Install Python 3.11
brew install python@3.11
# Go to your project directory
cd ~/Downloads
# Create a virtual environment
$(brew --prefix python@3.11)/bin/python3.11 -m venv venv1
# Activate the environment
source venv1/bin/activate
# Verify the version
python --version
# Expected output: Python 3.11.x (or similar)

# Install requests from Python 2.31 was downloaded
pip install requests==2.31.0 
# freeze current setup
pip freeze > requirements.txt 
# After you complete the tasks, stop (deactivate) the environment
deactivate

# The terminal is like a text box where you communicate with your laptop and give commands (command-line interface). Virtual environments ensure that dependencies are isolated to your project and not affecting your system Python. In your virtual environment, you can download specific Python packages which makes it easier to use certain versions of Python because future versions may make codes have bugs or new changes. You cannot commit a virtual environment into Github. You need to set up gitignore. 



// Git is a version control system that can track changes in code and collaborations. In this task we learn git status, git config, git clone, git add, git log, git push and git pull. 
brew install git 
git --version //verify


// Unlike in Windows that uses Bash, Git can be used on the terminal via Homebrew. Staging involves adding the files in the folder that cloned the repository via git clone. Committing would be to commit changes and they have a message that should be descriptive so future self would have an easier time. Always use git status to check status before git commit. Git push and pull are related to pushing files into GitHub. Git push is to upload files while git pull is to pull changes made in the local repository. Git log is to check history.

# Set your username for all repositories on your system
git config --global user.name "My Laptop CLI"

# Set your email address for all repositories on your system
git config --global user.email "mmataragnon@connect.ust.hk"

# Get the repo link
# For a public repository
git clone https://github.com/user/ISDN3000C_Lab1.git

# For a private repository, you will be prompted for credentials
git clone https://github.com/user/ISDN3000C_Lab1.git

#git status should show that no files are waiting to be added
cd ~/Downloads/3000CLab1/ISDN3000C_Lab1
git status

#make README.txt.Edit file and then change file type to README.md
git add READMe.md
git commit -m "Add initial project files and README.md"
#move venv1 into the folder
touch .gitignore
#edit .gitignore in vscode and put venv1/
git push -u origin main

