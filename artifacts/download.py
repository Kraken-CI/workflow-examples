def stage(ctx):
    return {
        "parent": "upload",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello world",
            "steps": [{
                "tool": "artifacts",
                "action": "download",
                "source": "abc"
            }, {
                "tool": "shell",
                "cmd": "ls -al && cat abc/a.txt"
            }, {
                "tool": "artifacts",
                "source": "abc/a.txt",
                "public": True
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
