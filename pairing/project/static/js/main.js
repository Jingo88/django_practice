$(document).ready(function(){

	console.log("We Are Connected");

	$('.movie_form').on('submit', function(event){
		event.preventDefault();
		var movie_title = $('input[name="search_value"]').val();

		$.get({
			url: "search",
			data: {"title": movie_title},
			dataType: "json",
			success: function(data){
				console.log(data)

///////////////////////		First Way		///////////////////////////////

//
				var template = $('#list').html();
				var renderM = Mustache.render(template,data);
				$('#blah').html(renderM)




///////////////////////		Second Way		///////////////////////////////

					// var tpl = "Movies:<ul>{{#Search}}<li>{{Title}} {{Type}}" +
     // 			     "{{Year}}</li>{{/Search}}</ul>";
					// var renderM = Mustache.render(tpl, data)
					// $('#blah').html(renderM)	

					// //enter the list
					// //when it sees the items in the list it creates it's own "context"
					// //We pass that "context" in as a argument in the render method
					// //# sign just means enter


				// var search_list = function(){
				// var template = $('#list').html();

				// }
				

				
			}
		})
	})









				// $.each(moviesRes, function(x){
				// // .html() get the contents of the first element inside #list
				// 	// console.log(moviesRes[x])
				// 	// var template = $('#list').html()

				// 	var el = moviesRes[x]
				// 	console.log(el)
				// 	var tpl = "Movies:<ul>{{#el}}<li>{{el.Title}} {{Type}}" +
    //       "{{Year}}</li>{{/el}}</ul>";
				// 	var renderM = Mustache.render(tpl, el)
				// 	$('#blah').append(renderM)	
				// })
















// verbatim tag wraps around all the mustache tags in the html file
// if you're sending template from django DJ will attempt to fill in blanks by Default 
// Verbatim says to leave it alone so we can render with our own data from the JS file
// Mustache same syntax as DJ variables
// When we render a template through DJ and it loads mustache items we want to make sure DJ does not interfere with our JS data going on the page
});