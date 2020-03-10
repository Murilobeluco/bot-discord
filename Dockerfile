FROM murilobeluco/bot-discord:inicio

COPY requirements.txt /
 
RUN pip3 install -r requirements.txt

ENV TOKEN "NTc4MzY1NzYxOTI0NDk3NDI3.XmbiaA.C_22ptdJMUZcRG6nxAftBwzXEkI"

WORKDIR /bot-discord

CMD ["python3", "-u", "bot.py"]


