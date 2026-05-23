

Everything is documented

    [copy_files] Filed copied: check_documentation.py
    [exec_bash_compare] Command to run:
    ./check_documentation.py 101-safely_get_value
    su student_jail -c 'timeout 30 bash -c '"'"'./check_documentation.py 101-safely_get_value'"'"''
    [exec_bash_compare] Return code: 1
    [exec_bash_compare] Student stdout:
    Module not documented or not enough: None -
    [exec_bash_compare] Student stdout length: 167
    [exec_bash_compare] Student stderr:
    [exec_bash_compare] Student stderr length: 0
    [exec_bash_compare] Desired stdout:
    OK
    [exec_bash_compare] Desired stdout length: 2
