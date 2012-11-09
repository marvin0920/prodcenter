// product.version.home.js
// ===============



$(function () {
		
    // $mapform = $('#chose .input-prepend');
    //     {% for ver in versions|dictsort:"product.id"%}
    //         {% ifchanged ver.product.name %}
	   //  $input_label = $("<label class='add-on disabled' style='float:left;'>");
	   //  $input_item = $("<input type='checkbox' value='{{ ver.product.name }}' name='prods'>");
	   //  $span_pname = $("<span></span>").addClass('input-xlarge uneditable-input').css({'width': '420px','float': 'left'});
    //             $span_pname.html("<i class='icon-tag'></i>&nbsp;{{ ver.product.name|escape }}{{ ver.product.alias|escape }}</span>");

	   //  {% ifequal ver.product.name 'MOC' %}
	   //      $input_label.addClass('active');
	   //      $input_item.attr({ checked: 'checked', disabled: 'true' });
	   //      $mapform.prepend($span_pname);
	   //      $mapform.prepend($input_label.append($input_item));
	   //  {% else %}
	   //      $mapform.append($input_label.append($input_item));
	   //      $mapform.append($span_pname);
    //             {% endifequal %}
                
    //         {% endifchanged %}
    //     {% endfor %}

    $mapForm = $("#chose");
    $mapInputBox = $mapForm.find(".input-prepend");
    $("#checkMOC").insertBefore("#chose .input-prepend>div:first");
    $mapInputBox.find("input:checked").parent().addClass("active");

    $('.add-on :checkbox').each(function(){
        $(this).on('click', function(e){
        	$(this).parent().hasClass("active")?$(this).parent('.add-on').removeClass('active'):$(this).parent().addClass('active');
        })
    });

    $('#findMap').on('click', function(e){
        e.preventDefault();
        var prodnames = [];
        $('.active :checkbox').each(function(){
        	prodnames.push($(this).val());
        });

        $.ajax({
        	type : "get",
            url : "/product/version/map/",
            data : {prods:prodnames.join('_')},
            success : function(data, textStatus) {
                $('#results').html(data)
                $mapForm.modal('hide')
            },
            error : function() {
                // 请求出错处理
                alert("网络服务链接出错！");
            }
        })

    });

    // search version with ajax
    $('#search').on('click', function(e){
        e.preventDefault();
        var keywords = $("#searchkey").val().toLowerCase();
        $.ajax({
            type : "get",
            url : "/product/version/search/",
            data : {words:keywords},
            success : function(data, textStatus) {
                $('#results').html(data);
            },
            error : function() {
                // 请求出错处理
                alert("网络服务链接出错！");
            }
        })
    })

});
