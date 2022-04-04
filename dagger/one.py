def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "dagger",
            "steps": [{
                "tool": "shell",
                "cmd": "cd /usr/local && curl -L https://dl.dagger.io/dagger/install.sh | sudo sh && dagger version"
            }, {
                "tool": "git",
                "checkout": "https://github.com/dagger/dagger",
                "branch": "v0.2.4"
            }, {
                "tool": "cache",
                "action": "restore",
                "keys": ["dgr"]
            }, {
                "tool": "shell",
                "cmd": "mkdir -p ~/dgr-cache && ls -al ~/dgr-cache",
            }, {
                "tool": "shell",
                "cmd": "dagger do build --log-format plain --cache-from type=local,src=$HOME/dgr-cache --cache-to type=local,mode=max,dest=$HOME/dgr-cache",
                "cwd": "dagger/pkg/universe.dagger.io/examples/todoapp"
            }, {
                "tool": "shell",
                "cmd": "ls -al _build",
                "cwd": "dagger/pkg/universe.dagger.io/examples/todoapp"
            }, {
                "tool": "shell",
                "cmd": "ls -al ~/dgr-cache",
            }, {
                "tool": "cache",
                "action": "save",
                "key": "dgr",
                "paths": ["~/dgr-cache"]
            }],
            "environments": [{
                "system": "krakenci/bld-kraken",
                "executor": "docker",
            	"agents_group": "all",
                "config": "default"
            }]
        }]
    }
