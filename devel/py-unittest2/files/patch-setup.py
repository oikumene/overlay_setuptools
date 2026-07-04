--- setup.py.orig	2015-06-30 06:47:44 UTC
+++ setup.py
@@ -57,11 +57,11 @@ KEYWORDS = "unittest testing tests".split(' ')
 # Both install and setup requires - because we read VERSION from within the
 # package, and the package also exports all the APIs.
 # six for compat helpers
-REQUIRES = ['argparse', 'six>=1.4', 'traceback2'],
+REQUIRES = ['six>=1.4', 'traceback2'],
 
 params = dict(
     name=NAME,
-    version=VERSION,
+    version=str(VERSION),
     description=DESCRIPTION,
     long_description=LONG_DESCRIPTION,
     packages=PACKAGES,
