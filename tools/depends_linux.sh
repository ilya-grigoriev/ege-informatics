mkdir /tmp/depends/
cd /tmp/depends

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка необходимых инструментов"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
sudo pacman -S wget unzip

echo ""
echo "~~~~~~~~~~~~~~~~~"
echo "Установка языка R"
echo "~~~~~~~~~~~~~~~~~"
sudo pacman -S r-base

echo ""
echo "~~~~~~~~~~~~~~~~~~~"
echo "Установка RMarkdown"
echo "~~~~~~~~~~~~~~~~~~~"
Rscript -e "install.packages('rmarkdown')"
Rscript -e "install.packages('reticulate')"
Rscript -e "reticulate::virtualenv_remove()"
Rscript -e "reticulate::virtualenv_create()"

echo ""
echo "~~~~~~~~~~~~~~~"
echo "Установка Latex"
echo "~~~~~~~~~~~~~~~"
sudo pacman -S pandoc
wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
zcat < install-tl-unx.tar.gz | tar xf -
rm -rf install-tl-unx.tar.gz*
cd install-tl-*
perl ./install-tl --no-interaction --scheme scheme-medium
tlmgr install tcolorbox hyperref amsmath setspace indentfirst array


echo ""
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка AnonymicePro Nerd Font"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/AnonymousPro.zip
unzip AnonymousPro.zip -d fonts
rm -rf AnonymousPro.zip
cd fonts
cp *.ttf /usr/share/fonts

echo ""
echo "~~~~~~~~~~~"
echo "Все готово!"
echo "~~~~~~~~~~~"
