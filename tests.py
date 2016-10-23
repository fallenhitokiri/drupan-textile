# -*- coding: utf-8 -*-
import unittest

from drupan.config import Config
from drupan.site import Site
from drupan.entity import Entity
from dptextile import Plugin


RAW = """*foo* _bar_"""
HTML = """\t<p><strong>foo</strong> <em>bar</em></p>"""


class PluginTests(unittest.TestCase):
    def setUp(self):
        self.config = Config()
        self.site = Site()

        self.entity = Entity(self.config)
        self.entity.raw = RAW
        self.site.entities.append(self.entity)

    def test_run(self):
        """should convert the entities raw text to HTML"""
        plugin = Plugin(self.site, self.config)
        plugin.run()

        self.assertEqual(self.entity.content, HTML)
