# Password Generator

A simple Python script for generating secure random passwords. 

## Features
- **Two password complexity levels**:
  - Simple: Contains letters and numbers.
  - Complex: Includes letters, numbers, and special characters.
- Fully customizable:
  - Adjust password length.
  - Define character sets.
- Easy to use and lightweight.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-generator.git
   cd password-generator
   ```

2. Run the script:
  ```bash
  python password_generator.py
  ```

3. Configuration
  You can customize the following parameters directly in the script:
  USE_COMPLEX_PASSWORD: Set to True for complex passwords or False for simple passwords.
  SHORT_PASSWORD_LENGTH: Length of simple passwords.
  COMPLEX_PASSWORD_LENGTH: Length of complex passwords.

Example Output:
  ```plaintext
  Simple password: abc123
  Complex password: aB1#cD!9@ 
