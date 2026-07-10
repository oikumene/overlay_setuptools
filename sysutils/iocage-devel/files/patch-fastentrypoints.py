--- fastentrypoints.py.orig	2025-12-12 22:04:57 UTC
+++ fastentrypoints.py
@@ -35,6 +35,7 @@ http://github.com/ninjaaron/fast-entry_points
 (c) 2016, Aaron Christianson
 http://github.com/ninjaaron/fast-entry_points
 '''
+from importlib import metadata
 from setuptools.command import easy_install
 import re
 TEMPLATE = '''\
@@ -59,13 +60,13 @@ def get_args(cls, dist, header=None):
         header = cls.get_header()
     for type_ in 'console', 'gui':
         group = type_ + '_scripts'
-        for name, ep in dist.get_entry_map(group).items():
+        for ep in metadata.entry_points(group=group, module="iocage_cli"):
             # ensure_safe_name
-            if re.search(r'[\\/]', name):
+            if re.search(r'[\\/]', ep.name):
                 raise ValueError("Path separators not allowed in script names")
             script_text = TEMPLATE.format(
-                          ep.module_name, ep.attrs[0], '.'.join(ep.attrs))
-            args = cls._get_script_args(type_, name, header, script_text)
+                          ep.module, ep.attr, ep.attr)
+            args = cls._get_script_args(type_, ep.name, header, script_text)
             for res in args:
                 yield res
 
