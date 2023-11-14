import re


def test_contact_unit_name_on_home_page(app):
    contact_form_home_page = app.contact.get_contact_list()[0]
    contact_form_edit_page = app.contact.get_contact_info_edit_page(0)
    assert contact_form_home_page.firstname == contact_form_edit_page.firstname
    assert contact_form_home_page.lastname == contact_form_edit_page.lastname


def test_contact_address_on_home_page(app):
    contact_form_home_page = app.contact.get_contact_list()[0]
    contact_form_edit_page = app.contact.get_contact_info_edit_page(0)
    assert contact_form_home_page.address == contact_form_edit_page.address


def test_contact_email_on_home_page(app):
    contact_form_home_page = app.contact.get_contact_list()[0]
    contact_form_edit_page = app.contact.get_contact_info_edit_page(0)
    assert contact_form_home_page.all_emails_from_homepage == merge_emails_like_on_home_page(contact_form_edit_page)


def test_phones_on_home_page(app):
    contact_form_home_page = app.contact.get_contact_list()[0]
    contact_form_edit_page = app.contact.get_contact_info_edit_page(0)
    assert contact_form_home_page.all_phones_from_homepage == merge_phones_like_on_home_page(contact_form_edit_page)


def test_phones_on_contact_view_page(app):
    contact_form_view_page = app.contact.contact_form_view_page(0)
    contact_form_edit_page = app.contact.get_contact_info_edit_page(0)
    assert contact_form_view_page.home_phone == contact_form_edit_page.home_phone
    assert contact_form_view_page.self_mobile == contact_form_edit_page.self_mobile
    assert contact_form_view_page.work_mobile == contact_form_edit_page.work_mobile


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.self_mobile, contact.work_mobile]))))
