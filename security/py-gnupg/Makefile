PORTNAME=	gnupg
PORTVERSION=	3.1.1
PORTREVISION=	2
CATEGORIES=	security python
PKGNAMEPREFIX=	${PYTHON_PKGNAMEPREFIX}

MAINTAINER=	cs@FreeBSD.org
COMMENT=	Python wrapper for GnuPG
WWW=		https://github.com/isislovecruft/python-gnupg

LICENSE=	GPLv3

RUN_DEPENDS=	${PYTHON_PKGNAMEPREFIX}psutil>=0.5.1:sysutils/py-psutil@${PY_FLAVOR}

USES=		python
USE_GITHUB=	yes
USE_PYTHON=	distutils autoplist

GH_ACCOUNT=	isislovecruft
GH_PROJECT=	python-gnupg

NO_ARCH=	yes

post-patch:
	${REINPLACE_CMD} \
		-e 's|\(git_refnames =\).*$$|\1 "${PORTVERSION}"|' \
		-e 's|\(git_full =\).*$$|\1 "${PORTVERSION}"|' \
		${WRKSRC}/pretty_bad_protocol/_version.py

.include <bsd.port.mk>
