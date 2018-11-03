;; Directory Local Variables

;; Activate 'amanita' virtual enviroment from emacs.
((nil . ((pyvenv-workon . "amanita"))))

;; Must run on shell: cp /usr/bin/pdb3 ~/.virtualenvs/amanita/bin/pdb
;; And change #! /usr/bin/python3 for #! /home/constrict0r/.virtualenvs/amanita/bin/python.

;; First time on emacs must call a shell an install the package to work:
;; M-x RET shell RET python setup.py install RET.

;; Tox default enviroment.
((nil . ((tox-default-env . "py35"))))