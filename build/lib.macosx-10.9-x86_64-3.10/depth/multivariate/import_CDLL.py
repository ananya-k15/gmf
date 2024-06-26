import ctypes as ct
import multiprocessing as mp
import sys, os, glob


def import_CDLL():
    if sys.platform == "linux":
        for i in sys.path:
            if (
                i.split("/")[-1] == "site-packages"
                or i.split("/")[-1] == "dist-packages"
            ):  # Add search dist-packages
                de = glob.glob(i + "**/*ddalpha*.so", recursive=True)
                da = glob.glob(i + "**/*depth_wrapper*.so", recursive=True)
                if da != [] and de != []:
                    ddalpha_exact = glob.glob(i + "**/*ddalpha*.so", recursive=True)
                    ddalpha_approx = glob.glob(
                        i + "**/*depth_wrapper*.so", recursive=True
                    )
                else:
                    print(da, de)
        libr = ct.CDLL(ddalpha_exact[0])
        libRom = ct.CDLL(ddalpha_approx[0])

    if sys.platform == "darwin":
        for i in sys.path:
            if (
                i.split("/")[-1] == "site-packages"
                or i.split("/")[-1] == "dist-packages"
            ):  # Add search dist-packages
                de = glob.glob(i + "**/*ddalpha*.so", recursive=True)
                da = glob.glob(i + "**/*depth_wrapper*.so", recursive=True)
                if da != [] and de != []:
                    ddalpha_exact = glob.glob(i + "/*ddalpha*.so")
                    ddalpha_approx = glob.glob(i + "/*depth_wrapper*.so")
        libr = ct.CDLL(ddalpha_exact[0])
        libRom = ct.CDLL(ddalpha_approx[0])

    if sys.platform == "win32":
        site_packages = [
            p for p in sys.path if ("site-packages" in p) or ("dist-packages" in p)
        ]  # Add search dist-packages
        for i in site_packages:
            os.add_dll_directory(i)
            ddalpha_exact = glob.glob(i + "/depth/src/*ddalpha*.dll")
            ddalpha_approx = glob.glob(i + "/depth/src/*depth_wrapper*.dll")
            if ddalpha_exact + ddalpha_approx != []:
                libr = ct.CDLL(r"" + ddalpha_exact[0])
                libRom = ct.CDLL(r"" + ddalpha_approx[0])
    return libr, libRom


libr, libRom = import_CDLL()
