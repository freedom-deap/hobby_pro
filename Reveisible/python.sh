#pythonファイルの実行の簡略化

#整数型の変数の定義
function do_pfile() {
    declare -i i=0

    array=()

    for var in *.py
    do
	#配列の末尾に要素を追加
	array=("${array[@]}" "$var")
	i=$i+1
	echo $i:$var
    done

    read FILENUM
    clear
    python3 ${array[$FILENUM-1]}
    return 1
}

do_pfile
