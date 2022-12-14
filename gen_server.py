import yaml 
import re
import os
import shutil
from pathlib import Path

if __name__ == '__main__':
    if(os.path.isdir(f'{__file__}\\..\\.gen_server') == True):
        shutil.rmtree(f'{__file__}\\..\\.gen_server')

    Path(f'{__file__}\\..\\.gen_server').mkdir()
    Path(f'{__file__}\\..\\.gen_server\\Models').mkdir()

    with open('swagger.yaml', 'r') as f:
        data = yaml.safe_load(f) 

        for key, value in data['definitions'].items():
            write_code = f"class {key}:"
            
            if 'properties' not in value.keys():
                continue

            for property_key, property_value in value['properties'].items():
                if 'type' in property_value.keys():
                    write_code += '\n' + f"    {property_key} = None # {property_value['type']}"
                else:
                    write_code += '\n' + f"    {property_key} = None # error"
            
            class_file_name = re.sub(r'(?<!^)(?=[A-Z])', '_', key).lower()

            
            Path(f'{__file__}\\..\\.gen_server\\Models\\{class_file_name}.py').write_text(write_code)