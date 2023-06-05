FROM python:3 

WORKDIR /API

COPY . .

CMD [ "python","API/scrpyNews/scrpyNews/__init__.py"]