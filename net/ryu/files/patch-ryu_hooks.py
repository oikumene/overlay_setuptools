--- ryu/hooks.py.orig	2026-04-15 06:02:21 UTC
+++ ryu/hooks.py
@@ -33,7 +33,7 @@ def save_orig():
     """Save original easy_install.get_script_args.
     This is necessary because pbr's setup_hook is sometimes called
     before ours."""
-    _main_module()._orig_get_script_args = easy_install.get_script_args
+    _main_module()._orig_get_script_args = easy_install.ScriptWriter._get_script_args
 
 
 def setup_hook(config):
@@ -57,7 +57,7 @@ def setup_hook(config):
         return _main_module()._orig_get_script_args(*args, **kwargs)
 
     packaging.override_get_script_args = my_get_script_args
-    easy_install.get_script_args = my_get_script_args
+    easy_install.ScriptWriter._get_script_args = my_get_script_args
 
     # another hack to allow setup from tarball.
     orig_get_version = packaging.get_version
