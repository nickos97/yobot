FROM python:3.9
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./ /code/app
ENV APIKEY "APIKEY"
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "3000"]
