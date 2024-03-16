from typing import Any, List, Optional, Tuple


def get_column_count(table: List[List[Any]]) -> int:
    return max(max(map(len, table)), 1)


def generate_table_str_representation(table: List[List[Any]]) -> str:
    return r" \\".join(
        " & ".join(map(str, row)) 
        for row in table
    ) + r" \\"


def generate_table_code(table: List[List[Any]]) -> str:
    TABLE_LATEX_TEMPLATE = """
\\begin{center}
\\begin{tabular}{ %s } 
\\hline
%s
\\hline
\\end{tabular}
\\end{center}
"""
    
    column_count = get_column_count(table)
    column_formatter = "|c" * column_count + "|"
    table_str_representation = generate_table_str_representation(table)
    
    return (TABLE_LATEX_TEMPLATE % (column_formatter, table_str_representation)).strip()


def generate_image_code(image_path: str) -> Tuple[str, str]:
    IMAGE_INSERT_LATEX_TEMPLATE = """
\\begin{center}
\\includegraphics[width=10cm, height10cm]{%s}
\\end{center}
"""
    IMAGE_INSERT_USER_PACKAGES = r"\usepackage{graphicx}"
    image_code = (IMAGE_INSERT_LATEX_TEMPLATE % image_path).strip()

    return image_code, IMAGE_INSERT_USER_PACKAGES


def generate_latex_doc(*latex_code_parts: Tuple[str, ...], user_packages: Optional[Tuple[str, ...]] = None) -> str:
    LATEX_DOC_TEMPLATE = """
\\documentclass{article}
%s
\\begin{document}
%s
\\end{document}
"""

    latex_user_packages = "\n".join(user_packages) if user_packages else ""
    latex_code = "\n".join(latex_code_parts)

    return (LATEX_DOC_TEMPLATE % (latex_user_packages, latex_code)).strip()
