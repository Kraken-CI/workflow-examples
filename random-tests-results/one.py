def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello",
            "steps": [{
                "tool": "rndtest",
                "count": 100
            }],
            "environments": [{
                "system": "krakenci/ubuntu:20.04",
                "executor": "docker",
                "agents_group": "all",
                "config": "c1"
            }]
        }]
    }
