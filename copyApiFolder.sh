#! /bin/sh
cd API-CODE/mAdvisorStgAPIUI/API_DOCKER
docker build -t $REPOSITORY_URI_API:latest .
docker tag $REPOSITORY_URI_API:latest $REPOSITORY_URI_API:$IMAGE_TAG_API
$(aws ecr get-login --region us-west-1 --no-include-email) 
docker push $REPOSITORY_URI_API:$IMAGE_TAG_API
cd ../../../