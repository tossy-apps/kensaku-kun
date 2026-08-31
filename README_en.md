# Kensaku-kun (Excel Quick Search Tool)

A Windows desktop application designed to quickly and easily find data across massive amounts of Excel assets. It is particularly optimized for searching heavily formatted or layout-driven Excel files (such as "Excel Hoganshi")!

## Features
- **Ultra-Fast Search**: By parsing and loading Excel files into memory prior to searching, it enables instantaneous searches across hundreds of files even when search conditions change.
- **Versatile Search Conditions**: You can target or exclude not only cell values, but also sheet names, workbook names, comments, and text within shapes.
- **Flexible Keyword Input**: Supports multi-keyword OR searches via line breaks, and fuzzy matching using wildcards (*).
- **User-Friendly UI**: Optimized for finding files easily, featuring drag-and-drop for folders/file lists and the ability to open files directly from the search results.
- **Organized Output**: Search results can be exported to Excel. The tool is designed for practical business use, reproducing the formatting of searched cells and their surroundings, and also checking for strikethrough text.

## Important Notes
- To achieve maximum search speed, this tool heavily utilizes available memory and CPU resources. A memory usage threshold is implemented; if the limit is exceeded, the tool safely slows down processing to prevent system overload.
- While it excels at searching complex, layout-driven files ("Excel Hoganshi"), it is **not well-suited** for searching massive database-style Excel tables with tens of thousands of rows, as doing so consumes an excessive amount of memory.
- It does not support direct searching of Excel files hosted on HTTP(S) locations (like SharePoint). Please download them to a local or network drive before searching.

## System Requirements
- OS: Windows 10 / 11 (64-bit)
- Memory: 16GB or more recommended (Designed to operate on around 2-3GB for approximately 500 files, though actual usage depends on file contents).
- The executable is self-contained. It works standalone without requiring any separate .NET Runtime installation.

## Security and Privacy
- **Fully Offline**: This tool requires no internet connection. All search and parsing operations are completed entirely within your local PC.
- **Zero Data Transmission**: Your Excel file contents, search keywords, and settings are **never** transmitted to external servers, cloud services, or AI systems. You can safely use it with highly confidential business data.

## Security Warning on Initial Launch (Windows SmartScreen)
- As this software is an indie/personal project, it is not signed with an expensive commercial Code Signing Certificate.
- Therefore, Windows SmartScreen may display a warning screen stating **"Windows protected your PC"** upon your initial launch.

**[How to Run]**
1. Click **"More info"** on the warning screen.
2. Click the **"Run anyway"** button that appears at the bottom right to start the application normally.

*Note: This tool operates completely offline and never communicates with external networks. Please feel safe to use it.*

## Folder Structure & Included Files
Extracting the zip package will provide the following files:
- `けんさくくん.exe` (Kensaku-kun.exe) : Application executable
- `スタートメニューへの登録.vbs` (Register to Start Menu) : Creates shortcuts in the Windows Start Menu (Registry-free)
- `システム設定を開く.vbs` (Open System Settings) : Allows configuring memory limits and exclusion folders prior to running searches
- `help.html` : Offline user manual
- `tools/` : Utility scripts for uninstallation and resetting settings

## Quick Start
1. Double-click `けんさくくん.exe` (Kensaku-kun.exe) to launch.
2. Drag and drop the folder containing your Excel files, or a text file (.txt) with a list of files, into the **"Search Target (検索対象)"** box.
3. Move the focus away from the search target box. The pre-parsing process will begin automatically to prepare for the search.
4. Enter your desired text or conditions in the **"Search Conditions (検索条件)"** window and execute the search.

For detailed instructions, please refer to **[Help] - [Open Manual]** in the application (or view the bundled `help.html`).

## Trial Period and Limitations
You can use all features for free for **30 days** from the first launch, even without registering a license.
If the 30-day trial period expires, the following functional limitations will apply:
- A message will be displayed when opening an Excel file from the search results (though the file can still be opened).
- Hyperlinks in the search results and exported Excel files will be disabled.
- A background watermark will be applied to the exported Excel files.

To continue using the tool without limitations, please purchase and register a valid license.
*For purchase and registration instructions, please see the bundled `LICENSE.txt` or our official website (URL TBD).*

## Disclaimer
The author (developer) assumes no responsibility for any damages (including but not limited to search failure, data loss, business interruption, loss of profits, system crashes, or impact on other applications) arising from the use of this software. Please use it entirely at your own risk.
- This software is provided "as-is" without any warranties. There is no guarantee of fitness for a particular purpose, absence of bugs, or obligation to provide support.
- We cannot guarantee that unexpected bugs or failure of the trial period validation mechanism will not affect your system or files. We strongly recommend backing up important data beforehand.
- The tool can be used for both commercial and personal purposes; however, the user is solely responsible for resolving any issues arising from its use.

## Copyright and Licensing
The copyright of this tool belongs to the author.
Unauthorized redistribution, reverse engineering, modification, and sales are strictly prohibited.

### Third-Party Components
This software utilizes the following open-source libraries.
The full license texts and copyright notices for these libraries are included in the bundled `LICENSE.txt` (or in the "About" dialog within the app).
- **ClosedXML** (MIT License) - Copyright (c) ClosedXML
- **DocumentFormat.OpenXml** (MIT License) - Copyright (c) Microsoft Corporation.
- **Material Design In XAML Toolkit** (MIT License) - Copyright (c) 2015 James Willock, Mulholland Software and Contributors
- **Microsoft Edge WebView2** (WebView2 SDK License) - Copyright (c) Microsoft Corporation.
- **Google Fonts (Material Symbols)** (Apache License Version 2.0) - https://fonts.google.com/icons

## Contact
At present, we do not have plans to internationalize (localize) the application's UI. However, if there is strong demand from users, we will consider it. If you have any requests or feedback regarding this, please feel free to contact us!

As this is a personal project, it may be difficult to respond to all requests or inquiries, but we gratefully welcome your messages.
- **Email**: <tossy.apps@gmail.com> (tossy.apps)