FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app

COPY ./templates /app/templates

COPY requirements.txt /app

COPY app.py /app

COPY init-db.js /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
ENTRYPOINT ["python", "app.py"]

