--- fastentrypoints.py.orig	2021-12-19 20:26:39 UTC
+++ fastentrypoints.py
@@ -35,6 +35,7 @@ http://github.com/ninjaaron/fast-entry_points
 (c) 2016, Aaron Christianson
 http://github.com/ninjaaron/fast-entry_points
 '''
+from importlib.metadata import entry_points
 from setuptools.command import easy_install
 import re
 TEMPLATE = r'''\
@@ -59,17 +60,17 @@ def get_args(cls, dist, header=None):
     """
     if header is None:
         header = cls.get_header()
-    spec = str(dist.as_requirement())
+    spec = f'{dist.name}=={dist.version}'
     for type_ in 'console', 'gui':
         group = type_ + '_scripts'
-        for name, ep in dist.get_entry_map(group).items():
+        for ep in entry_points(group=group, name='thefuck'):
             # ensure_safe_name
-            if re.search(r'[\\/]', name):
+            if re.search(r'[\\/]', ep.name):
                 raise ValueError("Path separators not allowed in script names")
             script_text = TEMPLATE.format(
-                          ep.module_name, ep.attrs[0], '.'.join(ep.attrs),
-                          spec, group, name)
-            args = cls._get_script_args(type_, name, header, script_text)
+                          ep.module, ep.attr, ep.attr,
+                          spec, group, ep.name)
+            args = cls._get_script_args(type_, ep.name, header, script_text)
             for res in args:
                 yield res
 
