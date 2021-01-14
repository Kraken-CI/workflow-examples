def stage(ctx):
    txt = 'CI'
    if ctx.is_dev:
        txt = 'DEV'
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters":  [],
        "configs": [],
        "jobs": [{
            "name": "hello world",
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'hello %s'" % txt
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
