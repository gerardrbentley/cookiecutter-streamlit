# Cookiecutter Streamlit

A collection of [cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/README.html) templates for generating a skeleton for your next fantastic [streamlit](https://streamlit.io/) app! 🎈

Plenty to deploy to [Streamlit Cloud](https://streamlit.io/cloud).

Options to develop in [gitpod](https://www.gitpod.io/) and deploy to [heroku](https://www.heroku.com/)

Made with ❤️ from [Gar's Bar](https://tech.gerardbentley.com/)

Make an awesome project with this?
Share it on twitter `@garsbar35plus` or in the [Streamlit Discus Forums](https://discuss.streamlit.io/)

## Getting Started

- Ensure you have python installed (if you don't, see [my way](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html))
- Install the `cookiecutter` package

```sh
python -m pip install cookiecutter
```

*NOTE:* These steps need to be followed once in order to use any template.

- Run cookiecutter on this repo
  - You'll have to press enter or type your own values to replace defaults for each option (more info below)

```sh
cookiecutter https://github.com/gerardrbentley/
```

## All Config Options

- `github_username`: Used for github links and the "made by" text
- `licensor_name`: Your full name or company name
- `project_name`: Name of your new app
- `project_slug`: defaults to camel_case version of your project name
- `project_short_description`: Description of your project
- `include_streamlit_config`: defaults to "yes" to generate .streamlit/config.toml
- `include_heroku_deployment`: defaults to "no" to not generate Procfile, app.json, runtime.txt
- `include_gitpod_config`: defaults to "no" to not generate .gitpod.yml
- `project_template`: defaults to "hello_world", see below template descriptions

## All Templates

### hello_world

Streamlit "Hello World".

Just enough to get started with your streamlit app, a README, requirements, and github necessities.

### cheat_sheet

Streamlit cheat sheet from [daniellewisDL](https://github.com/daniellewisDL/streamlit-cheat-sheet) (MIT License included)

### image_processing

Provides example with YOLOv4-tiny model for receiving user image input, processing the image, and displaying the results.

User can provide an image via URL, file upload, or webcam.

Includes weights and configurations for YOLOv4-tiny on OpenCV from [darknet github](https://github.com/AlexeyAB/darknet), which will not apply to all projects.

## Connect to your own Repo

Save your project and share with the world.
Start a repository on github (using the same name as your current folder will keep the documentation in line).
Or use gitlab / gitea and change the folder name if you know what you're doing!

```sh
# Run once
git init
git remote add origin git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

# Run for your changes and pushes
git add .
git commit -m "feat: Streamlit App Starter!"
git push
```

*NOTE:* in general don't `git add .` useless files into your repo. This skeleton should be all useful though! Also take some time to learn branching if you're working with others!
