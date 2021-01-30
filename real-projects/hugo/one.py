def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "repo": {
                "url": "https://github.com/gohugoio/hugo.git",
                "branch": "master",
                "interval": "2d"
            }
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "do all",
            "timeout": 2500,
            "steps": [{
                "tool": "git",
                "checkout": "https://github.com/gohugoio/hugo.git"
            }, {
                "tool": "cache",
                "action": "restore",
                "keys": ["one-key"]
            }, {
                "tool": "shell",
                "cwd": "hugo",
                "cmd": "go mod download"
            }, {
                "tool": "cache",
                "action": "save",
                "key": "one-key",
                "paths": [
                    "$GOPATH/pkg/mod/"
                ]
            }, {
                "tool": "shell",
                "cwd": "hugo",
                "cmd": "go mod verify"
            }, {
                "tool": "shell",
                "cwd": "hugo",
                "cmd": "go build",
                "timeout": 1000
            }, {
                "tool": "artifacts",
                "action": "upload",
                "cwd": "hugo",
                "source": [
                    "hugo"
                ],
                "public": True
            }, {
                "tool": "gotest",
                "cwd": "hugo",
                "timeout": 500,
                "params": "-p 1 ./..."
            }],
            "environments": [{
                "system": "krakenci/golang:1.15",
                "executor": "docker",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
