#!/bin/bash

# Configuration
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo ".env file not found. Please create it from .env.example first."
    exit 1
fi

if [ -z "$PUBLIC_IP" ] || [ "$PUBLIC_IP" == "your-ec2-ip" ]; then
    echo "PUBLIC_IP must be set in the .env file."
    exit 1
fi

# Create SSL directory
mkdir -p ./ssl

# Generate self-signed certificate
echo "Generating self-signed certificate for $PUBLIC_IP..."
openssl req -x509 -nodes -newkey rsa:4096 -days 365 \
    -keyout "./ssl/privkey.pem" \
    -out "./ssl/fullchain.pem" \
    -subj "/CN=$PUBLIC_IP"

echo "Certificate generation complete! Files located in ./ssl"
echo "NOTE: Browsers will show a security warning. You must click 'Advanced' -> 'Proceed' when accessing the site."
