def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "flow_label": "demo-#{KK_FLOW_SEQ}",
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "huge log",
            "steps": [{
                "tool": "shell",
                "cmd": "cat /dev/urandom | tr -dc 'a-zA-Z0-9 ' | fold -w 80 | head -n 100"
            }],
            "environments": [{
                "system": "ubuntu/focal/amd64",
                "agents_group": "lxd",
                "executor": "lxd",
                "config": "default"
            }, {
                "system": "krakenci/ubuntu:20.04",
                "agents_group": "docker",
                "executor": "docker",
                "config": "default"
            }, {
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
