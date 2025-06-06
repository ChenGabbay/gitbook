from typing import Dict, List, Optional
import markdown
from bs4 import BeautifulSoup



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

if __name__ == '__main__':
    b = _parse_permission_file('plugins/page-1.md')
