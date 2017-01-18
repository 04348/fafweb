/**
 * GW2.FR Database
 * http://db.gw2.fr/
 *
 * Design: Jona "Malcom" Detaille
 * Code: Yoann "Yoone" Bentz
 *       Elyas "Hirokoshi" Kamel
 *
 * Main website: http://www.gw2.fr/
 *
 */

(function($) {

	var content_url = "http://fils-des-ages-farouches.herokuapp.com/url=http://db.gw2.fr/",
		icon_loading = content_url + "img/item-tooltip-loading.gif",
		css_url = content_url + "css/remote-tooltip.css",
		icon_url = "http://fils-des-ages-farouches.herokuapp.com/url=http://data.gw2.fr/db-icons/<id>.png",
		icon_mystic_url = content_url + "img/tooltip-icon-mystic.png",
		icon_recipe_url = content_url + "img/tooltip-icon-recipe.png",
		api_url = "http://fils-des-ages-farouches.herokuapp.com/url=http://<domain>/tooltip/<type>/<id>",
		domains = {
			fr: "db.gw2.fr",
			en: "db.dulfy.net",
			de: "db.guildnews.de",
			es: "db.guildwars2-spain.com"
		},
		uri_format = /\/(item|recipe|mystic)\/([0-9]+)$/,
		data_prepend = "data-dbgw2fr-",
		tt_class = "dbgw2fr-tooltip",
		mouseX = 0,
		mouseY = 0;

	$.fn.showTooltip = function(type) {
		var lang = $(this).attr(data_prepend + "lang"),
			ttId = $(this).attr(data_prepend + type),
			ttUrl = api_url.replace("<domain>", domains[lang]).replace("<type>", type).replace("<id>", ttId),
			toolTip = $('div[' + data_prepend + type + '-tt="' + ttId + '"][' + data_prepend + 'lang="' + lang + '"]');

		if (toolTip.html() == undefined)
		{
			toolTip = $("<div />");
			$("body").append(toolTip);
			toolTip.html('<div class="inner"><img src="' + icon_loading + '" /></div>');
			toolTip.attr(data_prepend + type + "-tt", ttId);
			toolTip.attr(data_prepend + "lang", lang);
			toolTip.addClass(tt_class);

			$.getJSON(ttUrl, function(data) {
				toolTip.html('<div class="inner">' + data.html + '</div>');
				toolTip.addClass("loaded");
				$(this).moveTooltip(type, toolTip);
			});
		}

		$(toolTip).show();
	};

	$.fn.moveTooltip = function(type, toolTip) {
		var lang = $(this).attr(data_prepend + "lang"),
			ttId = $(this).attr(data_prepend + type);

		if (!toolTip)
			toolTip = $('div[' + data_prepend + type + '-tt="' + ttId + '"][' + data_prepend + 'lang="' + lang + '"]');

		var screenRight = $(document).scrollLeft() + $(window).width(),
			leftMax = mouseX + 15,
			leftMin = mouseX - toolTip.width() - 15,
			leftDecal = leftMax + toolTip.width() + 15 < screenRight ? leftMax : leftMin;

		var screenBottom = $(document).scrollTop() + $(window).height(),
			topMax = mouseY + 15,
			topMin = screenBottom - toolTip.height() - 15,
			topDecal = topMax + toolTip.height() + 15 < screenBottom ? topMax : topMin;

		toolTip.css({
			top: topDecal,
			left: leftDecal
		});
	};

	$(document).ready(function() {

		var head = $("head")[0],
			db_css = $("<link />");
		db_css.attr({
			rel: "stylesheet",
			type: "text/css",
			href: css_url
		});
		$(head).append(db_css);

		$("a").each(function(i, e) {
			for (var key in domains) {
				var url = $(e).attr("href");
				if (url && url.indexOf("http://" + domains[key]) == 0) {
					var result = uri_format.exec(url);
					if (result) {
						$(e).attr(data_prepend + "lang", key);
						$(e).attr(data_prepend + result[1], result[2]);

						var img = $("<img />");

						if (result[1] == "item")
							img.attr("src", icon_url.replace("<id>", result[2]));
						else if (result[1] == "recipe")
							img.attr("src", icon_recipe_url);
						else
							img.attr("src", icon_mystic_url);

						img.addClass(tt_class + "-icon");
						$(e).prepend(img);
					}
				}
			}
		});

		$("body").on("mousemove", "*[" + data_prepend + "item], *[" + data_prepend + "recipe], *[" + data_prepend + "mystic]", function(e) {
			mouseX = e.pageX;
			mouseY = e.pageY;

			var type = "item";
			if ($(this).attr(data_prepend + "recipe"))
				type = "recipe";
			else if ($(this).attr(data_prepend + "mystic"))
				type = "mystic";

			$(this).moveTooltip(type);
		});

		$("body").on("mouseenter", "*[" + data_prepend + "item], *[" + data_prepend + "recipe], *[" + data_prepend + "mystic]", function(e) {
			mouseX = e.pageX;
			mouseY = e.pageY;

			var type = "item";
			if ($(this).attr(data_prepend + "recipe"))
				type = "recipe";
			else if ($(this).attr(data_prepend + "mystic"))
				type = "mystic";

			$(this).showTooltip(type);
		});

		$("body").on("mouseleave", "*[" + data_prepend + "item], *[" + data_prepend + "recipe], *[" + data_prepend + "mystic]", function() {
			$("." + tt_class).hide();
		});

	});

}(jQuery));