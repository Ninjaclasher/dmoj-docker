FROM dmoj-site-base:latest

COPY repo/ /site/
WORKDIR /site/
RUN mkdir /assets/
RUN bash make_style.sh && python3 manage.py collectstatic --noinput && \
    python3 manage.py compilemessages && python3 manage.py compilejsi18n
RUN cp -r resources /assets/ && \
    cp 502.html /assets/ && \
    cp logo.png /assets/ && \
    cp robots.txt /assets/
