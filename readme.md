# command line tool #

Use like this:

    cat data.tsv | cut -c4,9 | py "print('DELETE FROM sites WHERE id IN ({0})'.format(','.join(IN)))" | psql testdb admin

Where the `py` bit replaces the slightly longer command:

    python -c "import sys; print 'DELETE FROM sites WHERE id IN ({0})'.format(','.join(sys.stdin))"

I made this because I am tired of reading man pages for `awk` and `sed` and others; I already know python, but I am also tired of typing `import sys`, etc repeatedly.

`os`, `sys`, `csv` and `json` are pre-imported, as well as `unicode_literals` and `print_function` from the future.

Aditionally the following are imported and renamed:

    sys.stdin -> IN
    sys.stdout -> OUT
    functools -> FT
    itertools -> IT
    operator -> OP
    pprint.pprint -> PP

-----

Install like this:

    pip install shell-pype

-----

For those interested in more robust solutions checkout <a href='https://github.com/alecthomas/pawk'>pawk</a> or <a href='http://code.google.com/p/pyp/'>pyp</a>.
