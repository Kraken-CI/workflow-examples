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
                "cmd": "rm -rf aaa /tmp/bbb /tmp/ccc && \
                        mkdir -p aaa /tmp/bbb /tmp/ccc && \
                        echo 'hello world' > aaa/a.txt && \
                        echo 'hello world' > /tmp/bbb/b.txt && \
                        echo 'hello world' > /tmp/ccc/c.txt"
            }, {
                "tool": "cache",
                "action": "save",
                "key": "one-key",
                "paths": [
                    "aaa",           # path inside current dir
                    "../../../bbb",  # path outside of current dir
                    "/tmp/ccc"       # absolute path
                ]
            }, {
                "tool": "shell",
                "cmd": "rm -rf aaa /tmp/bbb /tmp/ccc"
            }, {
                "tool": "cache",
                "action": "restore",
                "keys": ["one-key"]
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
