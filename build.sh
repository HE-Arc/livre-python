#!/bin/sh

set -xe

pycodestyle source
pydocstyle source
isort --check-only --diff --recursive source
find source -iname "*.rst" | xargs rstcheck --report 2
sphinx-build -Wn -b html source target/doc/build
