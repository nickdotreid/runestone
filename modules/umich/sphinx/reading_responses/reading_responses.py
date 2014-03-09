# Copyright (C) 2014 Nick Reid
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = 'nickreid'

from docutils import nodes
from docutils.parsers.rst import directives
from docutils.parsers.rst import Directive
import json
import os


def setup(app):
    app.add_directive('reading_response',ReadingResponse)

    app.add_node(ReadingResponseNode, html=(visit_rr_node, depart_rr_node))

    app.connect('doctree-resolved',process_reading_response_nodes)
    app.connect('env-purge-doc', purge_reading_reasponses)


rr_html = """
<div id="%(id)s" class="reading_response" data-min="%(min_char)s" data-max="%(max_char)s">
    <p class="prompt"><label for="%(id)s_text">%(prompt)s</label></p>
    <p class="no-js alert-warning">Javascript is Disabled</p>
    <div class="js loading">
        <textarea id="%(id)s_text"></textarea>
    </div>
    <div class="js controls">
        <a class="btn btn-primary save" href="#">Save</a>
        <a class="btn feedback">Show Feedback</a>
    </div>
    <p class="ac_caption">Reading Response: %(id)s</p>
</div>
"""


class ReadingResponseNode(nodes.General, nodes.Element):
    def __init__(self,options):
        super(ReadingResponseNode,self).__init__()
        
        self.settings = options

        if 'id' not in self.settings:
            self.settings['id'] = "default"
        if 'prompt' not in self.settings:
            self.settings['prompt'] = ""
        if 'min_char' not in self.settings:
            self.settings['min_char'] = ""
        if 'max_char' not in self.settings:
            self.settings['max_char'] = ""

def visit_rr_node(self,node):
    res = rr_html % node.settings
    self.body.append(res)

def depart_rr_node(self,node):
    pass

def process_reading_response_nodes(app,env,docname):
    pass


def purge_reading_reasponses(app,env,docname):
    pass

class ReadingResponse(Directive):
    required_arguments = 1
    optional_arguments = 1
    option_spec = {
        'prompt':directives.unchanged,
    }

    def run(self):
        self.options['id'] = self.arguments[0]
        return [ReadingResponseNode(self.options)]