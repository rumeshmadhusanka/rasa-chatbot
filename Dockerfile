FROM rasa/rasa:2.8.7

ARG PORT1=5005
ARG PORT2=5055

WORKDIR /app
COPY . /app

EXPOSE $PORT1
EXPOSE $PORT2

#RUN python3 -m pip install --upgrade pip
RUN pip install rasa-sdk==2.8.2
RUN pip install nltk

RUN rasa train

ENTRYPOINT ["rasa"]
CMD ["run"]
