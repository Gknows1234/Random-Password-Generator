# Password Tools

Simple Python scripts for password security management.

## What's Included

- **Password Strength Checker** - Evaluates how strong your password is
- **Password Generator** - Creates random secure passwords

## Requirements

- Python 3.x
- No additional packages needed (uses built-in modules only)

## How to Use

### Password Generator

```bash
password_generator.py
```

Choose option 1 to generate a password. Default is 12 characters but you can specify any length.

## Example Output

### Generator
```
Password Generator
-----------------
1. Generate password
2. Exit

Choose option: 1
Password length (press enter for 12): 
Your password: K9#mP2$vX8nQ
```

## Files

- `password_generator.py` - Password generation script
- `README.md` - This file

## Notes

The strength checker assumes a brute force attack rate of 1 billion attempts per second. Real-world crack times vary based on the attack method and hardware used.

Generated passwords include lowercase letters, uppercase letters, digits, and special characters for maximum security.
