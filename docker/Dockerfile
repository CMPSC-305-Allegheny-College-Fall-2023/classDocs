FROM ubuntu:22.04
RUN apt-get update && apt-get -y install git htop vim python3 python3-pip sqlite

COPY requirements.txt ./requirements.txt

RUN \
pip3 install -r requirements.txt


WORKDIR /root/
	ENV LC_ALL=C.UTF-8
	ENV LANG=C.UTF-8

RUN mkdir -p /root/.streamlit

RUN bash -c 'echo -e "\
	[general]\n\
	email = \"\"\n\
	" > /root/.streamlit/credentials.toml'

RUN bash -c 'echo -e "\
	[server]\n\
	enableCORS = false\n\
	" > /root/.streamlit/config.toml'

# EXPOSE 8000

# Note: below port configuration instruction for Django.
# Run Django server after building the site: 
# `django-admin startproject mysite`
# `cd mysite`
# `python3 manage.py runserver 0.0.0.0:8501`

EXPOSE 8501

CMD ["bash"]
