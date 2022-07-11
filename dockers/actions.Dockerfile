FROM rasa/rasa-sdk:3.0.2
WORKDIR /app
USER root
RUN python3 -m pip install pymongo 
RUN python3 -m pip install "pymongo[srv]"
COPY ./actions /app/actions
USER 1001
EXPOSE 5055