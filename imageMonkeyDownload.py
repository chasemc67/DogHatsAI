import logging
from pyimagemonkey import API

if __name__ == "__main__":
	logging.basicConfig()

	api = API(api_version=1)
	res = api.export_to_folder(["dog.has='eye'", "dog.has='nose'"], "./Data/AnnotatedData", min_probability = 0.8, only_annotated = True)