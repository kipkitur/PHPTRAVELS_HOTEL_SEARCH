#!/usr/bin/env bash
# pytest test
#cd tests
py.test -v test_navigation_alzer
py.test -v test_search_tria.py
py.test -v test_search_tria_children_increase.py
py.test -v test_search_tria_adult_decrease.py
py.test -v test_navigation_alzer.py
py.test -v test_search_alzer.py
py.test -v test_search_alzer_children_increase.py
py.test -v test_search_alzer_adult_decrease.py
#pytest -n auto