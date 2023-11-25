# syntax=docker/dockerfile:1
FROM python:3.9.18

ARG DEBIAN_FRONTEND=nointeractive

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt update && apt install -y git curl wget sudo mc && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Add a user developer with password dev123
RUN useradd -m -u 1000 -U -G sudo --system --password=$(openssl passwd -1 dev123) developer && \
    mkdir -p /home/developer/.local/bin && chown -R developer:developer /home/developer
# USER developer

CMD ["/bin/bash"]
