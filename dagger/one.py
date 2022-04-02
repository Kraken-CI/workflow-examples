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
                "tool": "shell",
                "cmd": "dagger do build --log-format plain",
                "cwd": "dagger/pkg/universe.dagger.io/examples/todoapp",
                "timeout": 240
            }, {
                "tool": "shell",
                "cmd": "ls -al _build",
                "cwd": "dagger/pkg/universe.dagger.io/examples/todoapp"
            }],
            "environments": [{
                "system": "krakenci/bld-kraken",
                "executor": "docker",
            	"agents_group": "all",
                "config": "default"
            }]
        }]
    }
