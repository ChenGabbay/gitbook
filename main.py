import json
import os
from typing import Dict, List, Optional
import markdown
from bs4 import BeautifulSoup
import argparse

### CONSTS ###
BLACKLIST_FILENAMES = ['template.md', 'readme.md']
OUTPUT_DIR = './output'  # assume empty library in this path


def _get__permissions_table_after_heading(soup: BeautifulSoup,
                                          heading_text: str) -> Optional[BeautifulSoup]:
    """Find a table that follows a specific heading."""
    anchor = soup.find('a', id='h_0bb427264a')
    if anchor and anchor.parent and 'Required permissions' in anchor.parent.text:
        return anchor.parent.find_next('table')
    return None

def _validate_table_columns(header_cells: List[BeautifulSoup], expected_columns: List[str]) -> bool:
    """Validate that the table has the expected column names."""
    if len(header_cells) != len(expected_columns):
        return False
    return all(cell.text.strip() == expected for cell, expected in
                                                    zip(header_cells, expected_columns))

def _parse_permission_row(row: BeautifulSoup) -> Optional[Dict[str, str]]:
    """Parse a single permission row from the table."""
    cells = row.find_all('td')
    if len(cells) < 2:
        return None
    return {
        'permission': cells[0].text.strip(),
        'description': cells[1].get_text(separator='\n').strip()
    }

def _parse_permission_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data =f.read()
    html_data = markdown.markdown(data).replace('\n', '')
    soup = BeautifulSoup(html_data, "html.parser")

    permissions_dict = {
        'service_id': filename.split('.md')[0],
        'fields': {}
    }


    permissions_table = _get__permissions_table_after_heading(soup, 'Required permissions <a href="#h_0bb427264a" id="h_0bb427264a"></a>')
    if not permissions_table:
        print(f"Warning: Could not find permissions table in {filename}")
        return permissions_dict
    header_row = permissions_table.find('tr')

    if not header_row:
        print(f"Warning: Could not find header row in {filename}")
        return permissions_dict

    header_cells = header_row.find_all('th')
    expected_columns = ['Permission', 'Description']
    if not _validate_table_columns(header_cells, expected_columns):
        print(f"Warning: Unexpected column names in {filename}. Expected {expected_columns},"
              f"got {[cell.text.strip() for cell in header_cells]}")
        return permissions_dict
    # Parse permission rows
    for row in permissions_table.find_all('tr')[1:]:  # Skip header row
        permission_data = _parse_permission_row(row)
        if permission_data:
            permissions_dict['fields'][permission_data['permission']] = [
                                                permission_data['description']]

    return permissions_dict

def _list_files(dir_namer, filter_files=True):
    raw_files = os.listdir(dir_namer)
    files = []
    for temp_file in raw_files:
        if filter_files and \
                (temp_file in BLACKLIST_FILENAMES or temp_file.startswith('.') or not temp_file.endswith('.md')):
            continue

        files.append(os.path.join(dir_namer, temp_file))

    return files

def filter_files(files: List[str], filter_files=True):
    if filter_files:
        files = [file for file in files if file not in BLACKLIST_FILENAMES and not file.startswith('.') and file.endswith('.md')]
    return files

def _write_jsons(jsons):
    if 0 == len(jsons):
        return

    base_path = os.path.join(OUTPUT_DIR, os.path.split(jsons[0]['service_id'])[0])
    os.makedirs(base_path)
    for elm in jsons:
        file_path = os.path.join(OUTPUT_DIR, elm['service_id'] + '.json')
        try:
            with open(file_path, 'w') as output:
                output.write(json.dumps(elm))
        except Exception as exc:
            print("failed to generate JSON from file: " + str(file_path))
            print(str(exc))
            raise exc

def parse(changed_files=None):
   if changed_files:
       plugins_files = changed_files.split('\n')
       plugins_files = filter_files(plugins_files)
   else:
       print("No changed files provided")
       return
   
   all_permissions = []
   for temp_plugin_filename in plugins_files:
        all_permissions.append(_parse_permission_file(temp_plugin_filename))
   _write_jsons(all_permissions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process plugin files and generate permissions.')
    parser.add_argument('--changed-files', type=str, help='List of changed files, one per line')
    args = parser.parse_args()
    parse(args.changed_files)
