install:
	pip install -r requirements.txt

serve:
	$(call terminal, python server.py)

swagger-build:
	specsynthase specs/cm4.yaml specs/cm4/vm.yaml specs/cm4/image.yaml specs/cm4/flavor.yaml > server/swagger.yaml

	