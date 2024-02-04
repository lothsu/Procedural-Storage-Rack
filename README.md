# Procedural-Storage-Rack .obj generation

The goal is to generate procedural new Storage Racks with different dimensions. The file will be in the Wavefront Object format (.obj). 
This project was made obsolete with the generative model generation by threestudio (Magic3D). Since the AI generation of 3D models takes a lot of computing power (+48GB VRAM) this approach could still be interesting with low compute power environments.
## Parameters
All parameters should be integers and in mm. For other units change the dim in the lageregal.py file
	
	python lagerregal.py -h -l -d -e -t

|                |short parameter                          |type                      |
|----------------|-------------------------------|-----------------------------|
|hight|-hi                    |int
|length          |-l            |int         |
|depth         |-d|int|
|edgelength|-e|int|
|thickness|	-t|int|


## Further Notes
This approach uses the idea of extrusion. With some more time it could be made into a library for easier Mesh generation
