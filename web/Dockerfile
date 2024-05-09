FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1


# Set the working directory
WORKDIR /web

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
