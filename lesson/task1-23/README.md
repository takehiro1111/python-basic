# カバレッジ率の集計

<details>
<summary>カバレッジ率</summary>

```zsh
[take@mactake:~/github/menta-python-lesson/lesson/task1-23]+[feature/task1-23](lesson-7I571lB-)
$pytest -v --cov=tests
================================================== test session starts ===================================================
platform darwin -- Python 3.12.2, pytest-8.3.5, pluggy-1.5.0 -- /Users/take/.local/share/virtualenvs/lesson-7I571lB-/bin/python
cachedir: .pytest_cache
rootdir: /Users/take/github/menta-python-lesson
configfile: pyproject.toml
plugins: anyio-4.9.0, mock-3.14.0, cov-6.1.1
collected 35 items

tests/test_account.py::TestAccountManager::test_account_info PASSED                                                [  2%]
tests/test_account.py::TestAccountManager::test_auth_user_id[takehiro1111-True] PASSED                             [  5%]
tests/test_account.py::TestAccountManager::test_auth_user_id[Michael-True] PASSED                                  [  8%]
tests/test_account.py::TestAccountManager::test_auth_user_id[test-dummy-user-False] PASSED                         [ 11%]
tests/test_account.py::TestAccountManager::test_auth_user_pin[takehiro1111-1234-True] PASSED                       [ 14%]
tests/test_account.py::TestAccountManager::test_auth_user_pin[Michael-5678-True] PASSED                            [ 17%]
tests/test_account.py::TestAccountManager::test_auth_user_pin[test-dummy-user-7890-False] PASSED                   [ 20%]
tests/test_account.py::TestBankAccount::test_initial_balance PASSED                                                [ 22%]
tests/test_account.py::TestBankAccount::test_set_balance PASSED                                                    [ 25%]
tests/test_atm.py::TestATM::test_guide_menu PASSED                                                                 [ 28%]
tests/test_atm.py::TestATM::test_deposit[1000-11000] PASSED                                                        [ 31%]
tests/test_atm.py::TestATM::test_deposit[test-str-None] PASSED                                                     [ 34%]
tests/test_atm.py::TestATM::test_deposit[0-None] PASSED                                                            [ 37%]
tests/test_atm.py::TestATM::test_deposit[-1-None] PASSED                                                           [ 40%]
tests/test_atm.py::TestATM::test_withdrawals[10000-0] PASSED                                                       [ 42%]
tests/test_atm.py::TestATM::test_withdrawals[200000-None] PASSED                                                   [ 45%]
tests/test_atm.py::TestATM::test_withdrawals[test-str-None] PASSED                                                 [ 48%]
tests/test_atm.py::TestATM::test_withdrawals[0-None] PASSED                                                        [ 51%]
tests/test_atm.py::TestATM::test_withdrawals[-1-None] PASSED                                                       [ 54%]
tests/test_atm.py::TestATM::test_show_error_msg PASSED                                                             [ 57%]
tests/test_atm.py::TestATM::test_execute_auth_user_id_true PASSED                                                  [ 60%]
tests/test_atm.py::TestATM::test_execute_auth_user_id_false PASSED                                                 [ 62%]
tests/test_atm.py::TestATM::test_execute_auth_user_pin_true PASSED                                                 [ 65%]
tests/test_atm.py::TestATM::test_execute_auth_user_pin_false PASSED                                                [ 68%]
tests/test_validate.py::TestBaseValidation::test_errors PASSED                                                     [ 71%]
tests/test_validate.py::TestBaseValidation::test_is_valid PASSED                                                   [ 74%]
tests/test_validate.py::TestDepositValidation::test_validate[10000-True] PASSED                                    [ 77%]
tests/test_validate.py::TestDepositValidation::test_validate[None-False] PASSED                                    [ 80%]
tests/test_validate.py::TestDepositValidation::test_validate[0-False] PASSED                                       [ 82%]
tests/test_validate.py::TestDepositValidation::test_validate[-1-False] PASSED                                      [ 85%]
tests/test_validate.py::TestWithdrawalsValidation::test_validate[1000-1000-None-True] PASSED                       [ 88%]
tests/test_validate.py::TestWithdrawalsValidation::test_validate[10000-None-\u91d1\u984d\u304c\u5165\u529b\u3055\u308c\u3066\u3044\u307e\u305b\u3093\u3002-False] PASSED [ 91%]
tests/test_validate.py::TestWithdrawalsValidation::test_validate[10000-0-1\u4ee5\u4e0a\u306e\u6570\u5b57\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002-False] PASSED [ 94%]
tests/test_validate.py::TestWithdrawalsValidation::test_validate[10000--1-1\u4ee5\u4e0a\u306e\u6570\u5b57\u3092\u5165\u529b\u3057\u3066\u304f\u3060\u3055\u3044\u3002-False] PASSED [ 97%]
tests/test_validate.py::TestWithdrawalsValidation::test_validate[10000-20000-\u6b8b\u9ad8\u4e0d\u8db3\u3067\u3059\u3002-False] PASSED [100%]

===================================================== tests coverage =====================================================
____________________________________ coverage: platform darwin, python 3.12.2-final-0 ____________________________________

Name                     Stmts   Miss  Cover
--------------------------------------------
tests/__init__.py            0      0   100%
tests/conftest.py           21      0   100%
tests/test_account.py       18      0   100%
tests/test_atm.py           37      0   100%
tests/test_validate.py      23      0   100%
--------------------------------------------
TOTAL                       99      0   100%
=================================================== 35 passed in 0.09s ============================================
```

</details>
