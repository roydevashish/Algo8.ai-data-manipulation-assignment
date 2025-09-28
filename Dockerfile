FROM ubuntu:latest

RUN apt update && apt upgrade -y
RUN apt install python3-full -y
RUN apt install curl -y
RUN curl -LsSf https://astral.sh/uv/install.sh | sh