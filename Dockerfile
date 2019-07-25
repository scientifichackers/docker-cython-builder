# legacy ubuntu ensures libc version is compatible with almost every target distro
FROM ubuntu:12.04

# requirements from https://github.com/pyenv/pyenv/wiki
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
    wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

RUN apt-get install -y git

# install pyenv
RUN curl https://pyenv.run | bash

ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

RUN pyenv install 3.7.4