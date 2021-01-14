def stage(ctx):
    return {
        "parent": "root",
        "triggers": {
            "parent": True,
        },
        "parameters": [],
        "configs": [],
        "jobs": [{
            "name": "build",
            "timeout": 1200,
            "steps": [{
                "tool": "shell",
                "cmd": "cat /etc/*release*",
            }],
            "environments": [{
                "system": ["maven:3.6.3-jdk-11", 
                           "fedora:32", 
                           "centos:8", 
                           "debian:buster", 
                           "debian:bullseye", 
                           "ubuntu:18.04", 
                           "ubuntu:20.04", 
                           "krakenci/bld-kraken",
                           "krakenci/ubuntu:20.04",
                           "krakenci/python:3.8",
                           "krakenci/maven:3.6.3-jdk-11"],
                "executor": "docker",
                "agents_group": "all",
                "config": "c1"
            }]
        }]
    }
