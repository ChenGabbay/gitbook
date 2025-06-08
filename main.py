import json
import os
from typing import Dict, List, Optional
import markdown
from bs4 import BeautifulSoup
import argparse

### CONSTS ###
BLACKLIST_FILENAMES = ['template.md', 'readme.md']
OUTPUT_DIR = './output'  # assume empty library in this path
PERMISSIONS_HEADING_TEXT = 'Required permissions'
PERMISSIONS_HEADING_ID_ATTR = 'h_0bb427264a'
EXPECTED_TABLE_HEADER_COLUMNS = ['Permission', 'Description']

def find_permissions_table_by_anchor(soup: BeautifulSoup) -> Optional[BeautifulSoup]:
    """Find the permissions table by looking for the specific heading with anchor tag.
    Args:
        soup: beautifulSoup object of the parsed HTML 
    Returns: beautifulSoup object of the permissions table if found, None otherwise
    """
    # Find the anchor tag with our specific ID
    anchor = soup.find('a', id=PERMISSIONS_HEADING_ID_ATTR)
    
    # Check if we found the anchor and it's in a heading with our text
    if anchor and anchor.parent and PERMISSIONS_HEADING_TEXT in anchor.parent.text:
        return anchor.parent.find_next('table')
    return None

def is_template_header_format(header_cells: List[BeautifulSoup]) -> bool:
    """Check if table headers match the template format."""
    return (len(header_cells) == len(EXPECTED_TABLE_HEADER_COLUMNS) and 
            all(cell.text.strip() == expected 
                for cell, expected in zip(header_cells, EXPECTED_TABLE_HEADER_COLUMNS)))

def _parse_permission_row(row: BeautifulSoup) -> Optional[Dict[str, str]]:
    """Parse a single permission row from the table."""
    cells = row.find_all('td')
    if len(cells) < 2:
        return None
    
    # Handle description with list items
    description_cell = cells[1]
    list_items = description_cell.find_all('li')
    if list_items:
        description = [item.get_text(separator='\n').strip() for item in list_items]
    else:
        description = [description_cell.get_text(separator='\n').strip()]
    
    return {
        'permission': cells[0].text.strip(),
        'description': description
    }

def _parse_permission_file(filename):
    """
    Read plugin guide file , look for the permissions table in it, and parse it into a dict in the following format:
    {
        'service_id': 'plugin_id path file',
        'fields': {
            'permission_name': ['description1', 'description2']
            'permission_name2': ['description1', 'description2']
            ...
        }
    }
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data =f.read()
    html_data = markdown.markdown(data).replace('\n', '')
    soup = BeautifulSoup(html_data, "html.parser")

    permissions_dict = {
        'service_id': filename.split('.md')[0],
        'fields': {}
    }

    permissions_table = find_permissions_table_by_anchor(soup)
    if not permissions_table:
        print(f"Warning: Could not find permissions table in {filename}")
        return permissions_dict

    header_row = permissions_table.find('tr')
    if not header_row:
        print(f"Warning: Could not find header row in {filename}")
        return permissions_dict

    table_header_cells = header_row.find_all('th')
    if not is_template_header_format(table_header_cells):
        print(f"Warning: Unexpected column names in {filename}")
        return permissions_dict
    
    # Parse permission rows
    for row in permissions_table.find_all('tr')[1:]:  # Skip table header row
        permission_data = _parse_permission_row(row)
        if permission_data:
            permissions_dict['fields'][permission_data['permission']] =  permission_data['description']

    return permissions_dict

def filter_markdown_files(files: List[str], should_filter=True) -> List[str]:
    """Filter list of files to only include valid markdown plugin files.
    
    Args:
        files: List of file paths to filter
        should_filter: Whether to apply filtering rules
        
    Returns:
        List of valid markdown plugin files
    """
    if not should_filter:
        return files
        
    return [
        file for file in files 
        if (file.endswith('.md') and 
            file not in BLACKLIST_FILENAMES and 
            not file.startswith('.'))
    ]

def _write_jsons(jsons):
    """
    input: list of permissions dicts, where each dict has a service_id and fields dict
    output: write the permissions dicts to the output directory
    """
    if 0 == len(jsons):
        print("No permissions to write")
        return

    for elm in jsons:
        base_path = os.path.join(OUTPUT_DIR, os.path.split(elm['service_id'])[0])
        os.makedirs(base_path, exist_ok=True)
        file_path = os.path.join(OUTPUT_DIR, elm['service_id'] + '.json')
        try:
            with open(file_path, 'w') as output:
                output.write(json.dumps(elm))
        except Exception as exc:
            print("failed to generate JSON from file: " + str(file_path))
            print(str(exc))
            raise exc

def parse(changed_files: Optional[str] = None) -> None:
    """Process plugin files and generate permissions JSON.
    
    Args:
        changed_files: Optional string of newline-separated file paths to process.
                                                                    If None, exit.
    """
    if not changed_files:
        print("No changed files provided")
        return
        
    plugins_files = changed_files.split('\n')
    print(f"Processing files: {plugins_files}")
    
    valid_files = filter_markdown_files(plugins_files)
    if not valid_files:
        print("No valid markdown files found")
        return
        
    all_permissions = [
        _parse_permission_file(file) 
        for file in valid_files
    ]
    _write_jsons(all_permissions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process plugin files and generate permissions.')
    parser.add_argument('--changed-files', type=str, help='List of changed files, one per line')
    args = parser.parse_args()
    parse(args.changed_files)
