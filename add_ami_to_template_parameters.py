#!/usr/bin/env python
import json

# Get the AMI ID from the packer output
manifest = {}
with open('manifest.json') as manifest_file:
    manifest = json.load(manifest_file)
ami_id = manifest['builds'][0]['artifact_id'].split(':')[1]


# Update the cf-parameters.json
with open('cf-parameters.json', 'r+w') as parameters_file:
    parameters = json.load(parameters_file)

    amiid_index = (
        i for i, v in enumerate(parameters) if 'AMIId' in v['ParameterKey']
    )
    parameters[next(amiid_index)]['ParameterValue'] = ami_id

    parameters_file.seek(0)
    json.dump(parameters, parameters_file)
    parameters_file.truncate()