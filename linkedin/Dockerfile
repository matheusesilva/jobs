# Official Playwright Python + Browsers (stable)
FROM mcr.microsoft.com/playwright/python:v1.48.0-focal

# Add AWS Lambda Runtime Interface Client
RUN pip install --no-cache-dir awslambdaric

# Install AWS Lambda RIE (local testing only)
ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie \
    /aws-lambda-rie
RUN chmod +x /aws-lambda-rie

# Set Lambda working dir
WORKDIR /var/task

# Copy your function code
COPY index.py /var/task/
COPY requirements.txt /var/task/

# Install additional Python dependencies (optional)
RUN pip install --no-cache-dir -r /var/task/requirements.txt || true

# Lambda runtime interface
ENTRYPOINT ["/usr/bin/python3", "-m", "awslambdaric"]

# The handler name = file.lambda_handler
CMD ["index.handler"]

