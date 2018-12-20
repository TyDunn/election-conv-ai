train-nlu:
	python -m rasa_nlu.train -c config.yml --data data/nlu_data.md -o models --fixed_model_name nlu_model --project current --verbose

train-core:
	python -m rasa_core.train -d domain.yml -s data/stories.md -o models/current/dialogue --epochs 200

cmdline:
	python -m rasa_core.run -d models/current/dialogue -u models/current/nlu_model --endpoints endpoints.yml

action-server:
	python -m rasa_core_sdk.endpoint --actions actions
