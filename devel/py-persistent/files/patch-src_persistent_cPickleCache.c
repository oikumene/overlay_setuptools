--- src/persistent/cPickleCache.c.orig	2026-04-19 11:48:14 UTC
+++ src/persistent/cPickleCache.c
@@ -623,7 +623,7 @@ cc_oid_unreferenced(ccobject *self, PyObject *oid)
 
     dead_pers_obj = (cPersistentObject*)PyDict_GetItem(self->data, oid);
     assert(dead_pers_obj);
-    assert(dead_pers_obj->ob_refcnt == 0);
+    assert(Py_REFCNT(dead_pers_obj) == 0);
 
     dead_pers_obj_ref_to_self = (ccobject*)dead_pers_obj->cache;
     assert(dead_pers_obj_ref_to_self == self);
@@ -633,7 +633,7 @@ cc_oid_unreferenced(ccobject *self, PyObject *oid)
     */
 
     Py_INCREF(dead_pers_obj);
-    assert(dead_pers_obj->ob_refcnt == 1);
+    assert(Py_REFCNT(dead_pers_obj) == 1);
     /* Incremement the refcount again, because delitem is going to
         DECREF it.  If its refcount reached zero again, we'd call back to
         the dealloc function that called us.
@@ -662,7 +662,7 @@ cc_oid_unreferenced(ccobject *self, PyObject *oid)
     Py_DECREF(dead_pers_obj_ref_to_self);
     dead_pers_obj->cache = NULL;
 
-    assert(dead_pers_obj->ob_refcnt == 1);
+    assert(Py_REFCNT(dead_pers_obj) == 1);
 
     /* Don't DECREF the object, because this function is called from
         the object's dealloc function. If the refcnt reaches zero (again), it
