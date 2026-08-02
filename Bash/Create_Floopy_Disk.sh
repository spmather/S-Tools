#!/bin/bash

mkdir ~/mountpoints
mkdir ~/mountpoints/floppy

dd if=/dev/zero of=floppy.img bs=1440k count=1
mkdosfs floppy.img
sudo mount -o loop floppy.img ~/mountpoints/floppy

# fin
