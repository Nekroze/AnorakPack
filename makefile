SHELL := /bin/bash
PRIVATE=TRUE
ifeq ($(PRIVATE),TRUE)
	VERSION=0.1.0Pb
else
	VERSION=0.1.0b
endif
CLIENTZIP=releases/AnorakPack-${VERSION}-client.zip
SERVERZIP=releases/AnorakPack-${VERSION}-server.zip
PUBLIC=/cygdrive/g/Dropbox/Public/${notdir ${CLIENTZIP}}


.PHONY: clean client server push

all: ${CLIENTZIP} ${SERVERZIP}

client: ${CLIENTZIP}

server: ${SERVERZIP}

${CLIENTZIP}: build/client/bin/modpack.jar
	@mkdir -p releases
	@rm -f $@
	cd build/client && zip -rq ../../$@ ./*

build/client/bin/modpack.jar: AnorakPack.py $(shell find components/data -print0 -type f)
	@rm -rf build
	python $< ${PRIVATE}

${SERVERZIP}: build/server/server.jar
	@mkdir -p releases
	@rm -f $@
	cd build/server && zip -rq ../../$@ ./*

build/server/server.jar: ${CLIENTZIP}

# Push is an example for how to "upload" to a public location
push: ${PUBLIC}

${PUBLIC}: ${CLIENTZIP} ${SERVERZIP}
	cp $< $@

clean:
	rm -rf ${SERVERZIP} ${CLIENTZIP} .tmp build
