FROM debian:latest

ADD main.py data_preprocess.py requirements.txt strokes_for_prediction.csv strokes_for_prediction.txt schemas.py lr_best_classifier.pkl rf_best_classifier.pkl ./


RUN apt-get update && apt-get install python3-pip -y && pip install -r ./requirements.txt

EXPOSE 8000

CMD uvicorn main:app --host '0.0.0.0' --port 8000
