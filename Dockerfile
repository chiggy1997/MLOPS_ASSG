# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the Flask app

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

ENTRYPOINT [ "flask"]
CMD ["run", "--host", "0.0.0.0"]
