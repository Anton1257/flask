FROM python:3.8-alpine
RUN apk add --no-cache gcc musl-dev linux-headers
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
COPY . /code/
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
CMD ["python", "run.py"]