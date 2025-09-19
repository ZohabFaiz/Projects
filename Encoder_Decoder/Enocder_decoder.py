import smtplib
from email.message import EmailMessage
import os

def get_credentials():
    """
    Checks for a config.py file and reads credentials from it.
    If the file doesn't exist, it prompts the user for credentials
    and saves them to a new config.py file.
    """
    config_file = 'config.py'
    if os.path.exists(config_file):
        try:
            # Import the variables from the config file
            from config import SENDER_EMAIL, SENDER_PASSWORD
            print("Using saved credentials.")
            return SENDER_EMAIL, SENDER_PASSWORD
        except ImportError:
            print("Error reading config.py. Please re-enter credentials.")
    
    # If config file doesn't exist or is invalid, ask for credentials
    print("No saved credentials found. Please enter them now.")
    sender_email = input('Enter Your Email: ')
    sender_password = input('Enter Your Password: ')
    
    # Save the new credentials to the config file
    with open(config_file, 'w') as f:
        f.write(f"SENDER_EMAIL = '{sender_email}'\n")
        f.write(f"SENDER_PASSWORD = '{sender_password}'\n")
    
    print("Credentials saved successfully! ✨")
    return sender_email, sender_password


ins = input('Enter to "Encode" or "Decode": ')
message = input('Enter the message: ')

if ins.lower() == 'encode':
    Encoded = ''
    t = message.split(' ')
    for m in range(0, len(t)):
        if len(t[m]) < 10:
            t[m] = t[m] + str(len(t[m]))
        else:
            t[m] = t[m] + str(len(t[m]) % 9)

    for i in range(len(t)):
        for j in range(len(t[i])):
            k = ord(t[i][j])
            k = k - len(t[i]) + 10
            Encoded += chr(k)
        Encoded += ' '
    
    # Get the credentials (either saved or new)
    sender_email, sender_password = get_credentials()
    R = input('Enter the Receiver Email: ')
    
    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Encoded Message'
    msg['From'] = sender_email
    msg['To'] = R
    msg.set_content(Encoded)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
        print("Email sent successfully! 😎")
    except Exception as e:
        print(f"Something went wrong: {e} 😬")
        print("If you're using Gmail, ensure you've enabled 2-Step Verification and are using an App Password.")

elif ins.lower() == 'decode':
    decoded = ''
    p = message.split(' ')
    for i in range(len(p)):
        for j in range(0, len(p[i]) - 1):
            d = ord(p[i][j])
            d = d + len(p[i]) - 10
            decoded += chr(d)
        decoded += ' '
    print('Decoded Message:', decoded)
else:
    print('Invalid choice. Please enter "Encode" or "Decode".')