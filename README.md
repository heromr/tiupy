<div align="center">
  <h1 style="color: #0d47a1; font-size: 3em;">tiupy</h1>

  <p>
    <a href="https://github.com/heromr/tiupy/commits/main"><img src="https://img.shields.io/github/last-commit/heromr/tiupy?label=last%20updated&color=blueviolet" alt="GitHub last commit"></a>
    <a href="https://pypi.org/project/tiupy/"><img src="https://img.shields.io/pypi/dw/tiupy?color=blueviolet" alt="PyPI - Downloads"></a>
  </p>

  <p style="font-size: 1.2em; color: #424242;">A Python module for interacting with the TIU (Tishk International University) website, offering features like login, profile information retrieval, and course data access.</p>

  <h2 style="color: #0d47a1; font-size: 2em;">Installation</h2>

  <p style="font-size: 1.2em; color: #424242;">You can install tiupy using pip:</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">pip install tiupy</code></pre>

  <p style="font-size: 1.2em; color: #424242;">Alternatively, clone the repository and install it manually:</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">git clone https://github.com/heromr/tiupy.git
cd tiupy
python setup.py install</code></pre>
</div>

<div>
  <h2 align="center">Getting Started</h2>

  <p>
    To get started with the Tiu Python Module, follow these steps:
  </p>

  <h3 align="center">1. Import the module</h3>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">from tiupy import Tiu</code></pre>

  <h3 align="center">2. Create an instance of Tiu</h3>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">tiu = Tiu()</code></pre>

  <p>
    You can customize the initialization by providing optional parameters like proxies and request timeout.
  </p>
</div>

<div>
  <h2 align="center">Methods</h2>

  <p>
    The Tiu module provides the following methods for interaction:
  </p>

  <h3 style="color: #0d47a1;" align="center">`login(username: str, password: str)`</h3>
  <p>Login to the TIU website.</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">await tiu.login(username='your_username', password='your_password')</code></pre>

  <h3 style="color: #0d47a1;" align="center">`sid_login(SID: str)`</h3>
  <p>Login using a session ID (SID).</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">await tiu.sid_login(SID='your_session_id')</code></pre>

  <h3 style="color: #0d47a1;" align="center">`logout()`</h3>
  <p>Log out from the TIU website.</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">await tiu.logout()</code></pre>

  <h3 style="color: #0d47a1;" align="center">`get_courses_data()`</h3>
  <p>Fetch course data from the TIU website.</p>

  <pre style="background-color: #f5f5f5; padding: 10px;"><code style="color: #f44336;">courses_data = await tiu.get_courses_data()</code></pre>
</div>

<div align="center">
  <h2>License</h2>

  <p>
    This module is open-source and available under the MIT License. See the <a href="https://github.com/heromr/tiupy/blob/main/LICENSE">LICENSE</a> file for more details.
  </p>
</div>
</body>
</html>
