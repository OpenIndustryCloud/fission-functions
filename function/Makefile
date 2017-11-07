.PHONY: deploy route clean

FUNCTION := echo
ENVIRONMENT := python
METHOD := POST

deploy: 
	fission fn create --name ${FUNCTION} --code echo.py --env ${ENVIRONMENT}

route: 
	fission route create --url /${FUNCTION} --method ${METHOD} --function ${FUNCTION}

clean: 
	fission fn delete --name ${FUNCTION} --env ${ENVIRONMENT}
	fission route list | grep ${FUNCTION} | grep ${METHOD} | grep ${FUNCTION} | awk '{ print $1 }' | xargs fission route delete