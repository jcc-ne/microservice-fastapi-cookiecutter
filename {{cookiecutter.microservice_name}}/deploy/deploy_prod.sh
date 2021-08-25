#! /bin/sh
#
# depoy_prod.sh
# Copyright (C) 2021 janine <janine@MacBook-Pro.local>
#
# Distributed under terms of the GNU GPLv3 license.
#


DIR=$(dirname $(python -c 'import os,sys;print(os.path.realpath(sys.argv[1]))' $0))
my_cwd=$PWD

if [ ! $DIR = $PWD ]; then
   echo "need to execute the script from $DIR"
   echo "*** moving to working directory *** "
   echo
   cd $DIR
fi

app_yaml="app.prod.yaml"

echo "######### quick view: $app_yaml ####################"
head -5 "../app_pkg/$app_yaml"
echo "####################################################"

confirm_deploy_using_app_yaml() {
    read -p "we are deploying using $app_yaml.  To confirm: type '$app_yaml': " input
    if [ $input != $app_yaml ];then
        confirm_deploy_using_app_yaml
    fi
}

confirm_deploy_using_app_yaml

echo "Deploying using: $app_yaml...($(date +%T))"

cd ../app_pkg
gcloud app deploy $app_yaml

echo "Done Deploying using: $app_yaml. ($(date +%T))"

cd $my_cwd
