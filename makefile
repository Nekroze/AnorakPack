SHELL := /bin/bash
VERSION=0.1.0
CLIENTZIP=releases/AnorakPack-${VERSION}-client.zip
SERVERZIP=releases/AnorakPack-${VERSION}-server.zip

.PHONY: clean client server push

all: ${CLIENTZIP} ${SERVERZIP}

client: ${CLIENTZIP}

server: ${SERVERZIP}

${CLIENTZIP}: build/client/bin/modpack.jar
	@mkdir -p releases
	zip -rq $@ build/client/

build/client/bin/modpack.jar: AnorakPack.py
	python $<

${SERVERZIP}: build/server/server.jar
	@mkdir -p releases
	zip -rq $@ build/server/

build/server/server.jar: AnorakPack.py
	python $<

push: ${CLIENTZIP} ${SERVERZIP}
	cp $< /cygdrive/g/Dropbox/Public/

clean:
	rm -rf ${SERVERZIP} ${CLIENTZIP} .tmp build
