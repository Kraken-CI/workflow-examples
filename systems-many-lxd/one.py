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
                    "centos/8-Stream/amd64",
                    "centos/9-Stream/amd64",
                    "debian/10/amd64",  # buster
                    "debian/11/amd64",  # bullseye
                    "fedora/35/amd64",
                    "opensuse/15.3/amd64",
                    "ubuntu/focal/amd64",
                    "ubuntu/jammy/amd64",
                    "rockylinux/8/amd64"
                ],
                "agents_group": "lxd",
                "executor": "lxd",
                "config": "default"
            }]
        }]
    }
