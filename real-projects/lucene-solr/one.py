def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "interval": "10h"
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "do all",
            "timeout": 3500,
            "steps": [{
                "tool": "git",
                "timeout": 600,
                "checkout": "https://github.com/apache/lucene-solr.git"
            }, {
                "tool": "shell",
                "timeout": 2500,
                "cwd": "lucene-solr",
                "cmd": "./gradlew assemble -Dversion.suffix=`git rev-parse --short HEAD`-#{KK_FLOW_SEQ}"
            }, {
                "tool": "artifacts",
                "action": "upload",
                "cwd": "lucene-solr/lucene/packaging/build/distributions/",
                "source": [
                    "lucene-*.tgz",
                    "lucene-*.tgz.sha512"
                ],
                "public": True
            }],
            "environments": [{
                "system": "openjdk:11.0-jdk-buster",
                "executor": "docker",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
