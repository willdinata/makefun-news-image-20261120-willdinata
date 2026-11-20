"""Hands the finished front page to the grader."""
import os
import shutil
import hashlib

def main():
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dst = os.path.join(out_dir, "entry.png")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copy2(src, dst)
    with open(dst, "rb") as f:
        data = f.read()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("Invalid PNG signature")
    print(f"Copied {len(data)} bytes. SHA-256: {hashlib.sha256(data).hexdigest()[:12]}")

if __name__ == "__main__":
    main()
