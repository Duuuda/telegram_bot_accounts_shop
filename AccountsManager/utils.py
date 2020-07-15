from os import listdir, walk
from shutil import rmtree
from zipfile import ZipFile, ZIP_DEFLATED
from JsonGetter import JSON


config_getter = JSON()
*_, accounts_path, on_sending_path = config_getter()


class TooManyAccounts(Exception):
    pass


class TooFewAccounts(Exception):
    pass


def _archive_and_delete(func):
    def wrapper(*args, **kwargs) -> str:
        accounts = func(*args, **kwargs)
        new_archive_name = ''.join(accounts) + '.zip'
        with ZipFile(on_sending_path + new_archive_name, 'w', ZIP_DEFLATED) as archive:
            for account in accounts:
                for root, dirs, files in walk(accounts_path + account):
                    for inside_file in files:
                        if inside_file != '':
                            archive.write(root + '/' + inside_file)
        for account in accounts:
            rmtree(accounts_path + account)
        return on_sending_path + new_archive_name
    return wrapper


@_archive_and_delete
def get_accounts(count: int = 1) -> list:
    all_accounts = listdir(accounts_path)
    if len(all_accounts) < count:
        raise TooManyAccounts(f'all accounts {len(all_accounts)}, and the requested {count}')
    elif count < 1:
        raise TooFewAccounts(f"you can't request {count} accounts")
    return all_accounts[0:count]


def get_count_accounts():
    return len(listdir(accounts_path))
