def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            # minutes, hours, days, months, dow
            "cron": "0 13 */2 * *",
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
