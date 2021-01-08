FROM python:3.8

WORKDIR app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE 5000

CMD ["python", "traveller.py"]