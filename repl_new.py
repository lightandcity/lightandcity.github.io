import os
import shutil

# ===== 설정부 =====
ROOT_DIR = r"C:\Users\user\Desktop\빛과도시\홈페이지\latest\lightandcity.github.io"
TARGET_EXTENSIONS = (".html", ".js", ".css")

OLD_BLOCK = """E-MAIL"""
NEW_BLOCK = """MAIL"""

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
