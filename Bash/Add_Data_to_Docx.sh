#!/bin/bash
# spmather
# requires 7zip
# 2026-08-18

echo "input a path to a docx file"
read docxpath
onlyhuman=""
for number in {1..524288}
do
    onlyhuman+="0"
done
echo $onlyhuman >> ./onlyhuman
7z a $docxpath ./onlyhuman
rm ./onlyhuman

# fin
