FROM python:alpine3.15

RUN apk update && apk add --no-cache jq
RUN pip install awscli

WORKDIR /script

COPY . .

CMD [ "" ]
