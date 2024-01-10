import random

from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="head", footer="foot"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
# def test_modify_group_header(app):
#   if app.group.count() == 0:
#       app.group.create(Group(name="test", header="head", footer="foot"))
#  old_groups = app.group.get_group_list()
# index = randrange(len(old_groups))
# group = Group(name="test", header="you")
# group.id = old_groups[index].id
# app.group.modify_group_by_index(index, group)
# assert len(old_groups) == app.group.count()
# new_groups = app.group.get_group_list()
# old_groups[index] = group
# assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
