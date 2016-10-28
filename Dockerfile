MAINTAINER https://github.com/AlbertoPuig
FROM python:2.7
COPY t2f /usr
RUN pip2 install httplib2 --upgrade
RUN chmod 777 /usr/t2f.py
CMD ["python","/usr/t2f.py"]
