
												




													// The following example creates a marker in Stockholm, Sweden using a DROP
													// animation. Clicking on the marker will toggle the animation between a BOUNCE
													// animation and no animation.

													var marker;

													function initMap() {
														var map = new google.maps.Map(document.getElementById('map'), {
															zoom: 13,
															center: {lat: 43.7321331, lng: -79.6757215}
														});
														var geocoder = new google.maps.Geocoder;
														var infowindow = new google.maps.InfoWindow;


														marker = new google.maps.Marker({
															map: map,
															draggable: true,
															animation: google.maps.Animation.DROP,
															position: {lat: 43.7321331, lng: -79.6757215}
														});
														marker.addListener('click', toggleBounce);
													}

													function toggleBounce() {
														if (marker.getAnimation() !== null) {
															marker.setAnimation(null);
														} else {
															marker.setAnimation(google.maps.Animation.BOUNCE);
													}
															setTimeout(function(){ marker.setAnimation(null); }, 203);
														}

