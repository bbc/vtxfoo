#!/usr/bin/env sh

mvn package
java -jar target/vtxfoo-fat.jar -conf src/etc/vtxfoo/application-conf.json \
  --redeploy="src/**/*.java,src/**/*.html" \
  --on-redeploy="./run.sh"