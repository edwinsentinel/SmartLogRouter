FROM python:3.10-slim
WORKDIR /app
COPY main.py requirements.txt ./
RUN pip install -r requirements.txt
RUN mkdir /logs
VOLUME /logs
CMD ["python", "main.py"]
