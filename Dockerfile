FROM python
RUN apt-get update
ENV PYTHONUNBUFFERED 1
RUN mkdir /repo
WORKDIR /repo
ADD . /repo/
RUN pip install -r requirement.txt
EXPOSE 8000

