"""
Members info plugin for Pelican
===============================

This plugin replaces the ``members`` variable with a structure of it's contents
for use in the template

it takes a :members: metadata where the first line defines each key for the
final dict, and the following lines have each member info

:members: nome, email, twitter, github, site_nome, site_href
    Danilo Shiga, daniloshiga@gmail.com, @daneoshiga, daneoshiga, Danilo Shiga, http://daniloshiga.com
"""


from pelican import signals


def add_members(generator, metadata):

    if 'members' in metadata.keys():
        members = metadata['members'].encode('utf-8').splitlines()
        metadata['members'] = dict()
        keys = map(str.strip, members[0].split(','))
        for member in members[1:]:
            values = map(str.strip, member.split(','))
            member_dict = dict(zip(keys, values))
            metadata['members'][member_dict['nome']] = member_dict


def register():
    signals.page_generator_context.connect(add_members)
