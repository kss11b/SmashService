FROM python:3.4-alpine
ADD . /code
WORKDIR /code
EXPOSE 8080
RUN pip install -r requirements.txt
CMD ["python", "server.py"]
