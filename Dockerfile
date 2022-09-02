FROM python:3.6.9
WORKDIR /Postgres
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY sql.py sql.py
CMD ["python3", "-u", "sql.py"]
