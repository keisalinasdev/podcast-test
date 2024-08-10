import yaml
import xml.etree.ElementTree as xml_tree

# Load YAML data from file
with open('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)


rss_element = xml_tree.Element('rss', {'version': '2.0',
                                    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
                                    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'})

channel_element = xml_tree.SubElement(rss_element, 'channel')
link_prefix = yaml_data['link']


xml_tree.SubElement(channel_element, 'link').text = link_prefix