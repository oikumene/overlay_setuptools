--- setup.py.orig	2026-07-02 20:27:48 UTC
+++ setup.py
@@ -53,7 +53,7 @@ setup(
     packages=find_packages(exclude=['tests']),
     package_dir={'': '.'},
     test_suite='tests',
-    python_requires='>=3.6.*',
+    python_requires='>=3.6',
     include_package_data=True,
     data_files=DATA_FILES,
     install_requires=[
