def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "repo": {
                "url": "https://github.com/apache/lucene.git",
                "branch": "main",
                "interval": "2d"
            }
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "do all",
            "timeout": 8000,
            "steps": [{
                "tool": "git",
                "timeout": 600,
                "checkout": "https://github.com/apache/lucene.git",
                "branch": "main"
            }, {
                "tool": "shell",
                "timeout": 2500,
                "cwd": "lucene",
                "cmd": "./gradlew assemble -Dversion.suffix=`git rev-parse --short HEAD`-#{KK_FLOW_SEQ}"
            }, {
                "tool": "artifacts",
                "action": "upload",
                "cwd": "lucene/lucene/packaging/build/distributions/",
                "source": [
                    "lucene-*.tgz",
                    "lucene-*.tgz.sha512"
                ],
                "public": True
            }, {
                "tool": "shell",
                "timeout": 4000,
                "cwd": "lucene",
                "cmd": "./gradlew -p lucene/core test -Dversion.suffix=`git rev-parse --short HEAD`-#{KK_FLOW_SEQ}"
            }, {
                "tool": "shell",
                "cwd": "lucene",
                "cmd": "find . -name '*.xml' | grep test-results"
            }, {
                "tool": "junit_collect",
                "cwd": "lucene",
                "file_glob": "**/test-results/test/*.xml"
            }],
            "environments": [{
                "system": "krakenci/openjdk:17",
                "executor": "docker",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
