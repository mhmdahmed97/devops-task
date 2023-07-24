FROM arm64v8/python:3.9-slim
# Create and set working directory
WORKDIR /app
# Copy requirements file
COPY requirements.txt /app
# Install dependencies
RUN pip install -r requirements.txt
# Copy application
COPY . /app
# Expose port 3000
EXPOSE 3000
# Run the application
CMD [ "python", "./transcoder.py" ]