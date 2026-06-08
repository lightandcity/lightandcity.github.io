import os
import shutil

# ===== 설정부 =====
ROOT_DIR = r"C:\Users\Kwon\Desktop\real_github\lightandcity.github.io"
TARGET_EXTENSIONS = (".html", ".js", ".css")

OLD_BLOCK = """
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_white_low.png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="216.666666667"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_white_low.png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="216.666666667"/>
"""
NEW_BLOCK = """
                <img alt="주식회사 빛과도시" class="normal_logo _front_img" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
                <img alt="주식회사 빛과도시" class="scroll_logo fixed_transform" src="https://raw.githubusercontent.com/lightandcity/lightandcity.github.io/refs/heads/main/logo/%EB%B9%9B%EA%B3%BC%EB%8F%84%EC%8B%9C_%EA%B0%80%EB%A1%9C%EB%A1%9C%EA%B3%A0_20260608_Image(2).png" style="max-width: 100%;height: auto; image-rendering: -webkit-optimize-contrast;" width="180"/>
"""

BACKUP = True
# =================


def replace_block_in_file(file_path, old_block, new_block, backup=True):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if old_block not in content:
        return

    if backup:
        shutil.copy(file_path, file_path + ".bak")

    content = content.replace(old_block, new_block)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[REPLACED] {file_path}")


def replace_block_in_folder(root_dir, old_block, new_block, backup=True):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(TARGET_EXTENSIONS):
                file_path = os.path.join(root, file)
                replace_block_in_file(
                    file_path,
                    old_block,
                    new_block,
                    backup
                )


if __name__ == "__main__":
    replace_block_in_folder(
        ROOT_DIR,
        OLD_BLOCK,
        NEW_BLOCK,
        BACKUP
    )
    print("✅ 블록 치환 완료")
