make -f autotools.mk
./configure
make
cp rabinpoly.py python/rabinpoly.py
cp rabinpoly.py test/rabinpoly.py
make test
sudo make install
