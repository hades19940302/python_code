var htmlAnchorDirective = valueFn({
    restrict: 'E',
    compile: function(element, attr) {
        if (!attr.href && !attr.xlinkHref && !attr.name) {
            return function(scope, element) {
                var href = toString.call(element.prop('href')) === '[object SVGAnimatedString]' ? 'xlink:href': 'href';
                element.on('click',
                function(event) {
                    if (!element.attr(href)) {
                        event.preventDefault();
                    }
                });
            };
        }
    }
});
var ngAttributeAliasDirectives = {};
forEach(BOOLEAN_ATTR,
function(propName, attrName) {
    if (propName == "multiple") return;
    var normalized = directiveNormalize('ng-' + attrName);
    ngAttributeAliasDirectives[normalized] = function() {
        return {
            restrict: 'A',
            priority: 100,
            link: function(scope, element, attr) {
                scope.$watch(attr[normalized],
                function ngBooleanAttrWatchAction(value) {
                    attr.$set(attrName, !!value);
                });
            }
        };
    };
});
forEach(ALIASED_ATTR,
function(htmlAttr, ngAttr) {
    ngAttributeAliasDirectives[ngAttr] = function() {
        return {
            priority: 100,
            link: function(scope, element, attr) {
                if (ngAttr === "ngPattern" && attr.ngPattern.charAt(0) == "/") {
                    var match = attr.ngPattern.match(REGEX_STRING_REGEXP);
                    if (match) {
                        attr.$set("ngPattern", new RegExp(match[1], match[2]));
                        return;
                    }
                }


function onClick() {
    var iconClasses = scope.icons || settings.expandIconClasses;
    element.toggleClass(iconClasses);
    var summaryRow = element.closest('tr');
    var detailCell = summaryRow.next('tr').find('.detail');
    var duration = scope.duration ? parseInt(scope.duration, 10) : settings.duration;
    if (summaryRow.hasClass('expanded')) {
        var options = {
            duration: duration,
            complete: function() {
                summaryRow.toggleClass('expanded');
            }
        };
        detailCell.find('.detail-expanded').slideUp(options);
    } else {
        summaryRow.toggleClass('expanded');
        if (detailCell.find('.detail-expanded').length === 0) {
            detailCell.wrapInner('<div class="detail-expanded"></div>');
        }
        detailCell.find('.detail-expanded').slideDown(duration);
    }
}