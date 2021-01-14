def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "hello",
            "steps": [{
                "tool": "git",
                "checkout": "https://github.com/Kraken-CI/sample-project-python.git"
            }, {
                "tool": "pytest",
                "cwd": "sample-project-python",
                "params": "-vv",
                "pythonpath": "src"
            }, {
                "tool": "shell",
                "cmd": "sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends python3-wheel python3-setuptools"
            }, {
                "tool": "shell",
                "cwd": "sample-project-python",
                "cmd": "python3 setup.py sdist bdist_wheel"
            }, {
                "tool": "artifacts",
                "action": "upload",
                "cwd": "sample-project-python/dist",
                "source": [
                    "sampleproject-2.0.0-py3-none-any.whl", 
                    "sampleproject-2.0.0.tar.gz"
                ],
                "public": True
            }],
            "environments": [{
                "system": "any",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
