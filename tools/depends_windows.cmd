@ECHO OFF
:: change CHCP to UTF-8
CHCP 65001
cls
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка необходимых инструментов
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
choco install wget unzip pandoc python312 -y

echo ~~~~~~~~~~~~~~~
echo Установка Latex
echo ~~~~~~~~~~~~~~~
rmdir /s /q install-tl-*
rmdir /s /q C:\texlive
wget http://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe
call install-tl-windows.exe --scheme scheme-medium
mkdir C:\texlive\2024\texmf-var\fonts\cache
del install-tl-windows.exe*
tlmgr install framed tcolorbox babel-russian cm-super fontenc inputenc hyperref setspace indentfirst array

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка AnonymicePro Nerd Font
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
del AnonymousPro.zip*
cd C:\Windows\Temp
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/AnonymousPro.zip
unzip AnonymousPro.zip -d fonts
cd fonts
copy /Y *.ttf "C:\Windows\Fonts"
cd ..

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка шрифтов для Latex
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~
mkdir C:\texlive\2024\texmf-var\fonts\conf
cd C:\texlive\2024\texmf-var\fonts\conf
echo ^<dir^>C:/Windows/Fonts^</dir^> > fonts.conf
fc-cache -vf

echo ~~~~~~~~~~~~~~~~~~
echo Установка языка R
echo ~~~~~~~~~~~~~~~~~~
cd C:\Windows\Temp
wget https://cloud.r-project.org/bin/windows/base/R-4.4.0-win.exe
call R-4.4.0-win.exe

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка переменных окружения для R
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
set PATH=%PATH%;"C:\Program Files\R\R-4.4.0\bin"

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка RMarkdown и необходимых компонентов для его работы
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Rscript -e "install.packages('fastmap', repos='https://cloud.r-project.org')"
Rscript -e "install.packages('rmarkdown', repos='https://cloud.r-project.org')"
Rscript -e "install.packages('reticulate', repos='https://cloud.r-project.org')"
Rscript -e "reticulate::virtualenv_remove()"
Rscript -e "reticulate::virtualenv_create()"

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Удаление остаточных файлов
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~
cd C:\Windows\Temp
del AnonymousPro.zip*
del R-4.4.0-win.exe*
rmdir fonts /S /Q

echo ~~~~~~~~~~~
echo Все готово!
echo ~~~~~~~~~~~
@ECHO ON
