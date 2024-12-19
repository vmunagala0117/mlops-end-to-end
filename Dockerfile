FROM python:3.12-slim
WORKDIR /app
COPY . /app

RUN apt update -y

RUN apt-get update && pip install -r requirements.txt

# Expose port for Flask app which listens on port 5000
EXPOSE 5000

# Use gunicorn to run the Flask app in the background
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.frontend.flask_app:app"]