import logging
from pyimagemonkey import API
import os

if __name__ == "__main__":
	logging.basicConfig()

	api = API(api_version=1)
	res = api.export(["dog.has='eye'", "dog.has='nose'"], min_probability = 0.8)

	ctr = 1
	for elem in res:
		print("[%d/%d] Downloading image %s" %(ctr, len(res), elem.image.uuid))
		if len(elem.annotations) > 0:
			# make fulder with the name of the elem UUID for the image and annotation data
			# name the image UUID.png/jpeg
			# name the annotation UUID.json

			# need to move the code i added to the API to here
			api.download_image_with_annotation(elem.image.uuid, "C:\\Users\chase\dev\dogHatsAi\DataAnnotated2")
			ctr += 1