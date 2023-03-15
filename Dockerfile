FROM python:3.8-slim-buster

WORKDIR D:\Project\whole_sys

COPY requirements.txt .

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org install -r requirements.txt

COPY subtract.py .

EXPOSE 5000

CMD ["python", "subtract.py"]
