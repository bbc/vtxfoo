#!/usr/bin/env sh

mvn package
java -jar target/vtxfoo-fat.jar \
  --redeploy="src/**/*.java,src/**/*.html" \
  --on-redeploy="./run.sh"