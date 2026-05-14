@echo off
chcp 65001
title SIESTO 数智化实验室
echo 🚀 正在启动：SIESTO Lab 数字化资产空间...

:: 使用绝对路径启动，彻底解决“上周行这周不行”的路径幻觉
"C:\Users\liujing\AppData\Local\Programs\Python\Python313\python.exe" -m streamlit run app.py

pause