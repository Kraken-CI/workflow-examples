def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "dagger",
            "steps": [{
                "name": "Checkout Dagger example",
                "tool": "git",
                "checkout": "https://github.com/dagger/examples",
                "branch": "main"
            }, {
                "name": "Install Dagger Python SDK",
                "tool": "shell",
                "script": """
                   python3.10 -m venv venv
                   ./venv/bin/pip install -U pip
                   ./venv/bin/pip install dagger-io
                """
            }, {
                "name": "Build using Dagger",
                "tool": "shell",
                "cwd": "examples/python/basic-example",
                "cmd": "../../../venv/bin/python3 test.py",
            }],
            "environments": [{
                "system": "krakenci/bld-kraken-22.04:20230121",
                "executor": "docker",
            	"agents_group": "all",
                "config": "default"
            }]
        }]
    }
