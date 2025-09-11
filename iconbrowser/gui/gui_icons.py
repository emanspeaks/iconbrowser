from pyrandyos.gui.icons.iconfont import IconSpec
from pyrandyos.gui.icons.thirdparty.codicons import Codicons
from pyrandyos.gui.icons.thirdparty.codicons import names as codicon_names
from pyrandyos.gui.icons.thirdparty.fa5.solid import names as fa5_s_names
from pyrandyos.gui.icons.thirdparty.fa5.solid import Fa5_Solid
from pyrandyos.gui.icons.thirdparty.fluentui.resize import FluentUI_Resize
from pyrandyos.gui.icons.thirdparty.fluentui.resize import names as fluentui_r_names  # noqa: E501

ConfigIcon = IconSpec.generate_iconspec(Codicons, glyph=codicon_names.json)
ProgramIcon = IconSpec.generate_iconspec(Fa5_Solid, glyph=fa5_s_names.icons)
CopyCodeIcon = IconSpec.generate_iconspec(FluentUI_Resize, glyph=fluentui_r_names.ic_fluent_clipboard_code_20_regular)  # noqa: E501
CopyNameIcon = IconSpec.generate_iconspec(FluentUI_Resize, glyph=fluentui_r_names.ic_fluent_clipboard_letter_20_regular)  # noqa: E501
