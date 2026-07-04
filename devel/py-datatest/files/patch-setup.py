--- setup.py.orig	2026-07-02 08:57:07 UTC
+++ setup.py
@@ -139,7 +139,7 @@ if __name__ == '__main__':
             ],
             # Additional fields:
             install_requires=[],  # <- No hard requirements!
-            python_requires='>=2.6.*, !=3.0.*, !=3.1.*',
+            python_requires='>=2.6,!=3.0,!=3.1',
             description='Test driven data-wrangling and data validation.',
             long_description=long_description,
             author='Shawn Brown',
