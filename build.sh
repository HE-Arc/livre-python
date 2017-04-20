#!/bin/sh

set -xe

pycodestyle source
pydocstyle --add-ignore=D401 source
isort --check-only --diff --recursive source
flake8 source
find source -iname "*.rst" \
    | xargs rstcheck \
        --ignore-directives sphinx,automodule,autoclass,autofunction \
        --report 2
sphinx-build -Wn -b html source target/doc/build
