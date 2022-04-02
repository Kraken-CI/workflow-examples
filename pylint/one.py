def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "pylint",
            "steps": [{
                "tool": "git",
                "checkout": "https://github.com/Kraken-CI/sample-project-python.git"
            }, {
                "tool": "shell",
                "cmd": "sudo apt-get update && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends pylint"
            }, {
                "tool": "pylint",
                "modules_or_packages": "src",
                "cwd": "sample-project-python"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
