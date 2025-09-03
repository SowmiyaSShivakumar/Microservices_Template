FROM apache/apisix:latest
COPY config/apisix-config.yaml /usr/local/apisix/conf/config.yaml
ENTRYPOINT ["/apisix/bin/apisix", "init"]
CMD ["start"]