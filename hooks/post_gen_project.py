from pathlib import Path
from datetime import date

delete_manifests = [
    '{% if cookiecutter.include_streamlit_config != "yes" %} .streamlit {% endif %}',
    '{% if cookiecutter.include_dev_setup != "yes" %} tests,.flake8,.pre-commit-config.yml,Makefile,pyproject.toml,requirements.dev.txt {% endif %}',
    '{% if cookiecutter.include_gitpod_config != "yes" %} .gitpod.yml {% endif %}',
    '{% if cookiecutter.include_heroku_deployment != "yes" %} app.json,Procfile,runtime.txt {% endif %}',
    '{% if cookiecutter.project_template != "cheat_sheet" %} LICENSE_streamlit_cheatsheet,logomark_website.png {% endif %}',
    '{% if cookiecutter.project_template != "image_processing" %} yolo {% endif %}',
    '{% if cookiecutter.project_template != "data_science" %} src,data,models {% endif %}',
]


def post_license_year():
    license = Path.cwd() / "LICENSE"
    license_content = license.read_text()
    current_year = str(date.today().year)
    license.write_text(license_content.replace("LICENSE_YEAR", current_year))


def promote_template():
    template_dir = Path.cwd() / "streamlit_app_templates"
    templates = template_dir.iterdir()
    project_template = "{{ cookiecutter.project_template }}.py"
    for template in templates:
        if template.name == project_template:
            template.rename(Path.cwd() / "streamlit_app.py")
        else:
            template.unlink()
    template_dir.rmdir()


def remove_unwanted():
    for files in delete_manifests:
        paths = files.strip().split(",")
        to_remove = [Path.cwd() / path for path in paths if path != '']
        recursive_remove(to_remove)


def recursive_remove(paths):
    for path in paths:
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            recursive_remove(path.iterdir())
            path.rmdir()


def download_model_weights():
    weights_url = "https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.weights"
    manual_download = f"For yolov4-tiny.weights, download from {weights_url}. The file should be in your project's yolo folder next to ./yolo/yolov4-tiny.cfg"
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
            (Path("yolo") / "yolov4-tiny.weights").write_bytes(weights_response.content)
        except Exception as e:
            print(e)
            print(manual_download)


post_license_year()
promote_template()
remove_unwanted()
if "{{ cookiecutter.project_template }}" == "image_processing":
    download_model_weights()
