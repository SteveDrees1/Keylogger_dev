# Keylogger Project - DevMind

This project is a Python-based keylogger that captures keystrokes, encodes them in Base64, appends a salt, converts the result to binary, multiplies the binary by 24, and stores the final result in a MySQL database.

**Disclaimer**: This project is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Ensure you have explicit consent from all parties involved and comply with all applicable laws.

## Table of Contents

- [Keylogger Project](#keylogger-project)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Install Dependencies](#2-install-dependencies)
    - [3. Set Up MySQL Database](#3-set-up-mysql-database)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Security Considerations](#security-considerations)
  - [How It Works](#how-it-works)
    - [1. Key Press Capture](#1-key-press-capture)
    - [2. Base64 Encoding](#2-base64-encoding)
    - [3. Salt Generation](#3-salt-generation)
    - [4. Binary Conversion](#4-binary-conversion)
    - [5. Multiplication and Storage](#5-multiplication-and-storage)
  - [License](#license)
  - [Authors](#Authors)
  - [For Educational Purposes](#For Educational Purposes)

## Features

- Captures keystrokes in real-time using the `pynput` library.
- Encodes each keystroke in Base64.
- Appends a cryptographic salt to enhance security.
- Convert the result to a binary format.
- Multiplies the binary value by 24 for added complexity.
- Stores the final result in a MySQL database.

## Installation

Follow these steps to set up and run the keylogger on your system.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/keylogger_project.git
cd keylogger_project
```

### 2.Install Dependencies

The project requires Python and a few Python libraries. Install them using pip:

```bash
pip install -r requirements.txt
```

### 3. Set Up MySQL Database
1. Create a MySQL database
You can create a new database for your keylogger by running the following SQL command:

```bash
CREATE DATABASE keylogger_db;
```

This command creates a new database named keylogger_db. You can use a different name if you prefer.

2. Create a table to store keystrokes
Next, switch to the newly created database and create a table to store the keystrokes:

```bash
USE keylogger_db;

CREATE TABLE keystrokes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    key_pressed BIGINT,  -- Stores the processed key data
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Here’s what each part of the table does:

 - id INT AUTO_INCREMENT PRIMARY KEY: This column will automatically increment and serve as a unique identifier for each record.
 - key_pressed BIGINT: This column will store the processed key data as a large integer (the result of encoding, salting, binary conversion, and multiplication).
 - timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP: This column automatically records the time when each keystroke is logged.

## Configuration
The database configuration is stored in config/db_config.py. Update this file with your MySQL connection details:

```bash
DB_CONFIG = {
    'host': 'localhost',
    'database': 'keylogger_db',
    'user': 'your_username',
    'password': 'your_password'
}
```

Replace 'your_username' and 'your_password' with your actual MySQL credentials.

## Usage
To run the keylogger:

```bash
python3 src/keylogger.py
```

The keylogger will start capturing keystrokes and store the processed results in the MySQL database.

 - Legal Compliance: Ensure that you have legal permission to run a keylogger on any device you use.
 - Transparency: Always inform and obtain consent from all users who might be affected by the keylogger.
 - Data Handling: Consider encrypting or securely storing the data to prevent unauthorized access.

## How It Works
This keylogger operates through several key stages:

1. Key Press Capture
The pynput library captures each key press. The captured key is converted to a string and sanitized by removing unnecessary characters.

2. Base64 Encoding
The sanitized key is encoded in Base64 to ensure it’s represented in a consistent format.

3. Salt Generation
A cryptographic salt is generated using os.urandom(). This random value adds an additional layer of security, ensuring that identical keystrokes result in different stored values.

4. Binary Conversion
The Base64-encoded key and salt are converted to a binary integer. This integer represents the combined value of the key and salt.

5. Multiplication and Storage
The binary integer is multiplied by 24 for added complexity and then stored in the MySQL database.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.


### Authors
Steve Drees, and Victor Cabieles

## For Educational Purposes
 1. Run the keylogger as a background process
 - Windows:
Run the script using Python and redirect the output to null to avoid displaying anything in the terminal:

 ```bash
python keylogger.py >nul 2>&1
 ```

ON macOS/Linux:

```bash
nohup python3 keylogger.py >/dev/null 2>&1 &
```

2. Hide the Script File
Change the file attributes:
   - On Windows, you can make the file hidden:

```bash
attrib +h keylogger.py
```

On macOS/Linux, you can prepend a dot to the filename to hide it:

```bash
mv keylogger.py .keylogger.py
```

3. Use Startup Scripts (With Caution)
You can configure the script to run automatically when the computer starts.
   However, this should only be done on your own devices where you have control and consent:

On Windows:
 - Add a shortcut to the script in the Startup folder:
```bash
shell:startup
```

On macOS: Use a launchd launch agent to run the script automatically on startup.

4. Log Files
Ensure that the keylogger's log files are stored in a secure, hidden directory.
   For example, on macOS/Linux, you can store logs in a hidden directory:

```bash
mkdir ~/.logs
```

And then direct the keylogger to save logs there.

## Risks and Legal Consequences
Running a keylogger without proper consent, even on your own device,
can expose you to legal risks if other users are affected.
Unauthorized monitoring can violate privacy laws and lead to serious repercussions.

## Conclusion
If you're developing or testing a keylogger,
it's critical to limit its use to environments where you have full ownership and control,
and ensure that no other users are affected without their knowledge.
Always prioritize ethical considerations and legal compliance in your work.
If you need to monitor activity on a shared or public device,
use transparent and legally approved methods such as parental control software or security monitoring tools
that are designed for these purposes.