FROM ubuntu:18.04

### SET UP ENVIRONMENT WITH TOOLS

RUN apt-get update && apt-get install -y zip unzip
RUN apt-get update && apt-get install -y vim

RUN apt-get update && apt-get install --no-install-recommends -y \
    git \
    sudo \
    wget \
    gdb \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Python SDK
RUN \
    apt-get update && \
    apt-get install -y python3 python-dev python3-pip python-virtualenv && \
    rm -rf /var/lib/apt/lists/*

### SET UP Virtual Studio Code-Server

# Reference Link: https://github.com/monostream/code-server/blob/develop/Dockerfile
RUN apt-get update && apt-get install --no-install-recommends -y \
    bsdtar \
    openssl \
    locales \
    net-tools \
    && rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8
ENV DISABLE_TELEMETRY true

ENV CODE_VERSION="1.903-vsc1.33.1"

RUN curl -sL https://github.com/codercom/code-server/releases/download/${CODE_VERSION}/code-server${CODE_VERSION}-linux-x64.tar.gz | tar --strip-components=1 -zx -C /usr/local/bin code-server${CODE_VERSION}-linux-x64/code-server

# Setup User
RUN groupadd -r coder \
    && useradd -m -r coder -g coder -s /bin/bash \
    && echo "coder ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/nopasswd
USER coder

# Setup User Visual Studio Code Extentions
ENV VSCODE_USER "/home/coder/.local/share/code-server/User"
ENV VSCODE_EXTENSIONS "/home/coder/.local/share/code-server/extensions"

RUN mkdir -p ${VSCODE_USER}

# Setup Python Extension
RUN mkdir -p ${VSCODE_EXTENSIONS}/python \
    && curl -JLs --retry 5 https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/latest/vspackage | bsdtar --strip-components=1 -xf - -C ${VSCODE_EXTENSIONS}/python extension

COPY index.html /home/travis/build/codercom/code-server/packages/server/build/web/

COPY --chown=coder:coder settings.json /home/coder/.local/share/code-server/User/

# Setup User Workspace
RUN mkdir -p /home/coder/project
WORKDIR /home/coder/project

USER root

#Setup the download code folder structure
RUN mkdir -p /root/download
RUN mkdir -p /root/download/public
WORKDIR /root/download

COPY ./download/public/index.html ./public/
COPY ./download/public/theme.css ./public/
COPY ./download/public/index.js ./public/
COPY ./download/public/desktop.jpg ./public/

WORKDIR /home/coder/project

#### SET UP NGINX

RUN apt-get update && apt-get install --no-install-recommends -y \
    nginx

VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

COPY reverse-proxy.conf /etc/nginx/sites-enabled

VOLUME /home/coder/project/

# Prepend FROM base-image
USER root

# Add submit button, copy for each version of python in the kernel
COPY coursera /tmp/coursera
RUN for d in $(ls $CONDA_DIR/lib | grep "^python*") ; do cp -r /tmp/coursera $CONDA_DIR/lib/$d; done

COPY nbextensions/submit-button $CONDA_DIR/share/jupyter/nbextensions/submit-button
RUN jupyter nbextension install $CONDA_DIR/share/jupyter/nbextensions/submit-button && \
    jupyter nbextension enable submit-button/main

COPY .jupyter/ /home/$NB_USER/.jupyter/
RUN fix-permissions /home/$NB_USER/.jupyter
ENV PYTHONWARNINGS ignore

# Set entry point
EXPOSE 8888
WORKDIR /home/$NB_USER/work
ENTRYPOINT ["tini", "--"]
CMD ["start-notebook.sh"]

USER $NB_USER
