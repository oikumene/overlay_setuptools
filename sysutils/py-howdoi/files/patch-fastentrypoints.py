--- fastentrypoints.py.orig	2021-07-30 16:10:51 UTC
+++ fastentrypoints.py
@@ -38,6 +38,7 @@ http://github.com/ninjaaron/fast-entry_points
 (c) 2016, Aaron Christianson
 http://github.com/ninjaaron/fast-entry_points
 '''
+from importlib import metadata
 from setuptools.command import easy_install
 import re
 TEMPLATE = r'''
@@ -63,18 +64,18 @@ def get_args(cls, dist, header=None):  # noqa: D205,D4
     if header is None:
         # pylint: disable=E1101
         header = cls.get_header()
-    spec = str(dist.as_requirement())
+    spec = f'{dist.name}=={dist.version}'
     for type_ in 'console', 'gui':
         group = type_ + '_scripts'
-        for name, ep in dist.get_entry_map(group).items():
+        for ep in metadata.entry_points(group=group, name="howdoi"):
             # ensure_safe_name
-            if re.search(r'[\\/]', name):
+            if re.search(r'[\\/]', ep.name):
                 raise ValueError("Path separators not allowed in script names")
             script_text = TEMPLATE.format(
-                ep.module_name, ep.attrs[0], '.'.join(ep.attrs),
-                spec, group, name)
+                ep.module, ep.attr, ep.attr,
+                spec, group, ep.name)
             # pylint: disable=E1101
-            args = cls._get_script_args(type_, name, header, script_text)
+            args = cls._get_script_args(type_, ep.name, header, script_text)
             for res in args:
                 yield res
 
