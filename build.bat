
conda activate yolo8work && ^
echo building frontend ... && ^
cd .\src\frontend\ && ^
npm run build && ^
cd ..\..\ && ^
echo packaging app ... && ^
pyinstaller .\main.spec && ^
pause