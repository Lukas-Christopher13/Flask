FROM python:3.8.10

WORKDIR /usr/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

#ENV FLASK_APP=/usr/app.py

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0" ]