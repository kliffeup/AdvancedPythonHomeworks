import os

from src.latex_doc_generation import generate_table_code, generate_latex_doc


if __name__ == "__main__":
    test_table = [
        [1, None, ...], 
        [False, "KEKW", "OMEGALUL"],
        [13.37, 3 + 22j, "KEKWait"],
    ]

    table_latex_code = generate_table_code(test_table)
    latex_code = generate_latex_doc(table_latex_code)

    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    latex_file_path = os.path.join(dir_path, "artifacts", "table.tex")
    
    with open(latex_file_path, mode="w+") as latex_file:
        latex_file.write(latex_code)
