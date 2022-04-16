# Cookiecutter Streamlit

A collection of [cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/README.html) templates for generating a skeleton for your next fantastic [Streamlit](https://streamlit.io/) app! 🎈

Plenty to deploy to [Streamlit Cloud](https://streamlit.io/cloud).

Options to develop in [gitpod](https://www.gitpod.io/) and deploy to [heroku](https://www.heroku.com/)

Made with ❤️ from [Gar's Bar](https://tech.gerardbentley.com/)

Make an awesome project with this?
Share it on twitter `@garsbar35plus` or in the [Streamlit Discuss Forums](https://discuss.streamlit.io/)

- [Cookiecutter Streamlit](#cookiecutter-streamlit)
  - [Getting Started](#getting-started)
  - [All Config Options](#all-config-options)
  - [All Templates](#all-templates)
    - [hello_world](#hello_world)
    - [cheat_sheet](#cheat_sheet)
    - [image_processing](#image_processing)
  - [Connect to your own Repo](#connect-to-your-own-repo)
  - [More Streamlit Resources](#more-streamlit-resources)

## Getting Started

- Ensure you have python 🐍 installed (if you don't, see [my way](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html))
- Install the `cookiecutter` 🍪 package

```sh
python -m pip install cookiecutter
```

*NOTE:* These steps need to be followed once in order to use any cookiecutter template.

- Run `cookiecutter` on this repository
  - You'll have to press enter or type your own values to replace defaults for each option (more info below)

```sh
cookiecutter https://github.com/gerardrbentley/cookiecutter-streamlit
```

- Open up your new project directory in your favorite text editor to get hacking!
  - Or just run it!

```sh
# Replace streamlit_app with your project directory name
cd streamlit_app
# If you don't have streamlit or other necessary packages installed, open your new README.md and get it installed!
streamlit run streamlit_app.py
```

*BONUS:* Use `git clone` with the same url to customize the templates for your own liking then use `cookiecutter cookiecutter-streamlit`

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

Save your project and share with the world!
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

*NOTE:* In general don't `git add .` useless files into your repo. This skeleton should be all useful though! Also take some time to [learn branching](https://docs.gitlab.com/ee/topics/gitlab_flow.html) if you're working with others!

## More Streamlit Resources

- [Official Docs](https://docs.streamlit.io/)
- [Official App Gallery](https://streamlit.io/gallery)
- [Official Components Gallery](https://streamlit.io/components)
