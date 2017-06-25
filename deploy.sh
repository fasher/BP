#!/bin/sh

show_help() {
  cat <<EOM
  Usage: deploy.sh -a <app_name>|all

    -a app_name to deploy or all for all apps, defaults to all if no argument given

EOM
}


app="all"
while getopts "ha:" opt; do
  case "$opt" in
    h)
      show_help
      exit 0
      ;;
    a) app=$OPTARG
  esac
done

if [ "$app" = "all" ]; then
  ansible-playbook -i dev/hosts base.yml 
else 
  ansible-playbook -i dev/hosts base.yml --tags $app
fi
