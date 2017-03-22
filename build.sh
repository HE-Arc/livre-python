#!/bin/sh

set -xe

pycodestyle source
pydocstyle source
isort --check-only --diff --recursive source
rstcheck source/index.rst
sphinx-build -Wn -b html source target/doc/build
