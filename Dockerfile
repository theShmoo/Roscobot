FROM python:3.8
ADD bot.py /
ADD .env /
RUN pip install requests \
        discord.py \
        python-dotenv
CMD [ "python", "./bot.py" ]
