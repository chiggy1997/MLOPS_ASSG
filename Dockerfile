# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "-v", "tests/test_model.py"]
CMD ["python3", "-m", "Flask",  "run", "--host=0.0.0.0"] 
