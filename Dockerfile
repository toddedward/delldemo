FROM python:3.9
WORKDIR /Users/toddsperry/code
COPY ./requirements.txt /Users/toddsperry/code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /Users/toddsperry/code/requirements.txt
COPY ./app /Users/toddsperry/code/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

