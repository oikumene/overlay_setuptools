--- setup.py.orig	2026-04-13 11:39:38 UTC
+++ setup.py
@@ -17,7 +17,7 @@ setup(
     packages=find_packages(),
     install_requires=['hidapi>=0.7.99', 'ecdsa>=0.9'],
     extras_require = {
-	'smartcard': [ 'python-pyscard>=1.6.12-4build1' ]
+	'smartcard': [ 'python-pyscard>=1.6.12' ]
     },
     include_package_data=True,
     zip_safe=False,
