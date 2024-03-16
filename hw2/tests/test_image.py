import os

from src.latex_doc_generation import generate_image_code, generate_latex_doc


if __name__ == "__main__":
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_image_path = os.path.join("images", "ayanami-rei.png")

    image_latex_code, image_latex_user_packages = generate_image_code(test_image_path)
    latex_code = generate_latex_doc(image_latex_code, user_packages=(image_latex_user_packages, ))

    latex_file_path = os.path.join(dir_path, "artifacts", "image.tex")
    
    with open(latex_file_path, mode="w+") as latex_file:
        latex_file.write(latex_code)
