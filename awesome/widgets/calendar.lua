local wibox = require("wibox")
local dpi = require("beautiful").xresources.apply_dpi
local gears = require("gears")
local beautiful = require("beautiful")
local awful = require("awful")

local calendar = {}

calendar.create = function(screen)
    local clock_widget = wibox.widget.textclock("<span font='" .. beautiful.title_font .. "'>%l:%M %p</span>", 1)

    awful.tooltip({
        objects = { clock_widget },
        mode = "outside",
        align = "right",
        timer_function = function()
            return os.date("The date today is %B %d %Y.")
        end,
        preferred_positions = { "right", "left", "top", "bottom" },
        margin_leftright = dpi(8),
        margin_topbottom = dpi(8),
    })

    local function cal_shape(cr, width, height)
        gears.shape.partially_rounded_rect(cr, width, height, false, false, true, true, 12)
    end

    local month_calendar = awful.widget.calendar_popup.month({
        screen = screen,
        start_sunday = true,
        spacing = 10,
        font = beautiful.title_font,
        long_weekdays = true,
        margin = 0, -- 10
        style_month = { border_width = 0, shape = cal_shape, padding = 12 },
        style_header = { border_width = 0, bg_color = "#00000000" },
        style_weekday = { border_width = 0, bg_color = "#00000000" },
        style_normal = { border_width = 0, bg_color = "#00000000" },
        style_focus = { border_width = 0, bg_color = "#8AB4F8" },
    })

    month_calendar:attach(clock_widget, "tc", { on_pressed = true, on_hover = false })

    return clock_widget
end


return calendar
