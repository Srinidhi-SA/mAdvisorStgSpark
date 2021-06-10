#! /bin/sh
cd API_CODE/mAdvisorStgAPIUI/NGINX_DOCKER
docker build -t $REPOSITORY_URI_NGINX:latest .
docker tag $REPOSITORY_URI_NGINX:latest $REPOSITORY_URI_NGINX:$IMAGE_TAG_NGINX
$(aws ecr get-login --region us-west-1 --no-include-email) 
docker push $REPOSITORY_URI_NGINX:$IMAGE_TAG_NGINX
cd ../../../