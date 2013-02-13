# command line tool #

I feel this must already exist but I could not google it so I built a prototype.

Use like this:

    cat data.tsv | cut -c4,9 | py "print('DELETE FROM sites WHERE id IN ({0})'.format(','.join(IN)))" | psql testdb admin

Where the `py` bit replaces the slightly longer command:

    python -c "import sys; print 'DELETE FROM sites WHERE id IN ({0})'.format(','.join(sys.stdin))"

I made this because I am tired of reading man pages for `awk` and `sed` and others; I already know python, but I am also tired of typing `import sys`, etc repeatedly.

If this has been implemented before and better, I hope someone will point that out.

`os`, `sys`, `csv` and `json` are pre-imported, as well as `unicode_literals` and `print_function` from the future.

Aditionally the following are imported and renamed:

    sys.stdin -> IN
    sys.stdout -> OUT
    functools -> FT
    itertools -> IT
    operator -> OP
    pprint.pprint -> PP
