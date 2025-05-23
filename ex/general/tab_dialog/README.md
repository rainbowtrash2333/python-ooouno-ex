# TAB CONTROL DIALOG BOX

LibreOffice do not a Tab Control in the macro editor.
However LibreOffice does have a [Tab Container](<https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1tab_1_1UnoControlTabPageContainerModel.html>) built in.

This example demonstrates how to use Tabs in a Dialog Box.

**Update**: [OOO Development Tools](https://python-ooo-dev-tools.readthedocs.io/en/latest/index.html) has a much better implementation of Tab Control.
See the [tree](../../dialog/tree/) and [list box](../../dialog/tabs_list_box/) examples.

Example is created in [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) style.

Example also demonstrates usage of [Radio Button](https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlRadioButton.html) Controls and [List Box](https://api.libreoffice.org/docs/idl/ref/servicecom_1_1sun_1_1star_1_1awt_1_1UnoControlListBox.html) controls.

![Dialog](https://user-images.githubusercontent.com/4193389/166167632-5492c83d-f4df-4199-b164-f0785a9a829b.png)

## Sample Document

see sample LibreOffice Writer document, [tab_dialog.odt](tab_dialog.odt)

### Sample Code

see [script.py](script.py) for sample usage.

## Usage

```python
from src.examples.tab_dialog.mvc.controller import MultiSyntaxController
from src.examples.tab_dialog.mvc.model import MultiSyntaxModel
from src.examples.tab_dialog.mvc.view import MultiSyntaxView


dlg = MultiSyntaxController(model=MultiSyntaxModel(), view=MultiSyntaxView())
dlg.start()

```

## Events

Events are attached to the various components, when an event fires the controller is updated.

For instance [XItemListener](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XItemListener.html) are attached to List box clicks.

[XPropertyChangeListener](https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1beans_1_1XPropertyChangeListener.html) are attached to Radio buttons.

## Build

For automatic build run the following command from this folder.

```sh
make build
```

The following instructions are for manual build.

Build will compile the python scripts for this example into a single python script.

The following command will compile script as `tab_dialog.py` and embed it into `tab_dialog.odt`
The output is written into `build` folder in the projects root.

```sh
oooscript compile --embed --config "ex/general/tab_dialog/config.json" --embed-doc "ex/general/tab_dialog/tab_dialog.odt" --build-dir "build/tab_dialog"
```

See [Guide on embedding python macros in a LibreOffice Document](https://python-ooo-dev-tools.readthedocs.io/en/latest/guide/embed_python.html).

## Run Directly

Even though this is a multi-script example, it is possible to run and debug the example directly from this source folder. See the `run.py` script in this folder.

To start LibreOffice and display a message box run the following command from this folder.

```sh
make run
```

## Source

see [mvc](mvc)
