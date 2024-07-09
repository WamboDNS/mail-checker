#!/bin/bash

# Define the Python script and virtual environment directory
SCRIPT="check_mails.py"
VENV_DIR=".venv"
LINK_NAME="check-mails"

# Prompt the user for email configuration details
read -p "Enter IMAP server: " IMAP_SERVER
read -p "Enter email address: " EMAIL_ACCOUNT
read -s -p "Enter email password: " EMAIL_PASSWORD
echo

# Create the .env file with the provided details
cat > .env <<EOL
EMAIL_SERVER=${IMAP_SERVER}
EMAIL_ACCOUNT=${EMAIL_ACCOUNT}
EMAIL_PASSWORD=${EMAIL_PASSWORD}
EOL

# Create a virtual environment
python3 -m venv ${VENV_DIR}

# Activate the virtual environment and install dependencies
source ${VENV_DIR}/bin/activate
pip install -r requirements.txt
deactivate

# Get the full path of the Python interpreter in the virtual environment
VENV_PYTHON="${PWD}/${VENV_DIR}/bin/python"

# Update the shebang line of the Python script
sed -i "1s|^#!.*|#!${VENV_PYTHON}|" ${SCRIPT}

SCRIPT_DIR=$(pwd)

# Update the .env file path in the Python script
sed -i "s|load_dotenv()|load_dotenv(os.path.join('${SCRIPT_DIR}', '.env'))|" ${SCRIPT}

# Make the Python script executable
chmod +x ${SCRIPT}

# Create a symbolic link to the script in /usr/local/bin
sudo ln -sf "$(realpath ${SCRIPT})" "/usr/local/bin/${LINK_NAME}"

echo "Setup complete. You can now run the script using 'check-mails'"
