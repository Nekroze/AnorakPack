SHELL := /bin/bash
PACKNAME=AnorakPack
VERSION=0.1.0
LITE=false
ifeq ($(LITE),false)
	PACKDIST=${PACKNAME}-${VERSION}
else
	PACKDIST=${PACKNAME}Lite-${VERSION}
endif
CLIENTZIP=releases/${PACKDIST}-client.zip
SERVERZIP=releases/${PACKDIST}-server.zip
PUBLIC=/cygdrive/g/Dropbox/Public/${notdir ${CLIENTZIP}}


.PHONY: clean client server push

all: ${CLIENTZIP} ${SERVERZIP}

client: ${CLIENTZIP}

server: ${SERVERZIP}

${CLIENTZIP}: build/client/bin/modpack.jar
	@mkdir -p releases
	@rm -rf $@
	cd build/client && zip -rq ../../$@ ./*

build/client/bin/modpack.jar: AnorakPack.py $(shell find components/data -print0 -type f)
	@rm -rf
	python $< ${LITE}

${SERVERZIP}: build/server/server.jar
	@mkdir -p releases
	@rm -rf $@
	cd build/server && zip -rq ../../$@ ./*

build/server/server.jar: ${CLIENTZIP}

# Push is an example for how to "upload" to a public location
push: ${PUBLIC}

${PUBLIC}: ${CLIENTZIP} ${SERVERZIP}
	cp $< $@

clean:
	rm -rf ${SERVERZIP} ${CLIENTZIP} .tmp build
