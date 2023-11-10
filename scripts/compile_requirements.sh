#!/usr/bin/env bash
#
# Pin current dependencies versions.
#

rm -f requirements.txt
rm -f requirements.dev.txt

# pin test / lint / docs dependencies for reproducibility
pip-compile requirements.dev.in

# pin requirements.in versions just as reference for potential incapability bugs in future
pip-compile requirements.in

# do not pin dependencies in the package
scripts/include_pyproject_requirements.py requirements.in
