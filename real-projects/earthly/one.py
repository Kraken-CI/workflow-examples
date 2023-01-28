def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "Build Earthly using Earthly",
            "steps": [{
                "tool": "git",
                "checkout": "https://github.com/earthly/earthly.git",
                "branch": "main"
            }, {
                "tool": "shell",
                "script": """
                    sudo apt update
                    sudo apt install -y wget
                    wget https://github.com/earthly/earthly/releases/latest/download/earthly-linux-amd64
                    chmod a+x earthly-linux-amd64
                """
            }, {
                "tool": "shell",
                "timeout": 600,
                "cwd": "earthly",
                "cmd": "../earthly-linux-amd64 +earthly-linux-amd64"
            }],
            "environments": [{
                "system": "krakenci/bld-kraken-22.04:20230121",
                "executor": "docker",
            	"agents_group": "all",
                "config": "default"
            }]
        }]
    }
