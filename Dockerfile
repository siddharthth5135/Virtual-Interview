# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js and npm for building the React app
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_14.x | bash - && \
    apt-get install -y nodejs && \
    npm install -g npm@latest

# Copy the rest of the application code
COPY . .

# Install Node.js dependencies and build the React app
WORKDIR /usr/src/app/Frontend
RUN npm install
RUN npm run build

# Move the build files to a directory served by Flask
RUN mkdir -p /usr/src/app/Backend/static
RUN cp -r build/* /usr/src/app/Backend/static/

# Expose the port the app runs on
EXPOSE 3000

# Copy supervisord configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Define environment variable
ENV NAME=World

# Start both services using supervisord
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
