FROM ubuntu AS mvc-test
WORKDIR /app
COPY ./init.sh .
COPY ./requirements.txt .
COPY ./local.env .
COPY ./entrypoint.sh .
COPY ./njmvc_checker.zip .
RUN ["chmod", "u+x", "./init.sh"]
RUN ./init.sh
# RUN ["chmod", "u+x", "./entrypoint.sh"]
# RUN ./entrypoint.sh
# CMD ["tail", "-f", "/dev/null"]
