import setuptools

setuptools.setup(
    name="AddressBook",
    entry_points={"console_scripts": ["contacts=address_book.cli:cli"]},
)
