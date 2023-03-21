def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "flow_label": "demo-#{flow.seq.shared}",
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello",
            "steps": [{
                "tool": "shell",
                "cmd": "cat /etc/*release*",
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
