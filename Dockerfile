FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
	&& pip install -r requirements.txt

COPY . .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
    
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]