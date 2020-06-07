FROM python:3.8.3-alpine

run apk add python3-dev ffmpeg git openssl libffi-dev libsodium-dev g++ make bash opus opus-tools ffmpeg-libs opusfile opus-dev libopusenc libopusenc-dev

COPY requirements.txt /

RUN pip3 install -r requirements.txt
