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
                "tool": "shell",
                "cmd": "echo $MY_VAR"
            }, {
                "tool": "shell",
                "cmd": "echo '#{env.MY_VAR}'"
            }, {
                "tool": "shell",
                "cmd": "echo '" + ctx.env.MY_VAR + "'"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
