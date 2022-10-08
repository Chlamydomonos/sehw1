#! /bin/bash

# TODO: add autopep8 here.

autopep8_all() {
    local root="$1"
    local fileName=""
    for file in `ls $1`
    do
        fileName=${root}"/"${file}
        if [ -d $fileName ]
        then
            autopep8_all $fileName
        elif [ "${fileName##*.}" == "py" ]
        then
            autopep8 --in-place $fileName
        fi
    done
}

autopep8_all .

# TODO: add autoflake here.

autoflake_all() {
    local root="$1"
    local fileName=""
    for file in `ls $1`
    do
        fileName=${root}"/"${file}
        if [ -d $fileName ]
        then
            autoflake_all $fileName
        elif [ "${fileName##*.}" == "py" ]
        then
            autoflake --in-place $fileName
        fi
    done
}

autoflake_all .

# TODO: add isort here.

isort .

# TODO: add flake8 here.

flake8 .