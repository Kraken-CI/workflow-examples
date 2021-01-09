def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "repo": {
                "url": "https://github.com/Kraken-CI/kraken/",
                "branch": "master",
                "interval": "60m"
            }
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
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
