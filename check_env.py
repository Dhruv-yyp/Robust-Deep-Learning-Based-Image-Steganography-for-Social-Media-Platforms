"""
SETUP AND RUN GUIDE
===================
Run this script first to check your environment.
"""
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REQUIRED = [
    ("streamlit", "streamlit"),
    ("opencv-python-headless", "cv2"),
    ("Pillow", "PIL"),
    ("numpy", "numpy"),
    ("scipy", "scipy"),
    ("scikit-image", "skimage"),
    ("PyWavelets", "pywt"),
    ("torch", "torch"),
    ("torchvision", "torchvision"),
]


def main():
    print("=" * 50)
    print("StegaGuard - Environment Checker")
    print("=" * 50)
    print(f"\n[OK] Python version: {sys.version}")

    missing = []
    for package_name, import_name in REQUIRED:
        try:
            __import__(import_name)
            print(f"[OK] {package_name} - installed")
        except ImportError:
            print(f"[MISSING] {package_name}")
            missing.append(package_name)

    if missing:
        print(f"\nMissing packages: {missing}")
        print("Run: pip install -r requirements.txt")
        return 1

    print("\nAll packages installed. You're ready to run.")
    print("\nTo start the app:")
    print("  streamlit run app/streamlit_app.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
