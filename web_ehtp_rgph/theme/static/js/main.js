$(document).ready(function () {
	spinner_wrapper = $("#spinner-wrapper");
	client_ip_info = $("#client-ip-info");
	client_ip_local = $("#client-ip-local");
	$.ajax(spinner_wrapper.data("api"), {
		dataType: 'json',
		timeout: 50000,
		beforeSend: function () {
			spinner_wrapper.removeClass("hidden");
		},

		success: function (data) {
			console.log(data);
			if (data.status == 405 || data.status == 404) {
				client_ip_local.find("#ip").text(data.ip);
				client_ip_local.removeClass("hidden");
			}
			else if (data.status == 200) {
				client_ip_info.find("#ip").text(data.ip);
				client_ip_info.find("#country").text(data.country);
				client_ip_info.find("#city").text(data.city);
				client_ip_info.find("#localisation").text(
					data.longitude + "|" + data.latitude
				);
				client_ip_info.removeClass("hidden");
			}

			spinner_wrapper.addClass("hidden");
		},
		error: function (data) {
			console.log(data);
			spinner_wrapper.find("#spinner-message").text(
				'Sorry we cannot retieve your localisation! Server error. !'
			);
		}
	});

	$(".login-row").click(function () {
		$("#id_username").val(($(this).find(".username-row").html()));
		$("#id_password").val(($(this).find(".password-row").html()));
	});
});