import os
import time
from typing import NamedTuple, Optional, Dict, Tuple, List, Any

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


"""
#########################
# CUSTOM-MADE FUNCTIONS #
#########################
"""

# all_pages_list = ['https://python.iamroot.eu/genindex.html', 'https://python.iamroot.eu/py-modindex.html', 'https://python.iamroot.eu/index.html', 'https://python.iamroot.eu/whatsnew/3.9.html', 'https://python.iamroot.eu/whatsnew/3.8.html', 'https://python.iamroot.eu/whatsnew/3.7.html', 'https://python.iamroot.eu/whatsnew/3.6.html', 'https://python.iamroot.eu/whatsnew/3.5.html', 'https://python.iamroot.eu/whatsnew/3.4.html', 'https://python.iamroot.eu/whatsnew/3.3.html', 'https://python.iamroot.eu/whatsnew/3.2.html', 'https://python.iamroot.eu/whatsnew/3.1.html', 'https://python.iamroot.eu/whatsnew/3.0.html', 'https://python.iamroot.eu/whatsnew/2.7.html', 'https://python.iamroot.eu/whatsnew/2.6.html', 'https://python.iamroot.eu/whatsnew/2.5.html', 'https://python.iamroot.eu/whatsnew/2.4.html', 'https://python.iamroot.eu/whatsnew/2.3.html', 'https://python.iamroot.eu/whatsnew/2.2.html', 'https://python.iamroot.eu/whatsnew/2.1.html', 'https://python.iamroot.eu/whatsnew/2.0.html', 'https://python.iamroot.eu/whatsnew/changelog.html', 'https://python.iamroot.eu/tutorial/index.html', 'https://python.iamroot.eu/tutorial/appetite.html', 'https://python.iamroot.eu/tutorial/interpreter.html', 'https://python.iamroot.eu/tutorial/introduction.html', 'https://python.iamroot.eu/tutorial/controlflow.html', 'https://python.iamroot.eu/tutorial/datastructures.html', 'https://python.iamroot.eu/tutorial/modules.html', 'https://python.iamroot.eu/tutorial/inputoutput.html', 'https://python.iamroot.eu/tutorial/errors.html', 'https://python.iamroot.eu/tutorial/classes.html', 'https://python.iamroot.eu/tutorial/stdlib.html', 'https://python.iamroot.eu/tutorial/stdlib2.html', 'https://python.iamroot.eu/tutorial/venv.html', 'https://python.iamroot.eu/tutorial/whatnow.html', 'https://python.iamroot.eu/tutorial/interactive.html', 'https://python.iamroot.eu/tutorial/floatingpoint.html', 'https://python.iamroot.eu/tutorial/appendix.html', 'https://python.iamroot.eu/using/index.html', 'https://python.iamroot.eu/using/cmdline.html', 'https://python.iamroot.eu/using/unix.html', 'https://python.iamroot.eu/using/windows.html', 'https://python.iamroot.eu/using/mac.html', 'https://python.iamroot.eu/using/editors.html', 'https://python.iamroot.eu/reference/index.html', 'https://python.iamroot.eu/reference/introduction.html', 'https://python.iamroot.eu/reference/lexical_analysis.html', 'https://python.iamroot.eu/reference/datamodel.html', 'https://python.iamroot.eu/reference/executionmodel.html', 'https://python.iamroot.eu/reference/import.html', 'https://python.iamroot.eu/reference/expressions.html', 'https://python.iamroot.eu/reference/simple_stmts.html', 'https://python.iamroot.eu/reference/compound_stmts.html', 'https://python.iamroot.eu/reference/toplevel_components.html', 'https://python.iamroot.eu/reference/grammar.html', 'https://python.iamroot.eu/library/index.html', 'https://python.iamroot.eu/library/intro.html', 'https://python.iamroot.eu/library/functions.html', 'https://python.iamroot.eu/library/constants.html', 'https://python.iamroot.eu/library/stdtypes.html', 'https://python.iamroot.eu/library/exceptions.html', 'https://python.iamroot.eu/library/text.html', 'https://python.iamroot.eu/library/string.html', 'https://python.iamroot.eu/library/re.html', 'https://python.iamroot.eu/library/difflib.html', 'https://python.iamroot.eu/library/textwrap.html', 'https://python.iamroot.eu/library/unicodedata.html', 'https://python.iamroot.eu/library/stringprep.html', 'https://python.iamroot.eu/library/readline.html', 'https://python.iamroot.eu/library/rlcompleter.html', 'https://python.iamroot.eu/library/binary.html', 'https://python.iamroot.eu/library/struct.html', 'https://python.iamroot.eu/library/codecs.html', 'https://python.iamroot.eu/library/datatypes.html', 'https://python.iamroot.eu/library/datetime.html', 'https://python.iamroot.eu/library/zoneinfo.html', 'https://python.iamroot.eu/library/calendar.html', 'https://python.iamroot.eu/library/collections.html', 'https://python.iamroot.eu/library/collections.abc.html', 'https://python.iamroot.eu/library/heapq.html', 'https://python.iamroot.eu/library/bisect.html', 'https://python.iamroot.eu/library/array.html', 'https://python.iamroot.eu/library/weakref.html', 'https://python.iamroot.eu/library/types.html', 'https://python.iamroot.eu/library/copy.html', 'https://python.iamroot.eu/library/pprint.html', 'https://python.iamroot.eu/library/reprlib.html', 'https://python.iamroot.eu/library/enum.html', 'https://python.iamroot.eu/library/graphlib.html', 'https://python.iamroot.eu/library/numeric.html', 'https://python.iamroot.eu/library/numbers.html', 'https://python.iamroot.eu/library/math.html', 'https://python.iamroot.eu/library/cmath.html', 'https://python.iamroot.eu/library/decimal.html', 'https://python.iamroot.eu/library/fractions.html', 'https://python.iamroot.eu/library/random.html', 'https://python.iamroot.eu/library/statistics.html', 'https://python.iamroot.eu/library/functional.html', 'https://python.iamroot.eu/library/itertools.html', 'https://python.iamroot.eu/library/functools.html', 'https://python.iamroot.eu/library/operator.html', 'https://python.iamroot.eu/library/filesys.html', 'https://python.iamroot.eu/library/pathlib.html', 'https://python.iamroot.eu/library/os.path.html', 'https://python.iamroot.eu/library/fileinput.html', 'https://python.iamroot.eu/library/stat.html', 'https://python.iamroot.eu/library/filecmp.html', 'https://python.iamroot.eu/library/tempfile.html', 'https://python.iamroot.eu/library/glob.html', 'https://python.iamroot.eu/library/fnmatch.html', 'https://python.iamroot.eu/library/linecache.html', 'https://python.iamroot.eu/library/shutil.html', 
# 'https://python.iamroot.eu/library/persistence.html', 'https://python.iamroot.eu/library/pickle.html', 'https://python.iamroot.eu/library/copyreg.html', 'https://python.iamroot.eu/library/shelve.html', 'https://python.iamroot.eu/library/marshal.html', 'https://python.iamroot.eu/library/dbm.html', 'https://python.iamroot.eu/library/sqlite3.html', 'https://python.iamroot.eu/library/archiving.html', 'https://python.iamroot.eu/library/zlib.html', 'https://python.iamroot.eu/library/gzip.html', 'https://python.iamroot.eu/library/bz2.html', 'https://python.iamroot.eu/library/lzma.html', 'https://python.iamroot.eu/library/zipfile.html', 'https://python.iamroot.eu/library/tarfile.html', 'https://python.iamroot.eu/library/fileformats.html', 'https://python.iamroot.eu/library/csv.html', 'https://python.iamroot.eu/library/configparser.html', 'https://python.iamroot.eu/library/netrc.html', 'https://python.iamroot.eu/library/xdrlib.html', 'https://python.iamroot.eu/library/plistlib.html', 'https://python.iamroot.eu/library/crypto.html', 'https://python.iamroot.eu/library/hashlib.html', 'https://python.iamroot.eu/library/hmac.html', 'https://python.iamroot.eu/library/secrets.html', 'https://python.iamroot.eu/library/allos.html', 'https://python.iamroot.eu/library/os.html', 'https://python.iamroot.eu/library/io.html', 'https://python.iamroot.eu/library/time.html', 'https://python.iamroot.eu/library/argparse.html', 
# 'https://python.iamroot.eu/library/getopt.html', 'https://python.iamroot.eu/library/logging.html', 'https://python.iamroot.eu/library/logging.config.html', 'https://python.iamroot.eu/library/logging.handlers.html', 'https://python.iamroot.eu/library/getpass.html', 'https://python.iamroot.eu/library/curses.html', 'https://python.iamroot.eu/library/curses.ascii.html', 'https://python.iamroot.eu/library/curses.panel.html', 'https://python.iamroot.eu/library/platform.html', 'https://python.iamroot.eu/library/errno.html', 'https://python.iamroot.eu/library/ctypes.html', 'https://python.iamroot.eu/library/concurrency.html', 'https://python.iamroot.eu/library/threading.html', 'https://python.iamroot.eu/library/multiprocessing.html', 'https://python.iamroot.eu/library/multiprocessing.shared_memory.html', 'https://python.iamroot.eu/library/concurrent.html', 'https://python.iamroot.eu/library/concurrent.futures.html', 'https://python.iamroot.eu/library/subprocess.html', 'https://python.iamroot.eu/library/sched.html', 'https://python.iamroot.eu/library/queue.html', 'https://python.iamroot.eu/library/contextvars.html', 'https://python.iamroot.eu/library/_thread.html', 'https://python.iamroot.eu/library/ipc.html', 'https://python.iamroot.eu/library/asyncio.html', 'https://python.iamroot.eu/library/asyncio-task.html', 'https://python.iamroot.eu/library/asyncio-stream.html', 'https://python.iamroot.eu/library/asyncio-sync.html', 'https://python.iamroot.eu/library/asyncio-subprocess.html', 'https://python.iamroot.eu/library/asyncio-queue.html', 'https://python.iamroot.eu/library/asyncio-exceptions.html', 'https://python.iamroot.eu/library/asyncio-eventloop.html', 'https://python.iamroot.eu/library/asyncio-future.html', 'https://python.iamroot.eu/library/asyncio-protocol.html', 'https://python.iamroot.eu/library/asyncio-policy.html', 'https://python.iamroot.eu/library/asyncio-platforms.html', 'https://python.iamroot.eu/library/asyncio-api-index.html', 'https://python.iamroot.eu/library/asyncio-llapi-index.html', 'https://python.iamroot.eu/library/asyncio-dev.html', 'https://python.iamroot.eu/library/socket.html', 'https://python.iamroot.eu/library/ssl.html', 'https://python.iamroot.eu/library/select.html', 'https://python.iamroot.eu/library/selectors.html', 'https://python.iamroot.eu/library/asyncore.html', 'https://python.iamroot.eu/library/asynchat.html', 'https://python.iamroot.eu/library/signal.html', 'https://python.iamroot.eu/library/mmap.html', 'https://python.iamroot.eu/library/netdata.html', 'https://python.iamroot.eu/library/email.html', 'https://python.iamroot.eu/library/email.message.html', 'https://python.iamroot.eu/library/email.parser.html', 'https://python.iamroot.eu/library/email.generator.html', 'https://python.iamroot.eu/library/email.policy.html', 'https://python.iamroot.eu/library/email.errors.html', 'https://python.iamroot.eu/library/email.headerregistry.html', 'https://python.iamroot.eu/library/email.contentmanager.html', 'https://python.iamroot.eu/library/email.examples.html', 'https://python.iamroot.eu/library/email.compat32-message.html', 'https://python.iamroot.eu/library/email.mime.html', 'https://python.iamroot.eu/library/email.header.html', 'https://python.iamroot.eu/library/email.charset.html', 'https://python.iamroot.eu/library/email.encoders.html', 'https://python.iamroot.eu/library/email.utils.html', 'https://python.iamroot.eu/library/email.iterators.html', 'https://python.iamroot.eu/library/json.html', 'https://python.iamroot.eu/library/mailcap.html', 'https://python.iamroot.eu/library/mailbox.html', 'https://python.iamroot.eu/library/mimetypes.html', 'https://python.iamroot.eu/library/base64.html', 'https://python.iamroot.eu/library/binhex.html', 'https://python.iamroot.eu/library/binascii.html', 'https://python.iamroot.eu/library/quopri.html', 'https://python.iamroot.eu/library/uu.html', 'https://python.iamroot.eu/library/markup.html', 'https://python.iamroot.eu/library/html.html', 'https://python.iamroot.eu/library/html.parser.html', 'https://python.iamroot.eu/library/html.entities.html', 'https://python.iamroot.eu/library/xml.html', 'https://python.iamroot.eu/library/xml.etree.elementtree.html', 'https://python.iamroot.eu/library/xml.dom.html', 'https://python.iamroot.eu/library/xml.dom.minidom.html', 'https://python.iamroot.eu/library/xml.dom.pulldom.html', 'https://python.iamroot.eu/library/xml.sax.html', 'https://python.iamroot.eu/library/xml.sax.handler.html', 'https://python.iamroot.eu/library/xml.sax.utils.html', 'https://python.iamroot.eu/library/xml.sax.reader.html', 
# 'https://python.iamroot.eu/library/pyexpat.html', 'https://python.iamroot.eu/library/internet.html', 'https://python.iamroot.eu/library/webbrowser.html', 'https://python.iamroot.eu/library/cgi.html', 'https://python.iamroot.eu/library/cgitb.html', 'https://python.iamroot.eu/library/wsgiref.html', 'https://python.iamroot.eu/library/urllib.html', 'https://python.iamroot.eu/library/urllib.request.html', 'https://python.iamroot.eu/library/urllib.parse.html', 'https://python.iamroot.eu/library/urllib.error.html', 'https://python.iamroot.eu/library/urllib.robotparser.html', 'https://python.iamroot.eu/bugs.html', 'https://python.iamroot.eu/copyright.html', 'https://python.iamroot.eu/license.html', 'https://python.iamroot.eu/distutils/index.html', 'https://python.iamroot.eu/distutils/introduction.html', 'https://python.iamroot.eu/distutils/setupscript.html', 'https://python.iamroot.eu/distutils/configfile.html', 'https://python.iamroot.eu/distutils/sourcedist.html', 'https://python.iamroot.eu/distutils/builtdist.html', 'https://python.iamroot.eu/distutils/examples.html', 'https://python.iamroot.eu/distutils/extending.html', 'https://python.iamroot.eu/distutils/commandref.html', 'https://python.iamroot.eu/distutils/apiref.html', 'https://python.iamroot.eu/install/index.html', 'https://python.iamroot.eu/contents.html', 'https://python.iamroot.eu/whatsnew/index.html', 'https://python.iamroot.eu/library/http.html', 'https://python.iamroot.eu/library/http.client.html', 'https://python.iamroot.eu/library/ftplib.html', 'https://python.iamroot.eu/library/poplib.html', 'https://python.iamroot.eu/library/imaplib.html', 'https://python.iamroot.eu/library/nntplib.html', 'https://python.iamroot.eu/library/smtplib.html', 'https://python.iamroot.eu/library/smtpd.html', 'https://python.iamroot.eu/library/telnetlib.html', 'https://python.iamroot.eu/library/uuid.html', 'https://python.iamroot.eu/library/socketserver.html', 'https://python.iamroot.eu/library/http.server.html', 'https://python.iamroot.eu/library/http.cookies.html', 'https://python.iamroot.eu/library/http.cookiejar.html', 'https://python.iamroot.eu/library/xmlrpc.html', 'https://python.iamroot.eu/library/xmlrpc.client.html', 'https://python.iamroot.eu/library/xmlrpc.server.html', 'https://python.iamroot.eu/library/ipaddress.html', 'https://python.iamroot.eu/library/mm.html', 'https://python.iamroot.eu/library/audioop.html', 'https://python.iamroot.eu/library/aifc.html', 'https://python.iamroot.eu/library/sunau.html', 'https://python.iamroot.eu/library/wave.html', 'https://python.iamroot.eu/library/chunk.html', 'https://python.iamroot.eu/library/colorsys.html', 'https://python.iamroot.eu/library/imghdr.html', 'https://python.iamroot.eu/library/sndhdr.html', 'https://python.iamroot.eu/library/ossaudiodev.html', 'https://python.iamroot.eu/library/i18n.html', 'https://python.iamroot.eu/library/gettext.html', 'https://python.iamroot.eu/library/locale.html', 'https://python.iamroot.eu/library/frameworks.html', 'https://python.iamroot.eu/library/turtle.html', 'https://python.iamroot.eu/library/cmd.html', 'https://python.iamroot.eu/library/shlex.html', 'https://python.iamroot.eu/library/tk.html', 'https://python.iamroot.eu/library/tkinter.html', 'https://python.iamroot.eu/library/tkinter.colorchooser.html', 'https://python.iamroot.eu/library/tkinter.font.html', 'https://python.iamroot.eu/library/dialog.html', 'https://python.iamroot.eu/library/tkinter.messagebox.html', 'https://python.iamroot.eu/library/tkinter.scrolledtext.html', 'https://python.iamroot.eu/library/tkinter.dnd.html', 'https://python.iamroot.eu/library/tkinter.ttk.html', 
# 'https://python.iamroot.eu/library/tkinter.tix.html', 'https://python.iamroot.eu/library/idle.html', 'https://python.iamroot.eu/library/development.html', 'https://python.iamroot.eu/library/typing.html', 'https://python.iamroot.eu/library/pydoc.html', 'https://python.iamroot.eu/library/devmode.html', 'https://python.iamroot.eu/library/doctest.html', 'https://python.iamroot.eu/library/unittest.html', 'https://python.iamroot.eu/library/unittest.mock.html', 'https://python.iamroot.eu/library/unittest.mock-examples.html', 'https://python.iamroot.eu/library/2to3.html', 'https://python.iamroot.eu/library/test.html', 'https://python.iamroot.eu/library/debug.html', 'https://python.iamroot.eu/library/audit_events.html', 'https://python.iamroot.eu/library/bdb.html', 'https://python.iamroot.eu/library/faulthandler.html', 'https://python.iamroot.eu/library/pdb.html', 'https://python.iamroot.eu/library/profile.html', 'https://python.iamroot.eu/library/timeit.html', 'https://python.iamroot.eu/library/trace.html', 'https://python.iamroot.eu/library/tracemalloc.html', 'https://python.iamroot.eu/library/distribution.html', 'https://python.iamroot.eu/library/distutils.html', 'https://python.iamroot.eu/library/ensurepip.html', 'https://python.iamroot.eu/library/venv.html', 'https://python.iamroot.eu/library/zipapp.html', 'https://python.iamroot.eu/library/python.html', 'https://python.iamroot.eu/library/sys.html', 'https://python.iamroot.eu/library/sysconfig.html', 'https://python.iamroot.eu/library/builtins.html', 'https://python.iamroot.eu/library/__main__.html', 'https://python.iamroot.eu/library/warnings.html', 'https://python.iamroot.eu/library/dataclasses.html', 'https://python.iamroot.eu/library/contextlib.html', 'https://python.iamroot.eu/library/abc.html', 'https://python.iamroot.eu/library/atexit.html', 'https://python.iamroot.eu/library/traceback.html', 'https://python.iamroot.eu/library/__future__.html', 'https://python.iamroot.eu/library/gc.html', 'https://python.iamroot.eu/library/inspect.html', 'https://python.iamroot.eu/library/site.html', 'https://python.iamroot.eu/library/custominterp.html', 'https://python.iamroot.eu/library/code.html', 'https://python.iamroot.eu/library/codeop.html', 'https://python.iamroot.eu/library/modules.html', 'https://python.iamroot.eu/library/zipimport.html', 'https://python.iamroot.eu/library/pkgutil.html', 'https://python.iamroot.eu/library/modulefinder.html', 'https://python.iamroot.eu/library/runpy.html', 'https://python.iamroot.eu/library/importlib.html', 'https://python.iamroot.eu/library/importlib.metadata.html', 'https://python.iamroot.eu/library/language.html', 'https://python.iamroot.eu/library/parser.html', 'https://python.iamroot.eu/library/ast.html', 'https://python.iamroot.eu/library/symtable.html', 'https://python.iamroot.eu/library/symbol.html', 'https://python.iamroot.eu/library/token.html', 'https://python.iamroot.eu/library/keyword.html', 'https://python.iamroot.eu/library/tokenize.html', 'https://python.iamroot.eu/library/tabnanny.html', 'https://python.iamroot.eu/library/pyclbr.html', 'https://python.iamroot.eu/library/py_compile.html', 'https://python.iamroot.eu/library/compileall.html', 'https://python.iamroot.eu/library/dis.html', 'https://python.iamroot.eu/library/pickletools.html', 'https://python.iamroot.eu/library/misc.html', 'https://python.iamroot.eu/library/formatter.html', 'https://python.iamroot.eu/library/windows.html', 'https://python.iamroot.eu/library/msilib.html', 'https://python.iamroot.eu/library/msvcrt.html', 'https://python.iamroot.eu/library/winreg.html', 'https://python.iamroot.eu/library/winsound.html', 'https://python.iamroot.eu/library/unix.html', 'https://python.iamroot.eu/library/posix.html', 'https://python.iamroot.eu/library/pwd.html', 'https://python.iamroot.eu/library/spwd.html', 'https://python.iamroot.eu/library/grp.html', 'https://python.iamroot.eu/library/crypt.html', 'https://python.iamroot.eu/library/termios.html', 'https://python.iamroot.eu/library/tty.html', 'https://python.iamroot.eu/library/pty.html', 'https://python.iamroot.eu/library/fcntl.html', 'https://python.iamroot.eu/library/pipes.html', 'https://python.iamroot.eu/library/resource.html', 'https://python.iamroot.eu/library/nis.html', 'https://python.iamroot.eu/library/syslog.html', 'https://python.iamroot.eu/library/superseded.html', 'https://python.iamroot.eu/library/optparse.html', 'https://python.iamroot.eu/library/imp.html', 'https://python.iamroot.eu/library/undoc.html', 'https://python.iamroot.eu/library/security_warnings.html', 'https://python.iamroot.eu/extending/index.html', 'https://python.iamroot.eu/extending/extending.html', 'https://python.iamroot.eu/extending/newtypes_tutorial.html', 'https://python.iamroot.eu/extending/newtypes.html', 'https://python.iamroot.eu/extending/building.html', 'https://python.iamroot.eu/extending/windows.html', 'https://python.iamroot.eu/extending/embedding.html', 'https://python.iamroot.eu/c-api/index.html', 'https://python.iamroot.eu/c-api/intro.html', 'https://python.iamroot.eu/c-api/stable.html', 'https://python.iamroot.eu/c-api/veryhigh.html', 'https://python.iamroot.eu/c-api/refcounting.html', 'https://python.iamroot.eu/c-api/exceptions.html', 'https://python.iamroot.eu/c-api/utilities.html', 'https://python.iamroot.eu/c-api/sys.html', 'https://python.iamroot.eu/c-api/import.html', 'https://python.iamroot.eu/c-api/marshal.html', 'https://python.iamroot.eu/c-api/arg.html', 'https://python.iamroot.eu/c-api/conversion.html', 'https://python.iamroot.eu/c-api/reflection.html', 'https://python.iamroot.eu/c-api/codec.html', 'https://python.iamroot.eu/c-api/abstract.html', 'https://python.iamroot.eu/c-api/object.html', 'https://python.iamroot.eu/c-api/call.html', 'https://python.iamroot.eu/c-api/number.html', 'https://python.iamroot.eu/c-api/sequence.html', 'https://python.iamroot.eu/c-api/mapping.html', 'https://python.iamroot.eu/c-api/iter.html', 'https://python.iamroot.eu/c-api/buffer.html', 'https://python.iamroot.eu/c-api/objbuffer.html', 'https://python.iamroot.eu/c-api/concrete.html', 'https://python.iamroot.eu/c-api/type.html', 'https://python.iamroot.eu/c-api/none.html', 'https://python.iamroot.eu/c-api/long.html', 'https://python.iamroot.eu/c-api/bool.html', 'https://python.iamroot.eu/c-api/float.html', 'https://python.iamroot.eu/c-api/complex.html', 'https://python.iamroot.eu/c-api/bytes.html', 'https://python.iamroot.eu/c-api/bytearray.html', 'https://python.iamroot.eu/c-api/unicode.html', 'https://python.iamroot.eu/c-api/tuple.html', 'https://python.iamroot.eu/c-api/list.html', 'https://python.iamroot.eu/c-api/dict.html', 'https://python.iamroot.eu/c-api/set.html', 'https://python.iamroot.eu/c-api/function.html', 'https://python.iamroot.eu/c-api/method.html', 'https://python.iamroot.eu/c-api/cell.html', 'https://python.iamroot.eu/c-api/code.html', 'https://python.iamroot.eu/c-api/file.html', 'https://python.iamroot.eu/c-api/module.html', 'https://python.iamroot.eu/c-api/iterator.html', 'https://python.iamroot.eu/c-api/descriptor.html', 'https://python.iamroot.eu/c-api/slice.html', 'https://python.iamroot.eu/c-api/memoryview.html', 'https://python.iamroot.eu/c-api/weakref.html', 'https://python.iamroot.eu/c-api/capsule.html', 'https://python.iamroot.eu/c-api/gen.html', 'https://python.iamroot.eu/c-api/coro.html', 'https://python.iamroot.eu/c-api/contextvars.html', 'https://python.iamroot.eu/c-api/datetime.html', 'https://python.iamroot.eu/c-api/typehints.html', 'https://python.iamroot.eu/c-api/init.html', 'https://python.iamroot.eu/c-api/init_config.html', 'https://python.iamroot.eu/c-api/memory.html', 'https://python.iamroot.eu/c-api/objimpl.html', 'https://python.iamroot.eu/c-api/allocation.html', 
# 'https://python.iamroot.eu/c-api/structures.html', 'https://python.iamroot.eu/c-api/typeobj.html', 'https://python.iamroot.eu/c-api/gcsupport.html', 'https://python.iamroot.eu/c-api/apiabiversion.html', 'https://python.iamroot.eu/distributing/index.html', 'https://python.iamroot.eu/installing/index.html', 'https://python.iamroot.eu/howto/index.html', 'https://python.iamroot.eu/howto/pyporting.html', 'https://python.iamroot.eu/howto/cporting.html', 'https://python.iamroot.eu/howto/curses.html', 'https://python.iamroot.eu/howto/descriptor.html', 'https://python.iamroot.eu/howto/functional.html', 'https://python.iamroot.eu/howto/logging.html', 'https://python.iamroot.eu/howto/logging-cookbook.html', 'https://python.iamroot.eu/howto/regex.html', 'https://python.iamroot.eu/howto/sockets.html', 'https://python.iamroot.eu/howto/sorting.html', 'https://python.iamroot.eu/howto/unicode.html', 'https://python.iamroot.eu/howto/urllib2.html', 'https://python.iamroot.eu/howto/argparse.html', 'https://python.iamroot.eu/howto/ipaddress.html', 'https://python.iamroot.eu/howto/clinic.html', 'https://python.iamroot.eu/howto/instrumentation.html', 'https://python.iamroot.eu/faq/index.html', 'https://python.iamroot.eu/faq/general.html', 'https://python.iamroot.eu/faq/programming.html', 'https://python.iamroot.eu/faq/design.html', 'https://python.iamroot.eu/faq/library.html', 'https://python.iamroot.eu/faq/extending.html', 'https://python.iamroot.eu/faq/windows.html', 'https://python.iamroot.eu/faq/gui.html', 'https://python.iamroot.eu/faq/installed.html', 'https://python.iamroot.eu/glossary.html', 'https://python.iamroot.eu/about.html', 'https://python.iamroot.eu/search.html', 'https://python.iamroot.eu/download.html', 'https://python.iamroot.eu/genindex-Symbols.html', 'https://python.iamroot.eu/genindex-_.html', 'https://python.iamroot.eu/genindex-A.html', 'https://python.iamroot.eu/genindex-B.html', 'https://python.iamroot.eu/genindex-C.html', 'https://python.iamroot.eu/genindex-D.html', 'https://python.iamroot.eu/genindex-E.html', 'https://python.iamroot.eu/genindex-F.html', 'https://python.iamroot.eu/genindex-G.html', 'https://python.iamroot.eu/genindex-H.html', 'https://python.iamroot.eu/genindex-I.html', 'https://python.iamroot.eu/genindex-J.html', 'https://python.iamroot.eu/genindex-K.html', 'https://python.iamroot.eu/genindex-L.html', 'https://python.iamroot.eu/genindex-M.html', 'https://python.iamroot.eu/genindex-N.html', 'https://python.iamroot.eu/genindex-O.html', 'https://python.iamroot.eu/genindex-P.html', 'https://python.iamroot.eu/genindex-Q.html', 'https://python.iamroot.eu/genindex-R.html', 'https://python.iamroot.eu/genindex-S.html', 'https://python.iamroot.eu/genindex-T.html', 'https://python.iamroot.eu/genindex-U.html', 'https://python.iamroot.eu/genindex-V.html', 'https://python.iamroot.eu/genindex-W.html', 'https://python.iamroot.eu/genindex-X.html', 'https://python.iamroot.eu/genindex-Y.html', 'https://python.iamroot.eu/genindex-Z.html', 'https://python.iamroot.eu/genindex-all.html']

