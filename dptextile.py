# -*- coding: utf-8 -*-

"""
    drupan-textile

    Plugin that provides textile conversion using the textile library
"""

from textile import textile


class Plugin(object):
    """convert entities content to textile"""
    def __init__(self, site, config):
        """
        Arguments:
            site: instance of drupan.site.Site
            config: instance of drupan.config.Config
        """
        self.site = site
        self.config = config

    def run(self):
        """run the plugin"""
        for entity in self.site.entities:
            if entity.raw:
                self.convert(entity)

    def convert(self, entity):
        """
        convert entity.raw to HTML and store it in entity.content

        Arguments:
            entity: instance of drupan.entity.Entity
        """
        entity.content = textile(entity.raw)
