from wtforms import (
    FileField,
    HiddenField,
    PasswordField,
    RadioField,
    SelectField,
    StringField,
    TextAreaField,
)
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.constants.themes import DEFAULT_THEME
from CTFd.forms import BaseForm
from CTFd.forms.fields import SubmitField
from CTFd.utils.config import get_themes


class SetupForm(BaseForm):
    ctf_name = StringField(
        "赛事名称", description="您的CTF赛事/平台名称"
    )
    ctf_description = TextAreaField(
        "说明", description="CTF说明"
    )
    user_mode = RadioField(
        "用户模式",
        choices=[("teams", "团队模式"), ("users", "个人模式")],
        default="users",
        description="控制用户是加入团队进行游戏（团队模式）还是以自己的身份进行游戏（个人模式）",
        validators=[InputRequired()],
    )

    name = StringField(
        "平台管理员账户",
        description="管理帐户的用户名",
        validators=[InputRequired()],
    )
    email = EmailField(
        "平台管理员邮箱",
        description="您的管理帐户电子邮件地址",
        validators=[InputRequired()],
    )
    password = PasswordField(
        "平台管理员账户密码",
        description="您的管理帐户密码",
        validators=[InputRequired()],
    )

    ctf_logo = FileField(
        "标志/徽标",
        description="用于网站的徽标，而不是CTF名称。用作主页按钮。（可选）",
    )
    ctf_banner = FileField(
        "横幅", description="用于主页的横幅。（可选）"
    )
    ctf_small_icon = FileField(
        "小标志/徽标",
        description="用户浏览器中使用的收藏夹图标。仅接受PNG。必须为32x32px。(可选)",
    )
    ctf_theme = SelectField(
        "主题",
        description="要使用的CTFd主题。可以稍后更改。",
        choices=list(zip(get_themes(), get_themes())),
        default=DEFAULT_THEME,
        validators=[InputRequired()],
    )
    theme_color = HiddenField(
        "主题颜色",
        description="主题用于控制美学的颜色。需要主题支持。（可选）",
    )

    start = StringField(
        "开始时间", description="计划启动CTF的时间。（可选）"
    )
    end = StringField(
        "结束时间", description="您的CTF计划结束的时间。（可选）"
    )
    submit = SubmitField("完成")
