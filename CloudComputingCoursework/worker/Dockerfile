FROM python:3

EXPOSE 9000:9000

RUN mkdir -p /CC/CC/worker/volume
RUN mkdir -p /CC/CC/repo_descargas/

# RUN apt-get install ca-certificates curl gnupg lsb-release
# RUN mkdir -p /etc/apt/keyrings
# RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
# RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
# RUN apt-get update
# RUN chmod a+r /etc/apt/keyrings/docker.gpg
# RUN apt-get update
# RUN apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

WORKDIR /CC/CC/worker/
