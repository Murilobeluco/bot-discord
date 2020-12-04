FROM python:3.9.0-alpine3.12

run apk add ffmpeg libffi-dev libsodium-dev g++ make bash opus opus-tools ffmpeg-libs opusfile opus-dev libopusenc libopusenc-dev

COPY requirements.txt /

RUN pip3 install -r requirements.txt
