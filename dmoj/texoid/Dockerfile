FROM python:3.11-slim-bookworm

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        texlive-binaries texlive-latex-base texlive-latex-extra texlive-latex-recommended \
        texlive-pictures texlive-pstricks librsvg2-bin xxd imagemagick dvisvgm git && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/DMOJ/texoid/
WORKDIR /texoid/
RUN pip3 install -e .

EXPOSE 8888
ENTRYPOINT texoid --address=texoid --port=8888
