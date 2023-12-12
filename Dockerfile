FROM python:3.8-slim

WORKDIR /usr/src/app

COPY . .

EXPOSE 1212

CMD ["python", "app.py"]
