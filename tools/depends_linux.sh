mkdir /tmp/depends/
cd /tmp/depends

echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка необходимых инструментов"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
sudo pacman -S wget unzip pandoc python-pipx

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
    sudo tlmgr install tcolorbox hyperref amsmath setspace indentfirst array minted vmargin babel-russian cm-super hyphen-russian
    sudo fmtutil-sys --all
    sudo tlmgr install lh
    pipx install pygments
    rm -rf install-tl-*
else
    echo "Latex уже установлен"
fi


echo ""
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo "Установка FiraCode Nerd Font"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
if ! [[ $(fc-list | grep "FiraCode") ]]; then
    rm -rf /tmp/fonts
    rm -rf FiraCode.zip*

    wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/FiraCode.zip
    unzip FiraCode.zip -d fonts
    rm -rf FiraCode.zip*
    cd fonts
    sudo cp *.ttf /usr/share/fonts
else
    echo "Шрифт FiraCode Nerd Font уже есть"
fi

echo ""
echo "~~~~~~~~~~~"
echo "Все готово!"
echo "~~~~~~~~~~~"
