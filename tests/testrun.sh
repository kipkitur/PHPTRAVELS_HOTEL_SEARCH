# allure report
#cd tests
<<<<<<< HEAD
py.test --alluredir=%Reports% ./test_navigation_tria.py
py.test --alluredir=%Reports% ./test_search_tria.py
py.test --alluredir=%Reports% ./test_search_tria_children_increase.py
py.test --alluredir=%Reports% ./test_search_tria_adult_decrease.py
py.test --alluredir=%Reports% ./test_navigation_alzer.py
py.test --alluredir=%Reports% ./test_search_alzer.py
py.test --alluredir=%Reports% ./test_search_alzer_children_increase.py
=======

# Alzer Hotel Istanbul, Istanbul
# home page
py.test --alluredir=%Reports% ./test_navigation_tria.py
# 2 adults 0 children
py.test --alluredir=%Reports% ./test_search_tria.py
# 2 adults 2 children
py.test --alluredir=%Reports% ./test_search_tria_children_increase.py
# 0 adults 0 children
py.test --alluredir=%Reports% ./test_search_tria_adult_decrease.py

# Tria Hotel Istanbul Especial, Istanbul
# home page
py.test --alluredir=%Reports% ./test_navigation_alzer.py
# 2 adults 0 children
py.test --alluredir=%Reports% ./test_search_alzer.py
# 2 adults 2 children
py.test --alluredir=%Reports% ./test_search_alzer_children_increase.py
# 0 adults 0 children
>>>>>>> 601062a313790068a2e4e9f74a256325e65ec794
py.test --alluredir=%Reports% ./test_search_alzer_adult_decrease.py

# behave
#behave -f allure_behave.formatter:AllureFormatter -o %Reports% ./feature

allure serve %Reports%
