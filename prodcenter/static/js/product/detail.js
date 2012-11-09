// product.detail.js
// ===============

$(function () {
    // functions
    $functionBars = $("#func ul li");
    $functionPanes = $("#func .tab-content .tab-pane");

    $functionBars.first().addClass("active") && $functionPanes.first().addClass("active in");

    var groupName = $("#productTitle span").attr("group");
    var activeItem = new sidebarItem($sidebar.find("li:has(a[name='"+groupName+"'])")[0]);
    activeItem.showMember();
})