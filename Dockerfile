FROM alpine:3.19

RUN apk update && apk upgrade
RUN apk add make texlive texmf-dist-pictures
RUN apk add texmf-dist-publishers texmf-dist-science texmf-dist-fontsextra texmf-dist-latexextra
RUN apk add biber texmf-dist-bibtexextra
RUN apk add python3 py3-pip
RUN apk add inkscape
RUN pip install pymupdf --break-system-packages

# The 'bbm' package insists on generating stuff in the home directory. In
# order to guarantee access to the home directory no matter the user the
# docker container is run with, create a temporary one anyone can write to
RUN mkdir /tmp/home
RUN chmod -R 777 /tmp/home
ENV HOME=/tmp/home
