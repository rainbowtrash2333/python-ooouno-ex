# Grid Example

<p align="center">
<img src="https://user-images.githubusercontent.com/4193389/283202594-d22eaa6e-7c27-470e-9c61-f1c94952b903.png" width="662" height="410">
</p>

This example demonstrates how to create a Dialog window programmatically and add a grid control
to the dialog. Data is extracted from an existing spreadsheet and used to populate the grid control.

This demo uses This demo uses [OOO Development Tools] (OooDev).
Also available as a LibreOffice [Extension](https://extensions.libreoffice.org/en/extensions/show/41700).

See Also:

- [ooodev.dialog.dialogs.Dialogs](https://python-ooo-dev-tools.readthedocs.io/en/latest/src/dialog/dialogs.html)
- [ooodev.dialog.dl_control.ctl_dialog.CtlDialog](https://python-ooo-dev-tools.readthedocs.io/en/latest/src/dialog/dl_control/ctl_dialog.html)
- [ooodev.dialog.dl_control.ctl_grid.CtlGrid](https://python-ooo-dev-tools.readthedocs.io/en/latest/src/dialog/dl_control/ctl_grid.html)
- [ooodev.dialog.dl_control.ctl_button.CtlButton](https://python-ooo-dev-tools.readthedocs.io/en/latest/src/dialog/dl_control/ctl_button.html)

### Dev Container

From this folder.

```sh
python -m start
```

### Cross Platform

From this folder.

```sh
python -m start
```

### Linux/Mac

```sh
python ./ex/dialog/grid/start.py
```

### Windows

```ps
python .\ex\dialog\grid\start.py
```

## Embedding

### Embedding the Dialog in sales_data.ods

The dialog can be embedded in a spreadsheet in the following two ways:

The recommended way is to have [OOO Development Tools Extension] installed and use the number `1` method below.

These commands must be run from this current folder in a terminal.

1. **Embedding the Dialog in sales_data.ods use with extension**

   The dialog can be embedded in sales_data.ods running the following command in the terminal:

   ```sh
   make build
   ```

   With extension installed this will create a much more lightweight file. The startup for the macro will be faster.

2. **Embedding the Dialog in sales_data.ods use without extension**

    With this method the macro will run without the extension installed.

   The dialog can be embedded in sales_data.ods running the following command in the terminal:

   ```sh
   make build_ooodev
   ```

    This will include the required `ooodev` packages in the document. This will create a much larger file. The startup for the macro will be slower. After first load the macro files will be cached and running the macro again will be faster.

### Build output

After running the build command, the output will be in the `build/sales_grid` folder of this projects root.
The file name will be `grid_dialog.ods`.

See [Guide on embedding python macros in a LibreOffice Document](https://python-ooo-dev-tools.readthedocs.io/en/latest/guide/embed_python.html).

### Running the embedded Dialog

To run the embedded dialog, open the `sales_data.ods` file in LibreOffice and run
`Tools -> Macros -> Run Macro...` and select `grid_dialog.ods -> grid_dialog -> show_grid` and click `Run`.


## Live LibreOffice Python

Instructions to run this example in [Live-LibreOffice-Python](https://github.com/Amourspirit/live-libreoffice-python).

Start Live-LibreOffice-Python in a Codespace or in a Dev Container.

In the terminal run:

```bash
cd examples
gitget 'https://github.com/Amourspirit/python-ooouno-ex/tree/main/ex/dialog/grid'
```

This will copy the `gird` example to the examples folder.

In the terminal run:

```bash
cd grid
python -m start
```

[OOO Development Tools]: https://python-ooo-dev-tools.readthedocs.io/en/latest/
[OOO Development Tools Extension]: https://extensions.libreoffice.org/en/extensions/show/41700
