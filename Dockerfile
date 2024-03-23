FROM python:3.10.14

WORKDIR /references_service

COPY requirements.txt /references_service/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --user -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
