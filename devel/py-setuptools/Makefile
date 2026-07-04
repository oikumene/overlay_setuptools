PORTNAME=	setuptools
DISTVERSION=	81.0.0
CATEGORIES=	devel python
MASTER_SITES=	PYPI
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}
DIST_SUBDIR=	python

# note: before committing a new major version, contact portmgr to
# arrange for an experimental ports run. Untested commits may be
# backed out.
MAINTAINER=	python@FreeBSD.org
COMMENT=	Python packages installer
WWW=		https://setuptools.pypa.io/

LICENSE=	MIT
LICENSE_FILE=	${WRKSRC}/LICENSE

BUILD_DEPENDS=	${_CORE_DEPENDS}
RUN_DEPENDS=	${_CORE_DEPENDS}

USES=		cpe python
CPE_VENDOR=	python
USE_PYTHON=	allflavors autoplist concurrent pep517 pytest

_CORE_DEPENDS=	${PYTHON_PKGNAMEPREFIX}packaging>=24.2:devel/py-packaging@${PY_FLAVOR} \
		${PYTHON_PKGNAMEPREFIX}more-itertools>=8.8:devel/py-more-itertools@${PY_FLAVOR} \
		${PY_TOMLI} \
		${PYTHON_PKGNAMEPREFIX}wheel>=0.43.0:devel/py-wheel@${PY_FLAVOR}

# circular dependencies
#_CORE_DEPENDS=	${PYTHON_PKGNAMEPREFIX}jaraco.text>=3.7:devel/py-jaraco.text@${PY_FLAVOR} \
#		${PYTHON_PKGNAMEPREFIX}platformdirs>=4.2.2:devel/py-platformdirs@${PY_FLAVOR} \
#		${PYTHON_PKGNAMEPREFIX}jaraco.functools>=4:devel/py-jaraco.functools@${PY_FLAVOR}

# remove vendored packages of those already installed via pkg(8)
_DIST_EXCLUDES=	packaging* \
		more_itertools* \
		wheel* \
		tomli* \
		typing_extensions* \
		importlib_metadata* \
		zipp*
EXTRACT_AFTER_ARGS=	${_DIST_EXCLUDES:S,^,--exclude setuptools/_vendor/,}

NO_ARCH=	yes

.include <bsd.port.mk>
