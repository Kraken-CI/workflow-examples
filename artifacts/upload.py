def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "upload",
            "steps": [{
                "tool": "shell",
                "cmd": "mkdir abc && echo 'hello world' > abc/a.txt"
            }, {
                "tool": "artifacts",
                "source": "abc"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
