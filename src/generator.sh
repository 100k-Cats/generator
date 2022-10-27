#!/bin/bash
# $1 = ENS

CUR_DIR=$(pwd)$'/src/'
WORK_DIR=$(pwd)$'/dist/png/'
REPO=$(pwd)$'/src/layers/ALL/'

# compile digits
DIG=($(echo "$1" | grep -o .))
DIG1=$REPO"${DIG[0]}----.png"
DIG2=$REPO"-${DIG[1]}---.png"
DIG3=$REPO"--${DIG[2]}--.png"
DIG4=$REPO"---${DIG[3]}-.png"
DIG5=$REPO"----${DIG[4]}.png"
convert $DIG1 $DIG2 -gravity center -composite $WORK_DIR$1_.png
convert $WORK_DIR$1_.png $DIG3 -gravity center -composite $WORK_DIR$1_.png
convert $WORK_DIR$1_.png $DIG4 -gravity center -composite $WORK_DIR$1_.png
convert $WORK_DIR$1_.png $DIG5 -gravity center -composite $WORK_DIR$1_.png

# compile traits
NEW=$(python3 $CUR_DIR"rarity.py" $1)
IFS='+' read -ra ADDR <<< "$NEW"
read -a INDEX <<< "${ADDR[0]}"
read -a LAYER <<< "${ADDR[1]}"
read -a TRAIT <<< "${ADDR[2]}"
LEN=${#INDEX[@]}
FILE_STR=''
for (( i=0; i<$LEN; i++ )); do
  if [[ $i -eq 0 && "${LAYER[$i]}" != "-" ]]; then
    cp $REPO${INDEX[$i]}-${LAYER[$i]}.png $WORK_DIR$1.png
    FILE_STR='BG'
  fi
  if [[ $i -eq 1 && "${LAYER[$i]}" == "D" ]]; then
    convert $WORK_DIR$1.png $WORK_DIR$1_.png -gravity center -composite $WORK_DIR$1.png
    FILE_STR='ENS'
    rm $WORK_DIR$1_.png
  fi
  if [[ $i -gt 1 && "${LAYER[$i]}" != "-" ]]; then
    FILE_STR=$REPO${INDEX[$i]}-${LAYER[$i]}.png
    convert $WORK_DIR$1.png $FILE_STR -gravity center -composite $WORK_DIR$1.png
  fi
done

PIN=$(ipfs add -n $WORK_DIR$1.png)
CID=$(echo $PIN | awk '{ print $2 }')
echo $CID'+'${TRAIT[@]}
