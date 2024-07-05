FROM node:20.3.1-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json into the container
COPY frontend/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the frontend code into the container
COPY frontend /app/

# Expose the port the app runs on
EXPOSE 3000

# Run the frontend development server
CMD ["npm", "run", "dev"]
