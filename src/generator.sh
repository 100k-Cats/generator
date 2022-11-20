#!/bin/bash
# $1 = ENS

CUR_DIR=$(pwd)$'/src/'
WORK_DIR=$(pwd)$'/dist/png/'
REPO=$(pwd)$'/src/layers/ALL/'

CONSTS=('16180' '29979' '27182' '31415' '66260' '66730')
VALUES=("Golden Ratio" "Speed of Light" "Euler\'s number" "Pi" "Planck's Constant" "Gravitational Constant")

ONES=('00001' '2' '3' '4' '5' '6' '7' '8' '9' '10' '11')
MAPS=('BoredTown' 'DomainPlug' 'ENSMaxis' 'ENSVision' 'ETHmojiPunks' 'ETHNerd' 'ETHonART' 'n0vax' 'sshmatrix' 'Animakami' 'BENSYC')

# COMPILE TRAITS

# FUNDAMENTAL CONSTANTS
count=0
for item in ${CONSTS[@]}; do
  if [ "$1" == "$item" ]; then
    convert $REPO${1}_.png $REPO${1}.png -gravity center -composite $WORK_DIR$1.png
    PIN=$(ipfs add -n $WORK_DIR$1.png)
    CID=$(echo $PIN | awk '{ print $2 }')
    echo $CID'+-+'${VALUES[$count]}'+-'
    exit
  fi
  count=$((count + 1))
done
# EASTER EGGS
count=0
for item in ${ONES[@]}; do
  if [ "$1" == "$item" ]; then
    convert $REPO${MAPS[$count]}_.png $REPO${MAPS[$count]}.png -gravity center -composite $WORK_DIR$1.png
    PIN=$(ipfs add -n $WORK_DIR$1.png)
    CID=$(echo $PIN | awk '{ print $2 }')
    echo $CID'+-+'${MAPS[$count]}'+-'
    exit
  fi
  count=$((count + 1))
done

# REMAINING DIGITS
NEW=$(python3 $CUR_DIR"rarity.py" $1)
IFS='+' read -ra ADDR <<< "$NEW"
read -a INDEX <<< "${ADDR[0]}"
read -a LAYER <<< "${ADDR[1]}"
read -a TRAIT <<< "${ADDR[2]}"
read -a VALUE <<< "${ADDR[3]}"
read -a NAMES <<< "${ADDR[4]}"
LEN=${#INDEX[@]}
FILE_STR=''
for (( i=0; i<$LEN; i++ )); do
  if [[ $i -eq 0 && "${LAYER[$i]}" != "-" ]]; then
    cp $REPO${INDEX[$i]}-${LAYER[$i]}.png $WORK_DIR$1.png
    FILE_STR='BG'
  fi
  if [[ $i -eq 1 && "${LAYER[$i]}" != "-" ]]; then
    # compile digits
    DIG=($(echo "$1" | grep -o .))
    DIG1=$REPO"${LAYER[$i]}${DIG[0]}----.png"
    DIG2=$REPO"${LAYER[$i]}-${DIG[1]}---.png"
    DIG3=$REPO"${LAYER[$i]}--${DIG[2]}--.png"
    DIG4=$REPO"${LAYER[$i]}---${DIG[3]}-.png"
    DIG5=$REPO"${LAYER[$i]}----${DIG[4]}.png"
    convert $DIG1 $DIG2 -gravity center -composite $WORK_DIR$1_.png
    convert $WORK_DIR$1_.png $DIG3 -gravity center -composite $WORK_DIR$1_.png
    convert $WORK_DIR$1_.png $DIG4 -gravity center -composite $WORK_DIR$1_.png
    convert $WORK_DIR$1_.png $DIG5 -gravity center -composite $WORK_DIR$1_.png
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
echo $CID'+'${TRAIT[@]}'+'${VALUE[@]}'+'${NAMES[@]}
