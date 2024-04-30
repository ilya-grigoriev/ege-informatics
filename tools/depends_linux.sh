mkdir /tmp/depends/
cd /tmp/depends

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка необходимых инструментов"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
sudo pacman -S wget unzip pandoc

echo ""
echo "~~~~~~~~~~~~~~~~~"
echo "Установка языка R"
echo "~~~~~~~~~~~~~~~~~"
sudo pacman -S r-base

echo ""
echo "~~~~~~~~~~~~~~~~~~~"
echo "Установка RMarkdown"
echo "~~~~~~~~~~~~~~~~~~~"
if ! [[ $(Rscript -e "system.file(package='rmarkdown')") ]]; then
    Rscript -e "install.packages('rmarkdown', repos='http://cran.us.r-project.org')"
    Rscript -e "install.packages('reticulate', repos='http://cran.us.r-project.org')"
    Rscript -e "reticulate::virtualenv_remove()"
    Rscript -e "reticulate::virtualenv_create()"
else
    echo "RMarkdown уже установлен"
fi

echo ""
echo "~~~~~~~~~~~~~~~"
echo "Установка Latex"
echo "~~~~~~~~~~~~~~~"
if ! [ -d "/usr/local/texlive" ]; then
    wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz
    zcat < install-tl-unx.tar.gz | tar xf -
    rm -rf install-tl-unx.tar.gz*
    cd install-tl-*
    sudo perl ./install-tl --no-interaction --scheme scheme-medium
    sudo tlmgr install tcolorbox hyperref amsmath setspace indentfirst array
    rm -rf install-tl-*
else
    echo "Latex уже установлен"
fi


echo ""
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка AnonymicePro Nerd Font"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
if ! [[ $(fc-list | grep "Anonymice") ]]; then
    rm -rf /tmp/fonts
    rm -rf AnonymousPro.zip*

    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/AnonymousPro.zip
    unzip AnonymousPro.zip -d fonts
    rm -rf AnonymousPro.zip*
    cd fonts
    sudo cp *.ttf /usr/share/fonts
else
    echo "Шрифт AnonymicePro Nerd Font уже есть"
fi

echo ""
echo "~~~~~~~~~~~"
echo "Все готово!"
echo "~~~~~~~~~~~"
