def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "flow_label": "bld-#{KK_CI_DEV_FLOW_SEQ}",
        #"run_label": "run.#{KK_CI_DEV_RUN_SEQ}",
        "jobs": [{
            "name": "seqs",
            "steps": [{
                "tool": "shell",
                "cmd": "echo #{KK_FLOW_SEQ} #{KK_CI_DEV_FLOW_SEQ} #{KK_FLOW_TYPE} #{KK_BRANCH}"
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
