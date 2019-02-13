FROM nginx

COPY nginx.conf /etc/nginx/
COPY schedule.conf /etc/nginx/sites-available/

RUN mkdir -p /etc/nginx/sites-enabled/ \
    && ln -s /etc/nginx/sites-available/schedule.conf /etc/nginx/sites-enabled/schedule.conf \
    && rm -f /etc/nginx/conf.d/default.conf
