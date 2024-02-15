FROM python:3.10

WORKDIR /opt/app
COPY . .

RUN pip3 install -r requirements.txt

CMD [ "tail","-f","/dev/null" ]