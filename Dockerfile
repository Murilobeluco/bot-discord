FROM murilobeluco/bot-discord:inicio

COPY requirements.txt /

RUN pip3 install -r requirements.txt
