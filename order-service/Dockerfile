FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["gunicorn", "-w", "4", "-b", ":5002", "app:app"]
