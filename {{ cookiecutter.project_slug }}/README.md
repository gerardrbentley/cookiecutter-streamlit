{% set do_streamlit = cookiecutter.include_streamlit_config == 'yes' -%}
{% set do_heroku = cookiecutter.include_heroku_deployment == 'yes' -%}
{% set do_gitpod = cookiecutter.include_gitpod_config == 'yes' -%}

# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

Built with ❤️ by [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})
{%- if do_heroku %}

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})
{% endif %}
{%- if do_gitpod %}

<a href="https://gitpod.io/#https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}" rel="nofollow noopener noreferrer" target="_blank" class="after:hidden"><img src="https://gitpod.io/button/open-in-gitpod.svg" alt="Open in Gitpod"></a>
{% endif %}

## What's this?

- `README.md`: This Document! To help you find your way around
- `streamlit_app.py`: The main app that gets run by [`streamlit`](https://docs.streamlit.io/)
- `requirements.txt`: Pins the version of packages needed
- `LICENSE`: Follows Streamlit's use of Apache 2.0 Open Source License
- `.gitignore`: Tells git to avoid comitting / scanning certain local-specific files
{%- if do_streamlit %}
- `.streamlit/config.toml`: Customizes the behaviour of streamlit without specifying command line arguments (`streamlit config show`)
{% endif -%}
{%- if do_heroku %}- `app.json`: Provides "Deploy to Heroku" functionality / specification
- `Procfile`: Special file to tell Heroku how to run our app (`streamlit run`) (see [docs](https://devcenter.heroku.com/articles/procfile))
- `runtime.txt`: Special file to tell Heroku which python version to use (see [supported runtimes](https://devcenter.heroku.com/articles/python-support#supported-runtimes))
{% endif -%}
{%- if do_gitpod %}- `.gitpod.yml`: Special file to tell Gitpod how to start running your app (see [docs](https://www.gitpod.io/docs/config-gitpod-file) and [python docs](https://www.gitpod.io/docs/languages/python))
{% endif %}
## Local Setup

Assumes working python installation and some command line knowledge ([install python with conda guide](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html)).

```sh
# External users: download Files
git clone git@github.com:{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.git

# Go to correct directory
cd {{ cookiecutter.project_slug }}

# Create virtual environment for this project
python -m venv venv

# Activate the virtual environment
. ./venv/bin/activate
# .\venv\Scripts\activate for Windows

# Install required Packages
python -m pip install -r requirements.txt

# Run the streamlit app
streamlit run streamlit_app.py
```

Open your browser to [http://localhost:8501/](http://localhost:8501/) if it doesn't open automatically.

## Deploy

For the easiest experience, deploy to [Streamlit Cloud](https://streamlit.io/cloud)

For other options, see [Streamilt deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)

## Credits

This package was created with Cookiecutter and the `gerardrbentley/cookiecutter-streamlit` project template.

- Cookiecutter: [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
- `gerardrbentley/cookiecutter-streamlit`: [https://github.com/gerardrbentley/cookiecutter-streamlit](https://github.com/gerardrbentley/cookiecutter-streamlit)
