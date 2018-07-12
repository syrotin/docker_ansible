FROM mysql:5.7

# default replication user and pass
ENV REPLICATION_USER replica
ENV REPLICATION_PASSWORD 123456

COPY core/replication-entrypoint.sh /usr/local/bin/
COPY core/init-slave.sh /

RUN chmod +x /usr/local/bin/replication-entrypoint.sh
ENTRYPOINT ["/usr/local/bin/replication-entrypoint.sh"]

CMD ["mysqld"]
