#!/usr/bin/env bash
docker run -it --rm --name test \
-p 127.0.0.1:8888:8000 uol-awd:latest
