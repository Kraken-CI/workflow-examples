def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "flow_label": "bld-#{flow.seq.own}",
        "run_label": "run.#{run.seq.own}",
        "jobs": [{
            "name": "seqs",
            "steps": [{
                "tool": "shell",
                "cmd": "echo 'branch: #{args.branch}, flow kind: #{flow.kind} '"
            }, {
                "tool": "shell",
                "cmd": "echo 'flow.shared: #{flow.seq.shared} flow.own: #{flow.seq.own}'"
            }, {
                "tool": "shell",
                "cmd": "echo 'run.shared:#{run.seq.shared} run.own:#{run.seq.own}'"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
