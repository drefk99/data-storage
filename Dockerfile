FROM centos:latest

RUN yum -y update && yum -y install httpd

EXPOSE 80
EXPOSE 443

CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]
