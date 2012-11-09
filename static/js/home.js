/**
 * Created with PyCharm.
 * User: marvin
 * Date: 11/8/12
 * Time: 8:39 PM
 * To change this template use File | Settings | File Templates.
 */

$(function () {
    $(".folderList").hover(
        function(){
            $(this).css("background-color", "#ccc");
        },
        function(){
            $(this).css("background-color", "#eee");
        }
    );
})