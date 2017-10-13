# ZeroAoVoiceScripts
Voice Scripts for PC/PSP games *Zero no Kiseki* & *Ao no Kiseki*    
They can be used for project [SoraVoce](https://github.com/ZhenjianYang/SoraVoice)(for PC versions)
and [ZeroAoVoice-PSP](https://github.com/ZhenjianYang/ZeroAoVoice-PSP)(for PSP versions)

These platforms/versions' scripts were done:

- **PC** : **Chinese Simplified**   
- **PSP** : **Japanese**, **Chinese Simplified(unofficial)**   

Get them at [Release](https://github.com/ZhenjianYang/ZeroAoVoiceScripts/releases/latest), or   
## Follow these steps

1.  **Clone**   
  `git clone --recursive https://github.com/ZhenjianYang/ZeroAoVoiceScripts`
  
2.  **Install python3 and 7zip**   
  We assume the path of 7zip is `C:\Program Files\7-Zip\7z.exe`  
  Some python libs need to be installed. Please refer to [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler).

3.  **Generate script files**   
  Just run the batch file `DoAll.bat`   
  New script files will be packed under folder `pack`

## About tools/cn_psp_sjis

This is a custom codepage for the unofficial chinese translated PSP games   
It is defined by **jis2ucs.bin** and **ucs2jis.bin**

## Dependence

- [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler), forked from [Ouroboros/EDDecompiler](https://github.com/Ouroboros/EDDecompiler)   

- [tools/PyLibs](https://github.com/ZhenjianYang/PyLibs), forked from [Ouroboros/PyLibs](https://github.com/Ouroboros/PyLibs)   

# ZeroAoVoiceScripts
PC/PSP游戏《零之轨迹》&《碧之轨迹》的语音脚本    
语音脚本可以用于项目[SoraVoce](https://github.com/ZhenjianYang/SoraVoice)(PC版)
以及[ZeroAoVoice-PSP](https://github.com/ZhenjianYang/ZeroAoVoice-PSP)(PSP版)

以下平台/版本的语音脚本已完成：

- **PC** : **简体中文版**   
- **PSP** : **日文版**, **简体中文版(非官方)**   

在[这里](https://github.com/ZhenjianYang/ZeroAoVoiceScripts/releases/latest)可以获取到上述语音脚本。或者，   

## 参照以下步骤   

1.  **获取**   
  `git clone --recursive https://github.com/ZhenjianYang/ZeroAoVoiceScripts`
  
2.  **安装python3以及7zip**   
  这里假定7zip路径为：`C:\Program Files\7-Zip\7z.exe`   
  还需要安装一些python库，具体请参考[tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler)。

3.  **生成脚本文件**   
  执行`DoAll.bat`即可    
  新的脚本文件会打包好并置于文件夹`pack`下

## 关于 tools/cn_psp_sjis

非官方汉化的PSP游戏使用的自定义文字编码，由**jis2ucs.bin**及**ucs2jis.bin**定义

## 依赖

- [tools/EDDecompiler](https://github.com/ZhenjianYang/EDDecompiler), Fork自[Ouroboros/EDDecompiler](https://github.com/Ouroboros/EDDecompiler)   

- [tools/PyLibs](https://github.com/ZhenjianYang/PyLibs), Fork自[Ouroboros/PyLibs](https://github.com/Ouroboros/PyLibs) 
