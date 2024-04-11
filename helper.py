import os
def get_project_root_path() -> str:
    return os.path.dirname(os.path.abspath(__file__)) + "/"

def get_resources_path() -> str:
    return get_project_root_path() + "resources/"