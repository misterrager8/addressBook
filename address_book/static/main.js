$(document).ready(function() {
    document.documentElement.setAttribute('data-theme', localStorage.getItem('AddressBook'));
});

function changeTheme(theme) {
    localStorage.setItem('AddressBook', theme);
    document.documentElement.setAttribute('data-theme', localStorage.getItem('AddressBook'));
}

function toggleDiv(divId) {
    $('#' + divId).fadeToggle(150);
}