var img_array=["a.jpg","c.png","d.jpg","f.png","g.png","h.png"];
var i=0;
function moveslider()
{
 if(i==img_array.length)
		i=0;
	document.getElementById("slide").src="images/"+img_array[i];
	i++;
	window.setTimeout("moveslider()",2000);
}