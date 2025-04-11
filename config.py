class Config:
    # Flask app configuration
    SECRET_KEY = 'your_secure_secret_key_here'  # Change this to a secure random string
    DEBUG = True  # Set to False in production
    
    # AWS Configuration
    AWS_REGION_NAME = 'your-aws-region'  # e.g., 'us-east-1'
    
    # Email configuration
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587
    SENDER_EMAIL = 'your-email@gmail.com'
    SENDER_PASSWORD = 'your-app-password'  # Use an app password for Gmail
    ENABLE_EMAIL = False  # Set to True to enable email sending
    
    # SNS configuration
    SNS_TOPIC_ARN = ''  # Optional - Add your SNS topic ARN if you want notifications