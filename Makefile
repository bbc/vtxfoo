.PHONY: clean test uberjar sources rpm

clean:
	mvn clean
	rm -Rf RPMS/*
	rm -Rf SOURCES/*

test:
	mvn test

fatjar:
	mvn package

sources: fatjar
	mkdir -p "SOURCES"
	tar --exclude-vcs -czf "SOURCES/vtxfoo.tar.gz" "target/vtxfoo-fat.jar" "src/etc"
	tar --exclude-vcs -czf "SOURCES/bake-scripts.tar.gz" $(wildcard bake-scripts/*)

rpm: sources
	mbt
