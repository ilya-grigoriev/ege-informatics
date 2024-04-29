@echo off
PATH=%PATH%;"C:\Program Files\R\R-4.4.0\bin\x64"
mkdir pdfs
for /F %%G in ('dir *.rmd /s /b') do (
set "F=%%G"
setlocal EnableDelayedExpansion
Rscript --encoding=UTF-8 -e "rmarkdown::render('!F:\=/!', output_dir='pdfs');"
)
@echo on
