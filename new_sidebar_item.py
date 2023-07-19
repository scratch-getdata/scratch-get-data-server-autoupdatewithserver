import os

# Define the file paths and corresponding names for the sidebar
file_paths = ["templates/index_test.html"]
names_in_sidebar = ["index_test.html home"]
frontend_urls = ["index_test.html /home"]


for file_path, name_in_sidebar, frontend_url in zip(file_paths, names_in_sidebar, frontend_urls):
    # Read the file contents
    with open(file_path, 'r') as f:
        file_contents = f.read()

    # Find the sidebar div and add the new line
    sidebar_start = file_contents.find('<div id="mySidebar" class="sidebar">')
    sidebar_end = file_contents.find('</div>', sidebar_start)
    sidebar_contents = file_contents[sidebar_start:sidebar_end]
    new_sidebar_contents = ""

    # Iterate over the names in the sidebar and add them to the new sidebar contents
    for line in sidebar_contents.split('\n'):
        if line.strip() == "":
            continue
        link_text = line[line.find('>')+1:line.find('</a>')]
        if link_text in names_in_sidebar:
            new_sidebar_contents += line

    # Add the new line to the sidebar if it is not already present
    if name_in_sidebar not in new_sidebar_contents:
        new_sidebar_contents += f'<a href="{frontend_url}" class="sidebar-link">{name_in_sidebar}</a>'

    # Replace the old sidebar contents with the new sidebar contents
    file_contents = file_contents[:sidebar_start] + new_sidebar_contents + file_contents[sidebar_end:]

    # Write the modified file contents back to the file
    with open(file_path, 'w') as f:
        f.write(file_contents)