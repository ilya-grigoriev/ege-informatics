@ECHO OFF
REM change CHCP to UTF-8
CHCP 65001
cls
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка необходимых инструментов
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
choco install wget unzip -y

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Установка AnonymicePro Nerd Font
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cd C:\Windows\Temp
wget https://github.com/ryanoasis/nerd-fonts/releases/download/v3.1.1/AnonymousPro.zip
unzip -o AnonymousPro.zip -d fonts
cd fonts
copy /Y *.ttf "C:\Windows\Fonts"

echo ~~~~~~~~~~~~~~~~~~
echo Установка языка R
echo ~~~~~~~~~~~~~~~~~~
wget https://cloud.r-project.org/bin/windows/base/R-4.3.2-win.exe
call R-4.3.2-win.exe

echo ~~~~~~~~~~~~~~~~~~~
echo Установка RMarkdown
echo ~~~~~~~~~~~~~~~~~~~
cd "C:\Program Files\R\R-4.3.2\bin"
Rscript.exe -e "install.packages('fastmap', repos='https://cloud.r-project.org')"
Rscript.exe -e "install.packages('rmarkdown', repos='https://cloud.r-project.org')"

echo ~~~~~~~~~~~~~~~~~~~~~~~~~~
echo Удаление остаточных файлов
echo ~~~~~~~~~~~~~~~~~~~~~~~~~~
cd C:\Windows\Temp
del AnonymousPro.zip*
del R-4.3.2-win.exe*
rmdir fonts /S /Q

echo ~~~~~~~~~~~
echo Все готово!
echo ~~~~~~~~~~~
@ECHO ON