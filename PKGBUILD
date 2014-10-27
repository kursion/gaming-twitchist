# PKGBUILD for twitch streams list

# Maintainer: Yves Lange <kursion@gmail.com>
pkgname=twilist
pkgver=0.1
pkgrel=1
pkgdesc="A little to that parse and show the streams on twitch. Open it
with you favorite browser."
arch=()
url=""
license=('GPL')
groups=()
depends=('python')
makedepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
install=
source=()
md5sums=()

package() {
    cd "$srcdir/$pkgname-$pkgver"
      python setup.py install --root="$pkgdir/" --optimize=1
    }

