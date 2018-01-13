FROM python:3.7.0a4-alpine3.7



COPY . ./
RUN pip install -r /requirements.txt

CMD python ./elasticsearch_cleanup.py
