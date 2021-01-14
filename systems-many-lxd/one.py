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
                    "centos/8/amd64",
                    "debian/buster/amd64",
                    "opensuse/15.2/amd64",
                    "fedora/32/amd64"
                ],
                "agents_group": "lxd",
                "executor": "lxd",
                "config": "default"
            }]
        }]
    }
