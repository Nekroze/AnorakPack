SHELL := /bin/bash
VERSION=0.1.0
CLIENTZIP=releases/AnorakPack-${VERSION}-client.zip
SERVERZIP=releases/AnorakPack-${VERSION}-server.zip
PUBLIC=/cygdrive/g/Dropbox/Public/${notdir ${CLIENTZIP}}

.PHONY: clean client server push

all: ${CLIENTZIP} ${SERVERZIP}

client: ${CLIENTZIP}

server: ${SERVERZIP}

${CLIENTZIP}: build/client/bin/modpack.jar
	@mkdir -p releases
	cd build/client && zip -rq ../../$@ ./*

build/client/bin/modpack.jar: AnorakPack.py $(shell find components/data -print0 -type f)
	@rm -rf build
	python $<

${SERVERZIP}: build/server/server.jar
	@mkdir -p releases
	cd build/server && zip -rq ../../$@ ./*

build/server/server.jar: ${CLIENTZIP}

push: ${PUBLIC}

${PUBLIC}: ${CLIENTZIP} ${SERVERZIP}
	cp $< $@


clean:
	rm -rf ${SERVERZIP} ${CLIENTZIP} .tmp build
