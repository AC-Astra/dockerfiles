import subprocess
import sys

def config():
    registry_name = "ghcr.io"
    github_username = "ac-astra"
    return f"{registry_name}/{github_username}"

def clone_image(image_name):
    new_repo = config()
    target_image = f"{new_repo}/{image_name}"
    podman_command = f'''
    podman pull {image_name}
    podman tag {image_name} {target_image}:latest
    podman push {target_image}:latest
    '''

    subprocess.run(podman_command, shell=True, check=True)
    print(f"Okay!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mirror.py <image-name>")
        sys.exit(1)
    image_name = sys.argv[1]
    clone_image(image_name)
