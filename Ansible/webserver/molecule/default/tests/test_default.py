"""Role testing files using testinfra."""


def test_hosts_file(host):
    """Validate /etc/hosts file."""
    f = host.file("/etc/hosts")

    assert f.exists
    assert f.user == "root"
    assert f.group == "root"

def test_httpd_runing(host):
  httpd = host.service("httpd")
  assert httpd.is_running

def test_index_contents(host):
  index = host.file("/var/www/html/index.html")
  assert index.exists