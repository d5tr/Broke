#!/bin/bash

#!/bin/bash

WHO=$(whoami)

if [ $WHO == root ]
then

cd /root/Broke && sudo python3 Broke.py

else

echo 'you must be root ! '
echo 'use sudo'

fi
