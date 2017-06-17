@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a


del /S /F /Q "%curp%\import_py_report.txt"
rd /S /Q "%curp%\tmp"

