"""Barcha daftarlarni ishga tushirib tekshirish: birorta katakda xato bo'lsa, dastur xato bilan tugaydi."""
import glob, sys
import nbformat as nbf
from nbclient import NotebookClient

xatolar = []
for yol in sorted(glob.glob("[0-9][0-9]-bob/*.ipynb")):
    nb = nbf.read(yol, as_version=4)
    try:
        NotebookClient(nb, timeout=1200, kernel_name="python3").execute()
        print("OK   ", yol, flush=True)
    except Exception as e:
        xatolar.append(yol)
        print("XATO ", yol, "\n", str(e)[-1500:], flush=True)
print(f"\n{len(xatolar)} ta daftarda xato topildi")
sys.exit(1 if xatolar else 0)
