files=$(find -iname "*.rmd")

mkdir -p pdfs

echo "Начинается конвертация..."
for file in $files
do
    echo "require(rmarkdown); render('$file', output_dir='pdfs');" | R --vanilla
done
echo "Конвертация файлов в PDF завершена"
