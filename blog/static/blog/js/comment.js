$(document).ready(function() {
	console.log('0');
	$('#col-lg-12').load('../../getComment', function(data) {
		console.log('1');
		var comment;
		for(comment in data.comments) {
			console.log(comment);
		}
		console.log('2');

	});
	$('#btn_comment_submit').click(function(datas) {
		var blogId = $("#thisBlogID").attr('value');
		<!--console.log('addComment?comment=' + $('#tbCommentBody').val() + '&blogid=' + {{data.blogid}});-->
		console.log('../../addComment?comment=' + $('#tbCommentBody').val() + '&blogid=' + $("#thisBlogID").attr('value'));
		$.ajax({
			url: '../../addComment?comment=' + $('#tbCommentBody').val() + '&blogid=' + $("#thisBlogID").attr('value'),
			dataType: 'json',
			success: function(data) {
				$('#tbCommentBody').val("");
				console.log('11111111111');
				console.log(data);
				getComment(blogId);
				console.log(data.comments);
				$('#comments').text(data.comments+' comments');

			}
		});
	});

});

function getComment(blogId) {
	console.log('000000000000');
	$.ajax({
		url: '../../getCommentJson?blogId=' + blogId,
		dataType: 'json',
		success: function(data) {
			comment(data);
		}
	});
}

function comment(datas) {
	console.log(datas);
	var tmpHtml='';
	$.each(datas, function(i, data) {
		tmpHtml += '<div class="social-feed-box">' +
			'<div class="social-avatar">' +
			'<a href="" class="pull-left">' +
			'<img alt="image" src="../../static/blog/img/a1.jpg">' +
			'</a>' +
			'<div class="media-body">' +
			'<a href="#">' +
			data.fields.username +
			'</a>' +
			'<small class="text-muted">' +
			data.fields.dataTime + '</small>' +
			'</div>' +
			'</div>' +
			'<div class="social-body">' +
			'<p>' +
			data.fields.content +
			'</p>' +
			'</div>' +
			'</div>'
	})
	$('.col-lg-12').html(tmpHtml);
}