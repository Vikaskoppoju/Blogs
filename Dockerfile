# Use an official Python runtime as a parent image
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run the Django app when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
