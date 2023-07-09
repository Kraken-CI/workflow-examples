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
            }, {
                "when": "was_no_error",
                "tool": "shell",
                "cmd": "echo 'was_no_error'"
            }, {
                "when": "was_any_error",
                "tool": "shell",
                "cmd": "echo 'was_any_error'"
            }, {
                "when": "is_ci",
                "tool": "shell",
                "cmd": "echo 'is_ci'"
            }, {
                "when": "is_dev",
                "tool": "shell",
                "cmd": "echo 'is_dev'"
            }, {
                "tool": "shell",
                "cmd": "missing-command-xyz"
            }, {
                "when": "was_no_error",
                "tool": "shell",
                "cmd": "echo 'was_no_error 2'"
            }, {
                "when": "was_any_error",
                "tool": "shell",
                "cmd": "echo 'was_any_error 2'"
            }, {
                "when": "always",
                "tool": "shell",
                "cmd": "echo 'hello world #{job.id} 2 #{job.steps[0].result}' && sleep 5"
            }, {
                "when": "job.steps[step.index - 1].result.duration > 3",
                "tool": "shell",
                "cmd": "echo 'hello world #{job.steps[step.index - 1].result.duration}'"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
