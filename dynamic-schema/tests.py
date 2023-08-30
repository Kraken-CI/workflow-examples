def stage(ctx):
    jobs = []
    for ts in (ctx.flow.data.tests or ['scope-default']):
        jobs.append({
            "name": "tests %s" % ts,
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'run tests %s'" % ts
            }],
            "environments": [{
                "executor": "docker",
                "system": ctx.flow.data.systems or "ubuntu:20.04",
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
