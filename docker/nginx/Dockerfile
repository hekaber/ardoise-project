FROM nginx:stable-alpine

## Remove default Nginx website
RUN rm -rf /usr/share/nginx/html/*

COPY ./docker/nginx/nginx.conf /etc/nginx/nginx.conf
COPY ./ardoise-app/dist/ardoise-app /usr/share/nginx/html

RUN echo "mainFileName=\"\$(ls /usr/share/nginx/html/main*.js)\" && \
          envsubst '\$BACKEND_API_URL \$DEFAULT_LANGUAGE ' < \${mainFileName} > main.tmp && \
          mv main.tmp  \${mainFileName} && nginx -g 'daemon off;'" > run.sh

ENTRYPOINT ["sh", "run.sh"]
