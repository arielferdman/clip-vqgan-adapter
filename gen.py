import sys
import os
import json

if __name__ == '__main__':
    # print command line args
    print(f"Command line args: {sys.argv}")
    # if length of args is not equal to 2 throw an exception but in the exception message reduce the length of the args by 1
    if len(sys.argv) != 2:
        raise Exception(f"Expected 1 argument but got {len(sys.argv) - 1}")
    # store the second argument in a variable
    prompt = sys.argv[1]
    # set the path of the json config file
    config_path = os.path.join(os.path.dirname(__file__), '../configs/local.json')
    # load the config json file from the path stored in config_path
    with open(config_path, 'r') as f:
        #read file and turn it into a dictionary
        config = json.load(f)
        # set the value under the prompts key to a list that contains the prompt variable
        config['prompts'] = [prompt]
        # write the config dictionary to the config file
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

    # change to parent directory
    os.chdir(os.path.join(os.path.dirname(__file__), '..'))
    # run the script that generates the prompts
    os.system('python3 -m scripts.generate -c ./configs/local.json')
