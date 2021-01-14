def stage(ctx):
    return {
        "parent": "one",
        "triggers": {
            "manual": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "manu",
            "steps": [{
                "tool": "shell",
                "cmd": "echo world"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
