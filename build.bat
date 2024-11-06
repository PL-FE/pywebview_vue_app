
conda activate py38 && ^
echo building frontend ... && ^
cd .\src\frontend\ && ^
npm run build && ^
cd ..\..\ && ^
echo packaging app ... && ^
pyinstaller .\main.spec && ^
pause
