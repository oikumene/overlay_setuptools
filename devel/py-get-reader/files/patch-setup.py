--- setup.py.orig	2026-07-01 09:53:20 UTC
+++ setup.py
@@ -45,7 +45,7 @@ setuptools.setup(
     long_description=get_long_description('README.md'),
     long_description_content_type='text/markdown',
     license='Apache 2.0',
-    python_requires='>=2.6.*, !=3.0.*, !=3.1.*',
+    python_requires='>=2.6,!=3.0,!=3.1',
     classifiers=[
         'License :: OSI Approved :: Apache Software License',
         'Development Status :: 5 - Production/Stable',
