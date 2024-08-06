#!/bin/bash

set -e

# Build the app
echo "Building the app..."

# Read pyproject.toml to get the version without spaces
VERSION=$(cat pyproject.toml | grep version | cut -d " " -f3 | cut -d '"' -f 2)

echo "Version:$VERSION"

# Build the Docker image
docker build . -t "yohandiaz/to-do:$VERSION"

# Tag the Docker image
docker tag yohandiaz/to-do:$VERSION yohandiaz/to-do:latest

docker push yohandiaz/to-do:$VERSION
docker push yohandiaz/to-do:latest