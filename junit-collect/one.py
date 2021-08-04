def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "junit collect",
            "steps": [{
            	"tool": "git",
            	"checkout": "https://github.com/junit-team/junit5-samples.git",
                "branch": "main"
            }, {
                "tool": "shell",
                "cmd": "./mvnw test",
                "cwd": "junit5-samples/junit5-jupiter-starter-maven"
            }, {
                "tool": "junit_collect",
                "cwd": "junit5-samples/junit5-jupiter-starter-maven/",
                "file_glob": "target/*/*xml"
            }],
            "environments": [{
                "system": "openjdk:11.0.12-slim-buster",
                "agents_group": "all",
                "executor": "docker",
                "config": "default"
            }]
        }]
    }
