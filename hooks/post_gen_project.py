from pathlib import Path
from datetime import date


def post_license_year():
    license = Path.cwd() / "LICENSE"
    license_content = license.read_text()
    current_year = str(date.today().year)
    license.write_text(license_content.replace("LICENSE_YEAR", current_year))


def remove_unwanted(paths):
    for raw_path in paths:
        path = Path.cwd() / raw_path
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            remove_unwanted(path.iterdir())
            path.rmdir()


def download_model_weights():
    weights_url = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"
    manual_download = f"For yolov4-tiny.weights, download from {weights_url}. The file should be in your project folder next to yolov4-tiny.cfg"
    try:
        import requests
    except ModuleNotFoundError:
        print(
            "Install the 'requests' library to automatically download model weights with this cookiecutter."
        )
        print(manual_download)
    else:
        try:
            weights_response = requests.get(weights_url)
            Path("yolov4-tiny.weights").write_bytes(weights_response.content)
        except Exception as e:
            print(e)
            print(manual_download)


post_license_year()
manifests = [
    '{% if cookiecutter.include_streamlit_config != "yes" %} .streamlit {% endif %}',
    '{% if cookiecutter.include_dev_setup != "yes" %} tests,.flake8,.pre-commit-config.yml,Makefile,pyproject.toml,requirements.dev.txt {% endif %}',
]
remove_paths = []
for files in manifests:
    paths = files.strip().split(',')
    if len(paths):
        remove_paths.extend(paths)
remove_unwanted(remove_paths)
if "{{ cookiecutter.project_template }}" == "image_processing":
    download_model_weights()
