FROM python:3.9-alpine

# Copy and set the working directory
ADD . /app
WORKDIR /app

# Copy and install the requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Run the Flask server
CMD ["python", "app/main.py"]