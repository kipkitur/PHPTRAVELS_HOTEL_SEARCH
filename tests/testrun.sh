# allure report
#cd tests
py.test --alluredir=%Reports% ./test_navigation_tria.py
py.test --alluredir=%Reports% ./test_search_tria.py
py.test --alluredir=%Reports% ./test_search_tria_children_increase.py
py.test --alluredir=%Reports% ./test_search_tria_adult_decrease.py
py.test --alluredir=%Reports% ./test_navigation_alzer.py
py.test --alluredir=%Reports% ./test_search_alzer.py
py.test --alluredir=%Reports% ./test_search_alzer_children_increase.py
py.test --alluredir=%Reports% ./test_search_alzer_adult_decrease.py

# behave
#behave -f allure_behave.formatter:AllureFormatter -o %Reports% ./feature

allure serve %Reports%
