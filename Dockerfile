<<<<<<< HEAD
# Rules to create the image(light weight computer)

# borrowing Base image - python + os(linux slim) from Docker Hub (https://hub.docker.com/_/python)
FROM python:3.12-slim

# Creating a directory -app
WORKDIR /app

# Copying requirements file into the container directory -app
=======
# Base image - python + os
FROM python:3.12-slim
# Creating a directory
WORKDIR /app
# Copying requirements file into the container directory
>>>>>>> a15694a9f1680cfc41f3fa573beb8025217ce988
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY apps/flask_app.py .
COPY models/xgb_car_price_model.pkl ./models/

# location of the flask app/ port number
EXPOSE 5000

CMD ["python", "flask_app.py"]