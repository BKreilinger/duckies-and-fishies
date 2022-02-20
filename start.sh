#!/bin/bash

is_arm="false"
set_arm="false"

while getopts an VAR; do
  case $VAR in
  a)
    is_arm="true"
    ;;
  n)
    set_arm="true"
    ;;
  esac
done

echo "options:

	-a	builds a second docker container which can run the linear programming calculations on arm
	-n	force not building second container in case the problem is fixed in the future
"

architecture=$(uname -a)

if [[ $set_arm == "true" ]]; then
  is_arm="false"

elif [[ $architecture =~ .*arm64.* ]]; then
  is_arm="true"
  echo "ARM is detected! Therefore another docker container will be built!"

fi

cd docker
docker-compose up -d ubuntu

docker-compose exec ubuntu "./scripts/dispatcher/dispatcher.sh"

if [[ $is_arm == "true" ]]; then
  docker-compose up -d ubuntu-arm
  docker-compose exec ubuntu "./scripts/dispatcher/dispatcher_arm.sh"
fi

docker-compose exec ubuntu bash
