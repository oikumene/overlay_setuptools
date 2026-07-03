--- tree_sitter/__init__.py.orig	2023-11-13 05:21:18 UTC
+++ tree_sitter/__init__.py
@@ -115,10 +115,12 @@ class Language:
                         extra_preargs=flags,
                     )[0]
                 )
+            flags =["-shared", "-fPIC"]
             compiler.link_shared_object(
                 object_paths,
                 output_path,
                 target_lang="c++" if cpp else "c",
+                extra_preargs=flags,
             )
         return True
 
