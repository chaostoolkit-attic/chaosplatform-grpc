#!/bin/bash
set -eo pipefail

function generate () {
    echo "Checking the code syntax"
    
}

function main () {
    generate || return 1
}

main "$@" || exit 1
exit 0