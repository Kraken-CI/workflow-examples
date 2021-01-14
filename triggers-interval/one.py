def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "interval": "10h"
            # "interval": "120s"
            # "interval": "1d 3h 30m 10s"
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello world",
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'hello world'"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
