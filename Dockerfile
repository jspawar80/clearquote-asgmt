# Use an official Python image ( using alpine image that is most light weight )
FROM python:3.8-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# expose application port 3000
EXPOSE 3000

# Run main.py when the container launches
CMD ["python", "main.py"]
