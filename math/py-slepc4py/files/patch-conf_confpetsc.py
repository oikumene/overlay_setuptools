--- conf/confpetsc.py.orig	2026-07-03 17:57:26 UTC
+++ conf/confpetsc.py
@@ -658,7 +658,7 @@ class build_ext(_build_ext):
                 fh.write(config_data)
         execute(write_file, (config_file, config_data),
                 msg='writing %s' % config_file,
-                verbose=self.verbose, dry_run=self.dry_run)
+                verbose=self.verbose)
 
     def get_config_data(self, arch_list):
         DESTDIR = self.DESTDIR
