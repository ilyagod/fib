FROM python:3.11-slim-buster

COPY --chown=www-data:www-data app/build/ /var/app/build
RUN cd /var/app/ && pip install -r build/requirements.txt

VOLUME /var/app/
EXPOSE 8000
WORKDIR /var/app/src/

COPY --chown=www-data:www-data ci/scripts/* /

CMD ["/entrypoint.sh"]
