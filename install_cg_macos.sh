#!/bin/bash
mkdir -p ~/.tmp/cg_installer
cd ~/.tmp/cg_installer
echo "Downloading apertium + cg3"
curl https://apertium.projectjj.com/osx/nightly/apertium-all-dev.tar.bz2 -o cg3.tar.bz2
tar xjf cg3.tar.bz2
echo "Extracting cg3"
echo "Copying cg3"
cp -rf ./apertium-all-dev/bin/* /usr/local/bin/
cp -f ./apertium-all-dev/bin/vislcg3 /usr/local/bin/cg3
cp -rf ./apertium-all-dev/include/* /usr/local/include/
cp -rf ./apertium-all-dev/lib/* /usr/local/lib/
cp -rf ./apertium-all-dev/share/* /usr/local/share/
echo "Cleaning up"
cd
rm -rf ~/.tmp/cg_installer