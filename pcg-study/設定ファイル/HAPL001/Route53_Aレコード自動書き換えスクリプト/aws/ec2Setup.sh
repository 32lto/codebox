#!/bin/sh
APPPATH=/var/config/aws/
ZONEID="Z05106306OUV1PE3U4Z8"
export AWS_CONFIG_FILE=/var/config/aws/settings.conf
IP=`/usr/bin/curl -s http://169.254.169.254/latest/meta-data/public-ipv4`
sed -e "s/{%IP%}/${IP}/g" ${APPPATH}dyndns.tmpl > ${APPPATH}SetDNS.json
aws route53 change-resource-record-sets --hosted-zone-id ${ZONEID} --change-batch file://${APPPATH}SetDNS.json
exit
