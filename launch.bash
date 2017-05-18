#!/bin/bash

# Router credentials
export routerAddress="<YOUR ROUTER ADDRESS>"
export routerUsername="<YOUR ROUTER USERNAME>"
export routerPassword="<YOUR ROUTER PASSWORD>"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR

`which python3` python/check.py
