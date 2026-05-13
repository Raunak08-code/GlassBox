import docker

class DockerMonitor:
    def __init__(self):
        try:
            self.client = docker.from_env()
        except Exception:
            self.client=None
        if not self.client:
            return [] 

    def running_containers(self):
        containers = self.client.list()
        return [
            container.name
            for container in containers
        ]