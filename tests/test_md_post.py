from wiki_documental.processing.md_post import post_process_text, clean_markdown


def test_clean_and_spacing():
    long_dots = '.' * 130
    text = (
        'intro\n' + long_dots + '\nparagraph\n'
        '## Heading2\ncontent\n### Heading3\nend\n'
    )
    result = post_process_text(text)
    lines = result.splitlines()
    assert long_dots not in result
    idx_h2 = lines.index('## Heading2')
    idx_h3 = lines.index('### Heading3')
    assert lines[idx_h2 - 1] == ''
    assert lines[idx_h3 - 1] == ''


def test_heading_cleanup():
    text = '##  **Title**  \n###   Another   Title   \n'
    result = clean_markdown(text)
    lines = result.splitlines()
    assert lines[0] == '## Title'
    assert lines[1] == ''
    assert lines[2] == '### Another Title'