all_pages_list = []
def get_all_pages(base_url: str) -> None:
    """
    Loops from all pages and saves link of each to all_pages_list.
    """
    soup = get_soup(base_url)
    a_tags = soup.find_all("a")
    
    for a in a_tags:
        url = a.get("href")

        if is_url_valid(url):
            full_url = urljoin(base_url, url)
            if not full_url in all_pages_list:
                all_pages_list.append(full_url)
                get_all_pages(full_url)    


def is_url_valid(url: str) -> bool:
    """
    Checks if url is on same domain as base_url.
    """
    if not url.startswith("http"):
        if url.endswith(".html"):
            if url.find("#") == -1:
                return True
    return False


def get_soup(base_url: str) -> BeautifulSoup:
    """
    Chcecks if page was already downloaded and creates a BeautifulSoup 
    object.
    """
    if not base_url == "https://python.iamroot.eu/":
        file_path = base_url[26:]

        if os.path.exists(f"saved_pages/{file_path}"):
            with open(f"saved_pages/{file_path}", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            time.sleep(0.5)
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage(file_path, page)
            return BeautifulSoup(page, "html.parser")
    else:
        if os.path.exists(f"saved_pages/index.html"):
            with open(f"saved_pages/index.html", "r", encoding="utf-8") as html_file:
                return BeautifulSoup(html_file.read(), "html.parser")

        else:
            time.sleep(0.5)
            responce = download_webpage(base_url)
            page  = responce.text
            save_webpage("index.html", page)
            return BeautifulSoup(page, "html.parser")


def save_webpage(file_path: str, page_content: str) -> None:
    """
    Saves page on local disk.
    """
    try:
        with open(f"saved_pages/{file_path}", "w", encoding="utf-8") as html_file:
            html_file.write(page_content)

    except FileNotFoundError:
        splited_path = file_path.split("/")
        os.mkdir(f"saved_pages/{splited_path[0]}")

        with open(f"saved_pages/{splited_path[0]}/{splited_path[1]}", "w",
                  encoding="utf-8") as html_file:

            html_file.write(page_content)


"""
######################
# TEMPLATE FUNCTIONS #
######################
"""

class FullScrap(NamedTuple):
    # TUTO TRIDU ROZHODNE NEMEN
    linux_only_availability: List[str]
    most_visited_webpage: Tuple[int, str]
    changes: List[Tuple[int, str]]
    params: List[Tuple[int, str]]
    tea_party: Optional[str]

    def as_dict(self) -> Dict[str, Any]:
        return {
            'linux_only_availability': self.linux_only_availability,
            'most_visited_webpage': self.most_visited_webpage,
            'changes': self.changes,
            'params': self.params,
            'tea_party': self.tea_party
        }


def download_webpage(url: str, *args, **kwargs) -> requests.Response:
    """
    Download the page and returns its response by using requests.get
    :param url: url to download
    :return: requests Response
    """
    # TUTO FUNKCI ROZHODNE NEMEN
    print('GET ', url)
    return requests.get(url, *args, **kwargs)


def get_linux_only_availability() -> List[str]:
    """
    Finds all functions that area available only on Linux systems
    :return: all function names that area available only on Linux systems
    """
    print("Getting linux avaible functions...")
    unix_avaible_functions = []
    required_words = ["Unix", "Linux"]
    prohibited_words = ["Windows", "BSD", "AIX"]
    for page in all_pages_list:
        soup = get_soup(page)

        func = soup.find_all("dl", class_ = "function")
        for dl in func:
            try:
                p = dl.find("p", class_ = "availability")
                required_word = [
                    x for x in required_words if p.text.find(x) > -1]
                prohibited_word = [
                    x for x in prohibited_words if p.text.find(x) > -1]
                if required_word and not prohibited_word:
                    dt = dl.find("dt")
                    unix_avaible_functions.append(dt.get("id"))

            except AttributeError:
                pass

        method = soup.find_all("dl", class_ = "method")
        for dl in method:
            try:
                p = dl.find("p", class_ = "availability")
                required_word = [
                    x for x in required_words if p.text.find(x) > -1]
                prohibited_word = [
                    x for x in prohibited_words if p.text.find(x) > -1]
                if required_word and not prohibited_word:
                    dt = dl.find("dt")
                    unix_avaible_functions.append(dt.get("id"))

            except AttributeError:
                pass

    return unix_avaible_functions


def get_most_visited_webpage() -> Tuple[int, str]:
    """
    Finds the page with most links to it
    :return: number of anchors to this page and its URL
    """
    print("Getting most visited page...")
    link_visits = {}
    for page in all_pages_list:
        soup = get_soup(page)
        a_tags = soup.find_all("a")

        for a in a_tags:
            url = a.get("href")
            if is_url_valid(url):
                full_url = urljoin(page, url)
                try:
                    link_visits[full_url] += 1
                except KeyError:
                    link_visits[full_url] = 1

    most_visited_page = max(link_visits)
    return (link_visits[most_visited_page], most_visited_page)


def get_changes() -> List[Tuple[int, str]]:
    """
    Locates all counts of changes of functions and groups them by version
    :return: all counts of changes of functions and groups them by version,
    sorted from the most changes DESC
    """
    print("Getting changes...")
    changes = {}

    for page in all_pages_list:
        soup = get_soup(page)

        ver_added = soup.find_all("span", class_ = "versionmodified added")
        ver_changed = soup.find_all("span", class_ = "versionmodified changed")

        for span in ver_added:
            cut = span.text.find("3.")

            if cut != -1:
                try:
                    changes[span.text[cut:cut + 3]] += 1
                except KeyError:
                    changes[span.text[cut:cut + 3]] = 1
        
        for span in ver_changed:
            cut = span.text.find("3.")

            if cut != -1:
                try:
                    changes[span.text[cut:cut + 3]] += 1
                except KeyError:
                    changes[span.text[cut:cut + 3]] = 1

    result = sorted(changes.items(), key=lambda x: x[1], reverse=True)
    swaped_result = []

    for i in result:
        swaped_result.append((i[1], i[0]))

    return swaped_result


def get_most_params() -> List[Tuple[int, str]]:
    """
    Finds the function that accepts more than 10 parameters
    :return: number of parameters of this function and its name, 
    sorted by the count DESC
    """
    print("Getting most parameters...")
    most_parm_functions = {}

    for page in all_pages_list:
        soup = get_soup(page)

        func = soup.find_all("dl", class_ = "function")
        for dl in func:
            func_names = dl.find_all("dt")
            for dt in func_names:
                parameters = dt.find_all("em", class_ = "sig-param")
                parm_count = 0

                for _ in parameters:
                    parm_count += 1

                if parm_count >= 10:
                    most_parm_functions[dt.get("id")] = parm_count
        
        methods = soup.find_all("dl", class_ = "method")
        for dl in methods:
            method_names = dl.find_all("dt")
            for dt in method_names:
                parameters = dt.find_all("em", class_ = "sig-param")
                parm_count = 0

                for _ in parameters:
                    parm_count += 1

                if parm_count >= 10:
                    most_parm_functions[dt.get("id")] = parm_count

    result = sorted(most_parm_functions.items(), key=lambda x: x[1], reverse=True)
    swaped_result = []

    for i in result:
        swaped_result.append((i[1], i[0]))

    return swaped_result


def find_secret_tea_party(base_url: str) -> Optional[str]:
    """
    Locates a secret Tea party
    :param base_url: base url of the website
    :return: url at which the secret tea party can be found
    """
    # Tuto funkci implementuj
    pass


def scrap_all(base_url: str) -> FullScrap:
    """
    Scrap all the information as efficiently as we can
    :param base_url: base url of the website
    :return: full web scrap of the Python docs
    """
    # Tuto funkci muzes menit, ale musi vracet vzdy tyto data
    scrap = FullScrap(
        linux_only_availability=get_linux_only_availability(),
        most_visited_webpage=get_most_visited_webpage(),
        changes=get_changes(),
        params=get_most_params(),
        tea_party=find_secret_tea_party(base_url)
    )
    return scrap


def main() -> None:
    """
    Do a full scrap and print the results
    :return:
    """
    # Tuto funkci klidne muzes zmenit podle svych preferenci :)
    time_start = time.time()
    
    import json

    if not os.path.isdir("saved_pages"):
        os.mkdir("saved_pages")

    print("Getting all pages...")
    get_all_pages('https://python.iamroot.eu/')
    print(len(all_pages_list), "in list")
    
    print(json.dumps(scrap_all('https://python.iamroot.eu/').as_dict()))
    print('took', int(time.time() - time_start), 's')


if __name__ == '__main__':
    main()
