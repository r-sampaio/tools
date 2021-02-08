#!/bin/bash
if [ "$1" == "" ]
then
	echo" Usage: $0 site ext "
else
lynx --dump "https://www.google.com/search?&q=site:$1+ext:$2" | grep ".$2" | cut -d "=" -f 2 | egrep -v "site|google" | sed 's/...$//' > file
for url in $(cat file)
do
wget -q $url
done
exiftool *.$2
rm *.$2 file
fi