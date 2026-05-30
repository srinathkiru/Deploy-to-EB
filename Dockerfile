FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the dependencies file to the container
COPY requirements.txt .

# Step 4: Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code
COPY app.py .

#0 Step 6: Expose the port the app runs on
EXPOSE 5050

# Step 7: Define the command to start the application
CMD ["python", "-m", "flask", "run"]
