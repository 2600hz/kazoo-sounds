#!/bin/bash

pushd $(dirname $0) > /dev/null

not_found=0

while read i
do
    FILENAME=`echo $i | cut -d':' -f1`;
    if [ -z "${FILENAME}" ]
    then
  	continue
    fi

    for DIR in `find . -mindepth 2 -type d`
    do
	if [ $(ls ${DIR}/${FILENAME}* 2>/dev/null | wc -w) -lt 1 ]
	then
	    echo ${DIR}/${FILENAME}
            ((++not_found))
	fi
    done

done < prompts.txt

popd > /dev/null

[[ $not_found > 0 ]]; echo "Found $not_found missing prompts"
exit $not_found
