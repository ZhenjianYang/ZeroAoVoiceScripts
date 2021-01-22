@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

set Zip7=C:\Program Files\7-Zip\7z.exe
set dt=%date:~2,2%%date:~5,2%%date:~8,2%

set outdir=%curp%\..\pack\%dt%

md "%outdir%"

"%Zip7%" -t7z -mx=9 a "%outdir%\%curd%_%dt%.7z" "%curp%\tmp\scena"
