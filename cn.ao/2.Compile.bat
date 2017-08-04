@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

set input=%curp%\tmp\py.%curd%
set output=%curp%\tmp\scena

mkdir "%output%"
for %%i in ("%input%\*.py") do py "%%i" --cp=gbk "%output%"
