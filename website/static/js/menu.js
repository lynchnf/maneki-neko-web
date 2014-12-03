var MyMenu = new Object();

MyMenu.toggle = function(event) {
    event.preventDefault();
    event.stopPropagation();
    var $this = $(this)
    if ($this.is('.disabled, :disabled')) return;
    var $parent = MyMenu.getParent($this);
    var isActive = $parent.hasClass('open');
    MyMenu.clearMenus();
    if (!isActive) {
        if ('ontouchstart' in document.documentElement && !$parent.closest('.navbar-nav').length) {
            // if mobile we use a backdrop because click events don't delegate
            $('<div class="dropdown-backdrop"/>').insertAfter($(this)).on('click', clearMenus);
        }
        var relatedTarget = {
            relatedTarget : this
        };
        $parent.trigger(e = $.Event('show.bs.dropdown', relatedTarget));
        if (e.isDefaultPrevented()) return;
        $this.trigger('focus').attr('aria-expanded', 'true');
        MyMenu.openAncestors($parent);
        $parent.addClass('open').trigger('shown.bs.dropdown', relatedTarget);
    }
    return false;
}

MyMenu.clearMenus = function() {
    var backdrop = '.dropdown-backdrop';
    $(backdrop).remove();
    var toggle = '[data-toggle="dropdown"]';
    $(toggle).each(function() {
        var $this = $(this);
        var $parent = MyMenu.getParent($this);
        var relatedTarget = {
            relatedTarget : this
        };
        if (!$parent.hasClass('open')) return;
        $parent.trigger(e = $.Event('hide.bs.dropdown', relatedTarget));
        if (e.isDefaultPrevented()) return;
        $this.attr('aria-expanded', 'false');
        $parent.removeClass('open').trigger('hidden.bs.dropdown', relatedTarget);
    });
}

MyMenu.getParent = function($this) {
    var selector = $this.attr('data-target');
    if (!selector) {
        selector = $this.attr('href');
        selector = selector && /#[A-Za-z]/.test(selector) && selector.replace(/.*(?=#[^\s]*$)/, ''); // strip for ie7
    }
    var $parent = selector && $(selector);
    return $parent && $parent.length ? $parent : $this.parent();
}

MyMenu.openAncestors = function($this) {
    var $grandparent = $this.parent().parent();
    if ($grandparent.hasClass('dropdown')) {
        MyMenu.openAncestors($grandparent);
        $grandparent.addClass('open');
    }
}

$('[data-toggle="dropdown"]').on('click', MyMenu.toggle);