from pathlib import Path
from tools.sidebar_from_frontmatter import generate_sidebar
from tools.update_sidebar import update_sidebar


def test_generate_sidebar_and_update(tmp_path):
    wiki = tmp_path / "wiki"
    wiki.mkdir()

    # pages with different sections and weights
    (wiki / "a.md").write_text(
        """---
title: Tema A
path: a.md
section_path: Seccion/Uno
weight: 2
---
body""",
        encoding="utf-8",
    )
    (wiki / "b.md").write_text(
        """---
title: Tema B
path: b.md
section_path: Seccion/Uno
weight: 1
---
body""",
        encoding="utf-8",
    )
    (wiki / "c.md").write_text(
        """---
title: Root
path: c.md
weight: 3
---
body""",
        encoding="utf-8",
    )
    (wiki / "skip.md").write_text(
        """---
title: Skip
path: skip.md
visible: false
---
ignore""",
        encoding="utf-8",
    )

    auto_text = generate_sidebar(wiki)
    auto_file = tmp_path / "sidebar" / "_auto_index.md"
    auto_file.parent.mkdir()
    auto_file.write_text(auto_text, encoding="utf-8")

    sidebar = tmp_path / "_sidebar.md"
    sidebar.write_text(
        """<!-- AUTO-GENERATED BLOCK -->\n<!-- BEGIN: AUTO -->\nold\n<!-- END: AUTO -->\n\n<!-- BEGIN: MANUAL -->\nmanual\n<!-- END: MANUAL -->\n""",
        encoding="utf-8",
    )

    update_sidebar(sidebar, auto_file)
    lines = sidebar.read_text(encoding="utf-8").splitlines()
    assert "old" not in lines
    # manual block untouched
    manual_index = lines.index("<!-- BEGIN: MANUAL -->")
    assert lines[manual_index + 1] == "manual"
    # check ordering and hierarchy
    assert lines[2] == "* Seccion"
    assert lines[3] == "  * Uno"
    assert lines[4] == "    * [Tema B](b.md)"
    assert lines[5] == "    * [Tema A](a.md)"
    assert lines[6] == "* [Root](c.md)"
