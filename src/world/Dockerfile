FROM golang:1.11-alpine

COPY world.go /app/world.go

WORKDIR /app

RUN apk add curl

ENTRYPOINT go run world.go