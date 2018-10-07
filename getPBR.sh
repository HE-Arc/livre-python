#!/bin/bash

set -xe

cd source/pbr

rm -f index.rst

pbr_dir="Publishing-to-PyPI-with-pbr-and-Travis"
git clone https://github.com/73VW/${pbr_dir}.git
mv $pbr_dir/*.rst .
mv $pbr_dir/*.PNG ../_static
sed -E -i "s/\.\. image:: (.*\.*)/.. image:: ..\/_static\/\1/g" README.rst
rm -rf $pbr_dir

for f in note.rst README.rst; do (cat "${f}"; echo) >> index.rst; done
echo '.. _`Maël Pedretti`: https://github.com/73VW/Publishing-to-PyPI-with-pbr-and-Travis' >> index.rst
rm -f note.rst
rm -f README.rst
cd ../..
