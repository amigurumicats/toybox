#!/bin/sh
# 指定したフォルダ以下の各言語のコードの行数の総和

wcl(){
  C_FILE=`find ${1}/* -type f -name *.${2} | wc -l`
  C_LINE=`find ${1}/* -type f -name *.${2} -print0 | xargs -0 cat | wc -l`

  echo "${C_LINE} line, ${C_FILE} file"
}

echo 'C: '`wcl ${1} c`
echo 'C++: '`wcl ${1} cpp`
echo 'Python: '`wcl ${1} py`
echo 'JavaScript: '`wcl ${1} js`
echo 'Java: '`wcl ${1} java`
echo 'Ruby: '`wcl ${1} rb`

