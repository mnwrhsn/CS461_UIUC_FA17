#!/bin/bash -e

netid=hckuo2
python tweakedCertbuilder.py $netid template.cer # generate tempate certificate and write prefix to prefix.cer
IV=$(openssl dgst -md5 prefix.cer | awk '{print $2}') # compute md5(prefix) as inital vector to produce collisions with fastcoll
echo $IV
./fastcoll -p prefix.cer -o b1temp b2temp
dd bs=1 count=128 skip=192 if=b1temp of=b1file
dd bs=1 count=128 skip=192 if=b2temp of=b2file
rm -f template.cer b1temp b2temp

