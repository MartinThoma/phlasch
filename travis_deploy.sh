#!/bin/bash
docker tag "$DOCKER_USERNAME/$DOCKER_IMAGE" "$DOCKER_USERNAME/$DOCKER_IMAGE:$TRAVIS_TAG"
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker push "$DOCKER_USERNAME/$DOCKER_IMAGE"
