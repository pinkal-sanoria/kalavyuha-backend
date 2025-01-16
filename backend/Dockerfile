FROM python:3.9

WORKDIR /app

# Copy requirements.txt first to avoid re-installing dependencies on every build
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install 
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

EXPOSE 8000

CMD ["python3", "main.py"]
