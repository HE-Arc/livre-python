#!/bin/sh

set -xe

pycodestyle source
pydocstyle source
isort --check-only --diff --recursive source
sphinx-build -Wn -b html source target/doc/build
