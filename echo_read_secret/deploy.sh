#!/usr/bin/env bash

ENVIRONMENT="python"
FUNCTION="echo"

fission env get --name ${ENVIRONMENT} || fission env create --name ${ENVIRONMENT} --image gcr.io/beta-180508/${ENVIRONMENT}-env:latest

fission fn create --name ${FUNCTION} --env ${ENVIRONMENT} --code ./echo_read_secret.py

echo "this function will convert a JSON POST data to new JSON with a random risk added to it"
echo 
echo "To use it do:"
echo "  $ fission route create --method POST --url /${FUNCTION} --function ${FUNCTION}" 
echo "  $ curl -d '{\"id\":\"1234\", \"status\":\"new\", \"description\":\"this is cool\"}' \\"
echo "      -H 'Content-Type: application/json' \\"
echo "      -X POST http://$FISSION_ROUTER/${FUNCTION}"