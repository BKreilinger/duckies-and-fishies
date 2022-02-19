#!/bin/bash

is_arm="false"
set_arm="false"

while getopts an VAR
do
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

if [[ $set_arm == "true" ]]; then
	is_arm="false"

elif [[ $architecture =~ .*arm64.*  ]]; then
	architecture=$(uname -a)
	is_arm="true"
	echo "ARM is detected! Therefore another docker container will be built!"

fi

cd docker
docker-compose up -d ubuntu


if [[ $is_arm == "true"  ]]; then
	docker-compose up -d ubuntu-arm
	echo "You are now in the bash of the arm container!"
fi

docker-compose exec ubuntu bash

../scripts/test.sh
