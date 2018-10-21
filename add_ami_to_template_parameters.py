#!/usr/bin/env python
import json

# Get the AMI ID from the packer output
manifest = {}
with open('manifest.json') as manifest_file:
    manifest = json.load(manifest_file)
ami_id = manifest['builds'][-1]['artifact_id'].split(':')[1]
print(manifest)

# Update the cf-parameters.json
with open('cf-parameters.json', 'r+') as parameters_file:
    parameters = json.load(parameters_file)

    parameters['Parameters']['AMIId'] = ami_id
    print(parameters)
    parameters_file.seek(0)
    json.dump(parameters, parameters_file)
    parameters_file.truncate()
