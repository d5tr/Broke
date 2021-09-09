#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root && rm -rf Broke
cd /bin && rm Broke

echo 'Done uninstall ...'

else
then

echo 'you must be root'
echo 'use sudo '

fi
