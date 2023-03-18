def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello world",
            "steps": [{
			    "tool": "git",
			    "checkout": "http://github.com/Kraken-CI/workflow-examples",
                "branch": "main"
			}, {
                "tool": "shell",
                "cmd": "ls -al workflow-examples/dynamic-schema"
            }, {
                "tool": "data",
                "file": "workflow-examples/dynamic-schema/systems.json",
                "json_pointer": "/systems"
            }, {
                "tool": "data",
                "file": "workflow-examples/dynamic-schema/tests-scope.json",
                "json_pointer": "/tests"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
