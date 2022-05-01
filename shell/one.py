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
                "cmd": "exit `shuf -i 0-3 -n 1`",
                "attempts": 10,
                "sleep_time_after_attempt": 4
            }, {
                "tool": "shell",
                "script": """
                    sudo apt install -y zsh
                    which zsh
                """
            }, {
                "tool": "shell",
                "cmd": "echo $0",
                "shell_exe": "zsh"
            }],
            "environments": [{
                "system": "krakenci/ubuntu:20.04",
                "agents_group": "docker",
                "executor": "docker",
                "config": "default"
            }]
        }]
    }
