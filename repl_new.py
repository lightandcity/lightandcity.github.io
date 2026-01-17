import os
import shutil

# ===== 설정부 =====
ROOT_DIR = r"C:\Users\user\Desktop\빛과도시\홈페이지\latest\lightandcity.github.io"
TARGET_EXTENSIONS = (".html", ".js", ".css")

OLD_BLOCK = """
            ADDRESS
            <span style="letter-spacing: 5px;">
            </span>
            경기도 화성시 동탄중심상가1길 36, (반송동, 원영빌딩) 8층 801-J54호
            <br/>
            MAIL
            <span style="letter-spacing: 5px;">
            </span>
            business@lightandcity.r-e.kr
            <br/>
            TEL
            <span style="letter-spacing: 5px;">
            </span>
            070-5236-0730
            <br/>
            FAX
            <span style="letter-spacing: 5px;">
            </span>
            0504-168-6073
           </p>
"""
NEW_BLOCK = """
            ADDRESS
            <span style="letter-spacing: 5px;">
            </span>
            경기도 화성시 동탄중심상가1길 36, (반송동, 원영빌딩) 8층 801-J54호
            <br/>
            사업자등록번호
            <span style="letter-spacing: 5px;">
            </span>
            645-86-04462 (공학연구개발업, 기타엔지니어링서비스업)
            <br/>
            MAIL
            <span style="letter-spacing: 5px;">
            </span>
            business@lightandcity.r-e.kr
            <br/>
            TEL
            <span style="letter-spacing: 5px;">
            </span>
            070-5236-0730
            <br/>
            FAX
            <span style="letter-spacing: 5px;">
            </span>
            0504-168-6073
           </p>
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
