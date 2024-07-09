# check-mails

Check Mails is a Python script that connects to an IMAP email server, fetches unread emails, and displays them in the terminal (first 100 characters of each mail).

WARNING: This is a prototype for now and your credentials are stored in a config file in _clear text_. So if you want to use this with an important passwort, be careful please.

## Features

- display unread mails in terminal

## Installation

### Manual Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/check-mails.git
    cd check-mails
    ```

2. **Make the setup script executable**:

    ```bash
    chmod +x setup.sh
    ```

3. **Run the setup script**:

    The setup script will prompt you for your email configuration details (IMAP server, email address, and password), create a virtual environment, install the required dependencies, and configure the script for use.

    ```bash
    ./setup.sh
    ```

4. **Run the script**:

    After completing the setup, you can run the script from anywhere using the `check-mails` command:

    ```bash
    check-mails
    ```
## Usage

Once installed, you can use the `check-mails` command to check your unread emails. The script will display the sender, subject, received date, and the first 100 characters of the email body.
