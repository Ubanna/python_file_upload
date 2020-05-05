# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8.2
COPY . /web
WORKDIR /web
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["web.py"]
