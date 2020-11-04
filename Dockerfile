FROM ubuntu:18.04

### SET UP ENVIRONMENT WITH TOOLS

RUN apt-get update && apt-get install -y zip unzip
RUN apt-get update && apt-get install -y vim
RUN apt-get update && apt-get install -y supervisor
RUN mkdir -p /var/log/supervisor

RUN DEBIAN_FRONTEND=noninteractive TZ="America/New_York" apt-get -y install tzdata

RUN apt-get update && apt-get install --no-install-recommends -y \
    git \
    sudo \
    wget \
    gdb \
    build-essential \
    curl \
    postgresql \
    postgresql-client \
    postgresql-contrib \
    postgresql-server-dev-all \
    openjdk-8-jre \
    maven \
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
COPY settings.json /root/.local/share/code-server/User/

RUN mkdir -p ${VSCODE_USER}

# Setup Python Extension
RUN mkdir -p ${VSCODE_EXTENSIONS}/python \
   && curl -JLs --retry 5 https://github.com/microsoft/vscode-python/releases/download/2020.5.80290/ms-python-release.vsix | bsdtar --strip-components=1 -xf - -C ${VSCODE_EXTENSIONS}/python extension

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


RUN pip3 install virtualenvwrapper
ENV VIRTUALENVWRAPPER_PYTHON /usr/bin/python3
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;  mkvirtualenv -p /usr/bin/python3 advanced_web_dev"
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;  workon advanced_web_dev; pip install django==3.0.3; pip install psycopg2; pip install djangorestframework; pip install factory_boy; pip install django-bootstrap4; pip install channels"
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh;  workon advanced_web_dev; pip install channels-redis; pip install celery[redis]; pip install Pillow; pip install redis; pip install requests; pip install pyyaml; pip install uritemplate"

RUN echo 'export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3' >> ~/.bashrc
# RUN echo 'export WORKON_HOME=/home/coder/project/envs' >> ~/.bashrc
RUN echo 'source /usr/local/bin/virtualenvwrapper.sh 2> /dev/null' >> ~/.bashrc
RUN echo 'export LANGUAGE=en_US.UTF-8' >> ~/.bashrc
RUN echo 'export LANG=en_US.UTF-8' >> ~/.bashrc
RUN echo 'export LC_ALL=en_US.UTF-8' >> ~/.bashrc
RUN echo 'export C_FORCE_ROOT=True' >> ~/.bashrc
RUN echo 'export C_FORCE_ROOT=True' >> /home/coder/.bashrc
RUN echo 'export LANGUAGE=en_US.UTF-8' >> /home/coder/.bashrc
RUN echo 'export LANG=en_US.UTF-8' >> /home/coder/.bashrc
RUN echo 'export LC_ALL=en_US.UTF-8' >> /home/coder/.bashrc
RUN echo 'en_US.UTF-8 UTF-8' > /etc/locale.gen
RUN echo 'fs.inotify.max_user_watches=524288' >> /etc/sysctl.conf
RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure --frontend noninteractive locales
RUN echo 'if [ ! -d /home/coder/project/django_databases ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases"; runuser -l  coder -c "cp -r /home/coder/project/tmp_db/* /home/coder/project/django_databases/"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_commit_ts ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_commit_ts 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_dynshmem ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_dynshmem 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_replslot ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_replslot 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_serial ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_serial 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_snapshots ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_snapshots 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_stat ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_stat 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_stat_tmp ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_stat_tmp 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_tblspc ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_tblspc 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_twophase ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_twophase 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_logical ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_logical 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_logical/mappings ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_logical/mappings 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'if [ ! -d /home/coder/project/django_databases/pg_logical/snapshots ]; then runuser -l  coder -c "mkdir /home/coder/project/django_databases/pg_logical/snapshots 2> /dev/null"; fi' >> ~/.bashrc
RUN echo 'runuser -l  coder -c "chmod 0700 /home/coder/project/django_databases"' >> ~/.bashrc
RUN echo "chmod uog+rw /var/run/postgresql" >> ~/.bashrc
RUN echo 'runuser -l  coder -c "/usr/lib/postgresql/10/bin/postgres -D /home/coder/project/django_databases > /home/coder/project/django_databases/logfile 2>&1 &"' >> ~/.bashrc

WORKDIR /home/coder/project

#### SET UP NGINX

RUN apt-get update && apt-get install --no-install-recommends -y \
    nginx

VOLUME ["/etc/nginx/sites-enabled", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx", "/var/www/html"]

COPY reverse-proxy.conf /etc/nginx/sites-enabled

VOLUME /home/coder/project/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

### SET UP redis 5
COPY redis-5.0.9.tar.gz /root
WORKDIR /root
RUN tar -zxvf redis-5.0.9.tar.gz
WORKDIR /root/redis-5.0.9
RUN make
RUN make install
WORKDIR /root
RUN rm -rf redis-5.0.9/

WORKDIR /home/coder/project
