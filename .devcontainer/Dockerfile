
FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

# Remove broken Yarn repository before features run
RUN rm -f /etc/apt/sources.list.d/yarn.list

RUN apt-get update
