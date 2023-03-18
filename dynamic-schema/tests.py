def stage(ctx):
    jobs = []
    for ts in ctx.flow.data.tests:
        jobs.append({
            "name": "tests %s" % ts,
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'run tests %s'" % ts
            }],
            "environments": [{
                "executor": "docker",
                "system": ctx.flow.data.systems,
                "agents_group": "all",
                "config": "default"
            }]
        })
    return {
        "parent": "Prepare Testing",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": jobs
    }
