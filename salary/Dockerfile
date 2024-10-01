FROM centos:latest

RUN cd /etc/yum.repos.d/ && sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-* && yum install python3 -y && pip3 install pandas && pip3 install scikit-learn

COPY salary_data.csv /
COPY salaryPredict.py /

ENTRYPOINT ["python3", "/salaryPredict.py"]

CMD ["0"]
