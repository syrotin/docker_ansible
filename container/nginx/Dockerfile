FROM nginx:latest

COPY default.conf /etc/nginx/conf.d
COPY fastcgi.conf /etc/nginx/
COPY fastcgi-php.conf /etc/nginx/

EXPOSE 80

STOPSIGNAL SIGTERM

CMD ["nginx", "-g", "daemon off;"]
