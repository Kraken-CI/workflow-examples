def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "robot",
            "steps": [{
            	"tool": "git",
            	"checkout": "https://github.com/robotframework/RobotDemo.git"
            }, {
                "tool": "shell",
                "cmd": "python3 -m venv venv && ./venv/bin/pip install robotframework"
            }, {
                "tool": "shell",
                "cmd": "../venv/bin/robot --nostatusrc -x junit.xml *.robot",
                "cwd": "RobotDemo"
            }, {
                "tool": "junit_collect",
                "cwd": "RobotDemo",
                "file_glob": "junit.xml"
            }, {
                "tool": "artifacts",
                "cwd": "RobotDemo",
                "source": ["log.html", "report.html"],
                "report_entry": "report.html",
                "public": True
            }],
            "environments": [{
                "system": "krakenci/ubuntu:20.04",
                "executor": "docker",
                "agents_group": "all",
                "config": "default"
            }]
        }]
    }
