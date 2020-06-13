#!/bin/sh
set -e

exec {{ cookiecutter.package_name }} "$@"
