"""
Gravatar plugin for Pelican
===========================

This plugin assigns the ``author_gravatar`` variable to the Gravatar URL and
makes the variable available within the article's context.
"""


from pelican import signals


def add_member(generator, metadata):

    print metadata.keys()

    if 'members' in metadata.keys():
        members = metadata['members'].splitlines()
        metadata['MEMBROS'] = dict()
        keys = members[0].split(',')
        for member in members[1:]:
            member_key = member.split(',')[0]
            print 'member_key', member_key
            member_dict = dict(zip(keys, member.split(',')))
            metadata['MEMBROS'][member_dict['nome']] = member_dict

        print metadata['MEMBROS']


def register():
    signals.page_generator_context.connect(add_member)
