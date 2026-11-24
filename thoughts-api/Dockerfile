FROM python:3.11-alpine
WORKDIR /opt/code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV APP_VERSION=v2
EXPOSE 8000
CMD ["python", "app.py"]
