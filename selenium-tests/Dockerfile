FROM python:3.11-slim

WORKDIR /tests

COPY requirements.txt /tests/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /tests/

CMD ["pytest", "-v", "tests/test_ui.py"]
