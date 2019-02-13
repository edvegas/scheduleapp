FROM python:3.6

RUN mkdir -p /web/scheduleweb
COPY . /web/scheduleweb
WORKDIR /web/scheduleweb
RUN pip install --upgrade pip && pip install -r requirements.txt
