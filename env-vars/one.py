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
                "system": "ubuntu/focal/amd64",
                "agents_group": "all",
                "executor": "lxd",
                "config": "default"
            }, {
                "system": "krakenci/ubuntu:20.04",
                "agents_group": "all",
                "executor": "docker",
                "config": "default"
            }, {
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
