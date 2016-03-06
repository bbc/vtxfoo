#! /usr/bin/env python
import sys
import json

if __name__ == "__main__":
    config_filename = sys.argv[1]

    with open(config_filename) as config_file:
        config = json.load(config_file)
        with open("/etc/sysconfig/vtxfoo", "a") as sysconfig:
            sysconfig.write(json.dumps(config))


