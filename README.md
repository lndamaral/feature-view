Feature View is an easy way to convert Gherkin files into HTML files. Once you set the Github profile in the configuration file, Feature View has access to all repositories.

At this point, you only need to pass the repository name in the URL (`http:\\localhost:5000\<repository-name>) so Feature View can scan all the given repository and convert the all the feature files into an HTML page.


# Usage

## To Install
```
git clone https://github.com/lndamaral/feature-view.git
cd feature view; pip install -r requirements.txt
```

## To run
```
export GITHUB_PROFILE=<github profile>
python run.py
```

## To check HTML
Check it out on: http://localhost:5000/<repository-name> or http://localhost:5000/<repository-name>/<branch>