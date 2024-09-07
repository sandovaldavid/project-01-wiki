import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def markdown_to_html_v1(markdown):
    # Convert headings
    markdown = re.sub(r'(^|\n)###### (.*)', r'\1<h6>\2</h6>', markdown)
    markdown = re.sub(r'(^|\n)##### (.*)', r'\1<h5>\2</h5>', markdown)
    markdown = re.sub(r'(^|\n)#### (.*)', r'\1<h4>\2</h4>', markdown)
    markdown = re.sub(r'(^|\n)### (.*)', r'\1<h3>\2</h3>', markdown)
    markdown = re.sub(r'(^|\n)## (.*)', r'\1<h2>\2</h2>', markdown)
    markdown = re.sub(r'(^|\n)# (.*)', r'\1<h1>\2</h1>', markdown)

    # Convert bold text
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown)

    # Convert unordered lists
    markdown = re.sub(r'(^|\n)- (.*)', r'\1<ul>\n<li>\2</li>\n</ul>', markdown)
    markdown = re.sub(r'</ul>\n<ul>', '', markdown)  # Merge consecutive <ul> tags

    # Convert links
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    # Convert paragraphs
    markdown = re.sub(r'(^|\n)([^\n<].*?)(\n|$)', r'\1<p>\2</p>\3', markdown)

    return markdown

def test_markdown_to_html():
    # Test headings
    assert markdown_to_html_v1("# Heading 1") == "<h1>Heading 1</h1>"
    assert markdown_to_html_v1("## Heading 2") == "<h2>Heading 2</h2>"

    # Test bold text
    assert markdown_to_html_v1("**bold**") == "<strong>bold</strong>"

    # Test unordered lists
    assert markdown_to_html_v1("- item 1") == "<ul>\n<li>item 1</li>\n</ul>"

    # Test links
    assert markdown_to_html_v1("[link](http://example.com)") == '<a href="http://example.com">link</a>'

    # Test paragraphs
    assert markdown_to_html_v1("Paragraph text") == "<p>Paragraph text</p>"

    print("All tests passed.")
