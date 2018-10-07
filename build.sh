#!/bin/sh

set -xe

pycodestyle source
pydocstyle --add-ignore=D401 source
isort --check-only --diff --recursive source
flake8 source
rstcheck \
        --recursive source \
        --ignore-directives sphinx,automodule,autoclass,autofunction,bibliography \
        --ignore-roles cite \
        --report warning

sphinx-build -Wn -b html source target/doc/build
