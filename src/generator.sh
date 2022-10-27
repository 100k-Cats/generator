#!/bin/bash
# $1 = ENS

CUR_DIR=$(pwd)$'/src/'
WORK_DIR=$(pwd)$'/dist/png/'
REPO=$(pwd)$'/src/layers/ALL/'

NEW=$(python3 $CUR_DIR"rarity.py" $1)
IFS='+' read -ra ADDR <<< "$NEW"
read -a INDEX <<< "${ADDR[0]}"
read -a LAYER <<< "${ADDR[1]}"
read -a TRAIT <<< "${ADDR[2]}"
LEN=${#INDEX[@]}
FILE_STR=''
for (( i=0; i<$LEN; i++ )); do
  if [[ "$FILE_STR" == '' && "${LAYER[$i]}" != "-" ]]; then
    cp $REPO${INDEX[$i]}-${LAYER[$i]}.png $WORK_DIR$1.png
    FILE_STR='INIT'
  fi
  if [[ "$FILE_STR" != '' && "${LAYER[$i]}" != "-" ]]; then
    FILE_STR=$REPO${INDEX[$i]}-${LAYER[$i]}.png
    convert $WORK_DIR$1.png $FILE_STR -gravity center -composite $WORK_DIR$1.png
  fi
done

PIN=$(ipfs add -n $WORK_DIR$1.png)
CID=$(echo $PIN | awk '{ print $2 }')
echo $CID'+'${TRAIT[@]}
