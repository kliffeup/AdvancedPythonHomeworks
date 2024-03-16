import os

from latex_doc_generation import generate_image_code, generate_latex_doc, generate_table_code


if __name__ == "__main__":
    # table code
    test_table = [
        [1, None, ...], 
        [False, "KEKW", "OMEGALUL"],
        [13.37, 3 + 22j, "KEKWait"],
    ]

    table_latex_code = generate_table_code(test_table)

    # image code 
    test_image_path = os.path.join(".", "images", "ayanami-rei.png")

    image_latex_code, image_latex_user_packages = generate_image_code(test_image_path)

    # combine all
    latex_code = generate_latex_doc(table_latex_code, image_latex_code, user_packages=(image_latex_user_packages, ))
    latex_file_path = os.path.join(".", "artifacts", "table_image.tex")
    
    with open(latex_file_path, mode="w+") as latex_file:
        latex_file.write(latex_code)
