FROM debian:latest

RUN apt-get update && apt-get install python3-pip -y && pip install requests

ENV LOG 1

ADD prediction_tests.py /Docker/prediction_tests.py

ADD strokes_for_prediction.csv strokes_for_prediction.txt ./Docker/

WORKDIR /Docker/

CMD python3 prediction_tests.py
