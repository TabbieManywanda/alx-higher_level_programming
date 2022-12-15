#!/bin/bash
#Only status code
curl -slw "%{http_code}" -o /dev/null "${1}"
