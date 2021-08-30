FROM python:3.8-alpine

WORKDIR /offerzen-assessment

COPY . /offerzen-assessment/

RUN pip install -r requirements.txt

CMD python autorun.py