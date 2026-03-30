import json
import os
import sys
from jinja2 import Environment, FileSystemLoader

def extract_parameters(request_url):
    """
    Extract query parameters and path variables from Postman request url object.
    """
    params = []
    
    # Query parameters
    for q in request_url.get('query', []):
        params.append({
            'name': q.get('key'),
            'type': 'string', # Postman default to string for query
            'required': True if q.get('disabled') is not True else False,
            'description': q.get('description', 'No description.'),
            'example': q.get('value', '')
        })
        
    # Path variables
    for v in request_url.get('variable', []):
        params.append({
            'name': f":{v.get('key')}",
            'type': 'string',
            'required': True, # Path variables are typically required
            'description': v.get('description', 'No description.'),
            'example': v.get('value', '')
        })
        
    return params

def extract_body(request):
    """
    Extract request body (JSON) from Postman request object.
    """
    body = ""
    if 'body' in request and request['body'].get('mode') == 'raw':
        try:
            data = json.loads(request['body'].get('raw', '{}'))
            body = json.dumps(data, indent=2)
        except json.JSONDecodeError:
            body = request['body'].get('raw', '')
    return body

def extract_response(responses):
    """
    Extract successful response (status 200/201) from Postman response array.
    """
    for r in responses:
        if r.get('code') in [200, 201]:
            try:
                data = json.loads(r.get('body', '{}'))
                return json.dumps(data, indent=2)
            except json.JSONDecodeError:
                return r.get('body', '')
    return "{}"

def flatten_items(postman_items):
    """
    Recursively flatten Postman items to identify only requests.
    """
    requests = []
    for item in postman_items:
        if 'request' in item:
            requests.append(item)
        elif 'item' in item:
            requests.extend(flatten_items(item['item']))
    return requests

def generate_api_reference(collection_path, output_dir, template_dir):
    """
    Deterministic generation of API reference documentation.
    """
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('api_endpoint.md.j2')

    with open(collection_path, 'r', encoding='utf-8') as f:
        collection = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for top_level_folder in collection.get('item', []):
        folder_name = top_level_folder['name']
        # Sanitize folder_name to be a safe filename
        file_basename = folder_name.lower().replace(' ', '-').replace('/', '-').replace('{', '').replace('}', '')
        
        # Identify endpoints in this folder and subfolders
        folder_items = flatten_items(top_level_folder.get('item', []))
        
        endpoints = []
        for item in folder_items:
            req = item['request']
            endpoints.append({
                'name': item['name'],
                'method': req['method'],
                'description': req.get('description', 'No description.'),
                'parameters': extract_parameters(req['url']),
                'request_body': extract_body(req),
                'response_body': extract_response(item.get('response', [])),
                'notes': '' # Potential space for audit results
            })
            
        if endpoints:
            output_content = template.render(items=endpoints)
            output_path = os.path.join(output_dir, f"{file_basename}.md")
            
            # Ensure output directory exists (if nested folders were used)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {folder_name} API\n\n")
                f.write(output_content)
            print(f"Generated: {output_path}")

if __name__ == "__main__":
    COLLECTION_PATH = 'GitHub Web API Reference.postman_collection.json'
    OUTPUT_DIR = 'docs/api-reference'
    TEMPLATE_DIR = 'practitioners/lib/templates'
    
    generate_api_reference(COLLECTION_PATH, OUTPUT_DIR, TEMPLATE_DIR)
