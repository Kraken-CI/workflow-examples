def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True
        },
        "parameters": [{
            "name": "COUNT",
            "type": "string",
            "default": "10",
            "description": "Number of tests to generate"
        }],
        "jobs": [{
            "name": "random tests",
            "timeout": 100000,
            "steps": [{
                "tool": "rndtest",
                "count": "#{COUNT}"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "executor": "docker",
                "config": "default"
            }]
        }]
    }
