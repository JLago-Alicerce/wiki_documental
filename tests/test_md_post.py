from wiki_documental.processing.md_post import (
    post_process_text,
    clean_markdown,
    fix_image_links,
    warn_missing_images,
)


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


def test_fix_image_links_and_warning(tmp_path, capsys):
    text = '![a](media/img.png) and ![](../media/img2.jpg)'
    assets = tmp_path / 'assets' / 'media'
    assets.mkdir(parents=True)
    (assets / 'img.png').write_text('x', encoding='utf-8')

    fixed = fix_image_links(text)
    warn_missing_images(fixed, tmp_path)
    captured = capsys.readouterr()
    assert 'assets/media/img.png' in fixed
    assert '../media/img2.jpg' in fixed
    assert 'img2.jpg' not in captured.out


def test_fix_image_links_no_duplicate():
    text = '![alt](assets/media/img.png)'
    assert fix_image_links(text) == text
