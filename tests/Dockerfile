FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip install requests

ENV LOG 1

ADD predictions_test.py /tests/predictions_test.py

WORKDIR /authentication/

CMD python3 test_authentication.py
