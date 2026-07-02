sudo dnf update -y
sudo dnf install -y docker
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user
sudo dnf install -y nginx
sudo systemctl start nginx
sudo systemctl enable nginx
exit
docker ps
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
ssh
tree
ls
ssh -i "gaialink-key.pem" ec2-user@172.30.2.59
docker
docker-container
docker-compose
docker-compose --version
ssh -i "gaialink-key.pem" ec2-user@172.30.2.59
ls -l gaialink-key.pem
chmod 600 gaialink-key.pem
ls -l gaialink-key.pem
ssh -i "gaialink-key.pem" ec2-user@172.30.2.59
docker
ping 8.8.8.8
curl http://172.30.2.100:5002
curl http://172.30.2.100:5002/health
curl http://172.30.2.59:5003/health
curl http://172.30.2.59:5005/health
curl http://172.30.2.59:5003/health
ping 8.8.8.8
cd gaialink
docker-compose up -d --build
cls
docker-compose up -d --build
cd gaialink
docker-compose up -d --build
docker-compose down
docker system prune -a -f
docker-compose up -d --build
clear
docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker-compose down
cd gaialink
docker-compose down
docker-compose up -d --build
docker ps
docker-compose up -d
clear
docker-compose up -d
clear
mkdir -p ~/.docker/cli-plugins
curl -Lo ~/.docker/cli-plugins/docker-buildx https://github.com/docker/buildx/releases/latest/download/docker-buildx-linux-amd64
chmod +x ~/.docker/cli-plugins/docker-buildx
docker buildx version
docker buildx versionls
ls
cd
mkdir -p ~/.docker/cli-plugins
curl -Lo ~/.docker/cli-plugins/docker-buildx https://github.com/docker/buildx/releases/latest/download/docker-buildx-linux-amd64
chmod +x ~/.docker/cli-plugins/docker-buildx
docker buildx version
clear
sudo dnf update -y docker
docker buildx version
ping 8.8.8.8
clear
cd gaialink
docker build -t gaialink-api ./APIsudo rm /usr/local/bin/docker-compose
sudo rm /usr/local/bin/docker-compose
curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
clear
sudo curl -SL https://github.com/docker/compose/releases/download/v2.27.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose version
docker-compose up -d --build
docker ps
curl http://localhost:5000/health
docker-
docker-compose logs api
docker-compose logs front
curl http://127.0.0.1:5009
curl http://127.0.0.1:5009/health
clear
docker-compose down
clear
docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker ps
curl http://127.0.0.1:5009/health
curl http://127.0.0.1:5000/health
curl http://127.0.0.1:5000/
cd gaialink
sudo nano /etc/nginx/conf.d/gaialink.conf
sudo nginx -t
sudo systemctl reload nginx
sudo nginx -t
curl http://127.0.0.1:5000/health
docker ps
clear
curl http://127.0.0.1:5000/health
docker logs api_service
curl http://127.0.0.1:5000/health
docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker-compose down
docker system prune -a -f
curl http://172.30.2.59:6379
curl http://172.30.2.59:5005
curl http://172.30.2.59:6379
clear
docker-compose up -d --build
cd gaialink
docker-compose up -d --build
docker ps
curl http://172.30.2.59:6379
curl http://127.0.0.1:5000/health
docker-compose down
docker system prune -a -f
clear
docker-compose up -d --build
cd gaialink
docker-compose up -d --build
curl http://127.0.0.1:5000/health
docker logs api_service
curl http://127.0.0.1:5000/health
sudo nano /etc/nginx/conf.d/gaialink.conf
sudo nginx -t
sudo systemctl reload nginx
docker logs api
docker ps
docker logs gaialink-api
cd gaialink
docker logs api
docker logs api_service
curl http://localhost:5008/health
curl http://127.0.0.1:5000/health
docker logs api_service
curl http:172.30.2.59//:5008/health
curl http://ort number was not a decimal:5000/health
curl http://172.30.2.59:5008/health
docker logs auth_service --tail 50
docker logs auth_service --tail 50api
docker logs api_service --tail 50api
clear
docker exec -it api_service curl http://172.30.2.59:5008/health
docker exec -it api_service wget -qO- http://172.30.2.59:5008/health
docker exec -it api_service python -c "import requests; print(requests.get('http://172.30.2.59:5008/health', timeout=5).text)"
docker logs api_service --tail 50api
truncate -s 0 $(docker inspect --format='{{.LogPath}}' auth_service)
truncate -s 0 $(docker inspect --format='{{.LogPath}}' api_service)
sudo truncate -s 0 $(docker inspect --format='{{.LogPath}}' api_service)
docker logs api_service --tail 50api
[ec2-user@ip-172-30-2-59 ~]$ docker logs auth_service
172.30.1.164 - - [15/May/2026 08:30:40] "POST /login HTTP/1.1" 200 -
docker logs api_service
docker-compose down
docker system prune -a -f
cd gaialink
docker system prune -a -f
docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker logs api_service
clear
docker logs api_service
sudo dnf install -y certbot python3-certbot-nginx
sudo certbot --nginx -d gaialink.online -d api.gaialink.online
cd gaialink
cd Microservices
docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker logs api_service
clear
cd gaialink
docker-compose down
docker-compose up -d --build
docker ps
docker logs api_services
docker logs api_service
cd gaialink
docker-compose up -d --build front
docker logs api_service
cd gaialink
docker-compose down
docker-compose up -d --build
docker logs api_service
ssh -i "gaialink-key.pem" ec2-user@ec2-44-199-249-81.compute-1.amazonaws.com
docker
docker --help
docker ps
nginx
sudo systemctl status nginx
sudo systemctl restart nginx
docker ps
curl http://localhost:5009
sudo nano /etc/nginx/conf.d/default.conf
sudo nginx -t
ls /etc/nginx/conf.d/
sudo nano /etc/nginx/conf.d/default.conf
sudo nano /etc/nginx/conf.d/gaialink.conf
docker ps
 docker-compose down gaialink-api
cd gaialinl
cd gaialink
 docker-compose down gaialink-api
 docker-compose down api
 docker-compose down
docker system prune -a -f
docker-compose up -d --build
docker ps
docker logs 
docker logs api
docker logs api-service
docker ps
docker logs api_service
docker ps
docker logs -f api_service
docker compose down
docker-compose down
docker-compose build --no-cache
docker compose up -d
docker-compose up -d
docker logs -f api_service
docker-compose down
docker-compose build --no-cache
docker-compose up -d
docker logs -f api_service
docker logs -f front_service
clear
docker logs -f api_service
docker exec -it api_service sh
clear
docker-compose down
docker-compose build --no-cache
docker-compose up -d
docker logs -f api_service
clear
docker-compose down
docker-compose build --no-cache
docker-compose up -d
docker logs -f api_service
clear
docker-compose down
docker-compose build --no-cache
docker-compose up -d
docker ps
sudo systemctl status nginx
sudo nginx -T
clear
sudo nano /etc/nginx/conf.d/gaialink.conf
sudo nginx -t
sudo systemctl reload nginx
sudo systemctl status nginx
sudo systemctl reload nginx
sudo systemctl status nginx
clear
