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
                "cmd": "echo 'hello world'"
            }],
            "environments": [{
                "system": [
                    "ubuntu/focal/amd64",
                    "centos/8-Stream/amd64",
                    "debian/buster/amd64",
                    "opensuse/15.3/amd64",
                    "fedora/35/amd64"
                ],
                "agents_group": "lxd",
                "executor": "lxd",
                "config": "default"
            }]
        }]
    }
