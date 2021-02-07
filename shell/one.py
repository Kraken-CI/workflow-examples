def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "shell examples",
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'Hello World'"
            }, {
                "tool": "shell",
                "cmd": "pwd && ls -al",
                "cwd": "/"
            }, {
                "tool": "shell",
                "cmd": "whoami"
            }, {
                "tool": "shell",
                "cmd": "whoami",
                "user": "root"
            }, {
                "tool": "shell",
                "cmd": "echo $MSG",
                "env": {
                    "MSG": "hello world"
                }
            }, {
                "tool": "shell",
                "cmd": "exit $(($RANDOM % 3))",
                "attempts": 10,
                "sleep_time_after_attempt": 4
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
