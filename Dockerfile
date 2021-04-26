FROM python:3.8.6-slim-buster
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
EXPOSE 8001
CMD ["python", "counter.py"]
