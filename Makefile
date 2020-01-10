install:
	poetry install

lint:
	poetry run flake8 brain_games

publish:
	poetry publish -r demshin_brain_games 
