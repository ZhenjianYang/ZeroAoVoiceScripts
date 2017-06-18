@echo off

set curp=%~dp0
set toolsp=%curp%\..\tools
set PYTHONPATH=%toolsp%\EDDecompiler\Decompiler;%toolsp%\PyLibs

set p=%~p0
set p=%p:\= %
for %%a in (%p%) do set curd=%%a

set report=%curp%\tmp\import_py_report.txt
set dir_py_new=%curp%\tmp\py.%curd%

set dir_py=%curp%\py.ori.fmt
set dir_py_out=%curp%\out.ori
set dir_bin_out=%curp%\out.evo

"%toolsp%\ZA_Importer_PY.exe" "%dir_py_new%" "%dir_py%" "%dir_py_out%" "%dir_bin_out%" "%report%"
