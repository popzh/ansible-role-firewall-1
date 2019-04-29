import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_firewall_config(host):
    firewall_config = host.file("/etc/firewall.bash")
    firewall_config.exists
    oct(firewall_config.mode) == '0744'
    firewall_config.user == 'root'
    firewall_config.group == 'root'
