FROM minio/minio
EXPOSE 9000
EXPOSE 9001
WORKDIR /
RUN curl https://dl.min.io/client/mc/release/linux-amd64/mc --create-dirs -o /minio-binaries/mc
RUN chmod +x /minio-binaries/mc
ENV PATH=$PATH:/minio-binaries/
CMD ["minio", "server", "/cc/minio/volume/"]
