// product.home.js
// ===============

$(function () {

    $sidebar = $("#sidebar");
    $sidebarGroups = $("#sidebar li:has(a.title)");
    $sidebarMembers = $("#sidebar li:not(:has(a.title))");


    sidebarItem = function(element){
        this.element = $(element);
        this.groupName = this.element.find("a").attr("name");
        this.isGroup = this.element.find(".title")[0]?true:false;
        this.stateImg = this.element.find("i");
        this.isShow = !(this.stateImg.hasClass("icon-plus") || (this.element.css("display")=="none"));
        this.member = this.isGroup && $sidebarMembers.filter(":has(a[name='"+this.groupName+"'])");
    }
    sidebarItem.prototype = {
        constructor: sidebarItem,

        reflash: function(){
            this.isShow = !(this.stateImg.hasClass("icon-plus") || (this.element.css("display")=="none"));
            
            if(this.isGroup && this.isShow){
                this.stateImg.removeClass("icon-minus") && this.stateImg.addClass("icon-plus");
            }else{
                this.stateImg.removeClass("icon-plus") && this.stateImg.addClass("icon-minus");
            }
        },
        show: function(){
        	!(this.isShow) && this.element.show();
        },
        hide: function(){
        	this.isShow && this.element.hide();
        },
        showMember: function(){
            this.member.each(function(){
        	    $(this).show("slow");
            })
            this.reflash();
        },
        hideMember: function(){
        	this.member.each(function(){
        	    $(this).hide("slow");
            })
            this.reflash();
        }
    }

    //init page
    $sidebar.find("li").each(function(){
        var item = new sidebarItem(this);
        !(item.isGroup) && item.hide();
        item.isGroup && item.element.toggle($.proxy(item.showMember, item), $.proxy(item.hideMember, item));
    });

})