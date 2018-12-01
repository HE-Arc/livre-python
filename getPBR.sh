#!/bin/bash

set -xe

cd source/pbr

rm -f index.rst

pbr_dir="Publishing-to-PyPI-with-pbr-and-Travis"
git clone https://github.com/73VW/${pbr_dir}.git
cp $pbr_dir/docs/main.rst index.rst
cp $pbr_dir/docs/_static/*.PNG ../_static
sed -E -i "s/\.\. image:: /.. image:: ..\//g" index.rst
rm -rf $pbr_dir

(cat note.rst; echo) >> index.rst
echo '.. _`Maël Pedretti`: https://github.com/73VW/Publishing-to-PyPI-with-pbr-and-Travis' >> index.rst
rm -f note.rst
cd ../..
