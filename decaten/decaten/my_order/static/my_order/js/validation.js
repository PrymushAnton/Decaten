/**
 * Define the version of the Google Pay API referenced when creating your
 * configuration
 *
 * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#PaymentDataRequest|apiVersion in PaymentDataRequest}
 */
const baseRequest = {
    apiVersion: 2,
    apiVersionMinor: 0
  };
  
  /**
   * Card networks supported by your site and your gateway
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#CardParameters|CardParameters}
   * @todo confirm card networks supported by your site and gateway
   */
  const allowedCardNetworks = ["AMEX", "DISCOVER", "INTERAC", "JCB", "MASTERCARD", "VISA"];
  
  /**
   * Card authentication methods supported by your site and your gateway
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#CardParameters|CardParameters}
   * @todo confirm your processor supports Android device tokens for your
   * supported card networks
   */
  const allowedCardAuthMethods = ["PAN_ONLY", "CRYPTOGRAM_3DS"];
  
  /**
   * Identify your gateway and your site's gateway merchant identifier
   *
   * The Google Pay API response will return an encrypted payment method capable
   * of being charged by a supported gateway after payer authorization
   *
   * @todo check with your gateway on the parameters to pass
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#gateway|PaymentMethodTokenizationSpecification}
   */
  const tokenizationSpecification = {
    type: 'PAYMENT_GATEWAY',
    parameters: {
      'gateway': 'example',
      'gatewayMerchantId': 'exampleGatewayMerchantId'
    }
  };
  
  /**
   * Describe your site's support for the CARD payment method and its required
   * fields
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#CardParameters|CardParameters}
   */
  const baseCardPaymentMethod = {
    type: 'CARD',
    parameters: {
      allowedAuthMethods: allowedCardAuthMethods,
      allowedCardNetworks: allowedCardNetworks
    }
  };
  
  /**
   * Describe your site's support for the CARD payment method including optional
   * fields
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#CardParameters|CardParameters}
   */
  const cardPaymentMethod = Object.assign(
    {},
    baseCardPaymentMethod,
    {
      tokenizationSpecification: tokenizationSpecification
    }
  );
  
  /**
   * An initialized google.payments.api.PaymentsClient object or null if not yet set
   *
   * @see {@link getGooglePaymentsClient}
   */
  let paymentsClient = null;
  
  /**
   * Configure your site's support for payment methods supported by the Google Pay
   * API.
   *
   * Each member of allowedPaymentMethods should contain only the required fields,
   * allowing reuse of this base request when determining a viewer's ability
   * to pay and later requesting a supported payment method
   *
   * @returns {object} Google Pay API version, payment methods supported by the site
   */
  function getGoogleIsReadyToPayRequest() {
    return Object.assign(
        {},
        baseRequest,
        {
          allowedPaymentMethods: [baseCardPaymentMethod]
        }
    );
  }
  
  /**
   * Configure support for the Google Pay API
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#PaymentDataRequest|PaymentDataRequest}
   * @returns {object} PaymentDataRequest fields
   */
  function getGooglePaymentDataRequest() {
    const paymentDataRequest = Object.assign({}, baseRequest);
    paymentDataRequest.allowedPaymentMethods = [cardPaymentMethod];
    paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
    paymentDataRequest.merchantInfo = {
      // @todo a merchant ID is available for a production environment after approval by Google
      // See {@link https://developers.google.com/pay/api/web/guides/test-and-deploy/integration-checklist|Integration checklist}
      // merchantId: '12345678901234567890',
      merchantName: 'Decaten'
    };
    return paymentDataRequest;
  }
  
  /**
   * Return an active PaymentsClient or initialize
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/client#PaymentsClient|PaymentsClient constructor}
   * @returns {google.payments.api.PaymentsClient} Google Pay API client
   */
  function getGooglePaymentsClient() {
    if ( paymentsClient === null ) {
      paymentsClient = new google.payments.api.PaymentsClient({environment: 'TEST'});
    }
    return paymentsClient;
  }
  
  /**
   * Initialize Google PaymentsClient after Google-hosted JavaScript has loaded
   *
   * Display a Google Pay payment button after confirmation of the viewer's
   * ability to pay.
   */
  function onGooglePayLoaded() {
    const paymentsClient = getGooglePaymentsClient();
    paymentsClient.isReadyToPay(getGoogleIsReadyToPayRequest())
        .then(function(response) {
          if (response.result) {
            addGooglePayButton();
            // @todo prefetch payment data to improve performance after confirming site functionality
            // prefetchGooglePaymentData();
          }
        })
        .catch(function(err) {
          // show error in developer console for debugging
          console.error(err);
        });
  }
  
  /**
   * Add a Google Pay purchase button alongside an existing checkout button
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#ButtonOptions|Button options}
   * @see {@link https://developers.google.com/pay/api/web/guides/brand-guidelines|Google Pay brand guidelines}
   */
//   function addGooglePayButton() {
//     const paymentsClient = getGooglePaymentsClient();
//     const button =
//         paymentsClient.createButton({
//           onClick: onGooglePaymentButtonClicked,
//           allowedPaymentMethods: [baseCardPaymentMethod]
//         });
//     document.getElementById('container').appendChild(button);
//   }
  
  /**
   * Provide Google Pay API with a payment amount, currency, and amount status
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/request-objects#TransactionInfo|TransactionInfo}
   * @returns {object} transaction info, suitable for use as transactionInfo property of PaymentDataRequest
   */
  function getGoogleTransactionInfo() {
    return {
      countryCode: 'US',
      currencyCode: 'UAH',
      totalPriceStatus: 'FINAL',
      // set to cart total
      totalPrice: $('.final_price').val()
    };
  }
  
  /**
   * Prefetch payment data to improve performance
   *
   * @see {@link https://developers.google.com/pay/api/web/reference/client#prefetchPaymentData|prefetchPaymentData()}
   */
  function prefetchGooglePaymentData() {
    const paymentDataRequest = getGooglePaymentDataRequest();
    // transactionInfo must be set but does not affect cache
    paymentDataRequest.transactionInfo = {
      totalPriceStatus: 'NOT_CURRENTLY_KNOWN',
      currencyCode: 'UAH'
    };
    const paymentsClient = getGooglePaymentsClient();
    paymentsClient.prefetchPaymentData(paymentDataRequest);
  }
  
  /**
   * Show Google Pay payment sheet when Google Pay payment button is clicked
   */
  
//   function onGooglePaymentButtonClicked() {
//     const paymentDataRequest = getGooglePaymentDataRequest();
//     paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
  
//     const paymentsClient = getGooglePaymentsClient();
//     paymentsClient.loadPaymentData(paymentDataRequest)
//         .then(function(paymentData) {
//           // handle the response
//           processPayment(paymentData);
//         })
//         .catch(function(err) {
//           // show error in developer console for debugging
//           console.error(err);
//         });
//   }

//   $(".send").click(function(){
//     const paymentDataRequest = getGooglePaymentDataRequest();
//     paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
  
//     const paymentsClient = getGooglePaymentsClient();
//     paymentsClient.loadPaymentData(paymentDataRequest)
//         .then(function(paymentData) {
//           // handle the response
//           processPayment(paymentData);
//         })
//         .catch(function(err) {
//           // show error in developer console for debugging
//           console.error(err);
//         });
//   })

  /**
   * Process payment data returned by the Google Pay API
   *
   * @param {object} paymentData response from Google Pay API after user approves payment
   * @see {@link https://developers.google.com/pay/api/web/reference/response-objects#PaymentData|PaymentData object reference}
   */
  function processPayment(paymentData) {
    // show returned data in developer console for debugging
      console.log(paymentData);
    //   window.location.replace('/')
    $.ajax({
        url: '/add_order/',
        type: "POST",
        data: {
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            area: $("#area-select option:selected").text(),
            city: $("#city-select option:selected").text(),
            location: $("#location-select option:selected").text(),
            last_name: $("#last_name").val(),
            first_name: $("#first_name").val(),
            middle_name: $("#middle_name").val(),
            number: $("#number").val(),
        },
        success: function(response) {
            window.location.replace('/')
        }
    }
    )
    // @todo pass payment token to your gateway to process payment
    paymentToken = paymentData.paymentMethodData.tokenizationData.token;
  }



$(document).ready(function() {
    $(".send").click(function(e) {
        e.preventDefault();
        console.log($("#area-select option:selected").val())
        $.ajax({
            url: '/validation/',
            type: "POST",
            data: {
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                area: $("#area-select option:selected").text(),
                area_val: $("#area-select option:selected").val(),
                city: $("#city-select option:selected").text(),
                city_val: $("#city-select option:selected").val(),
                location: $("#location-select option:selected").text(),
                location_val: $("#location-select option:selected").val(),
                last_name: $("#last_name").val(),
                first_name: $("#first_name").val(),
                middle_name: $("#middle_name").val(),
                number: $("#number").val(),
            },
            success: function(data){
                if (data == '321') {
                    $('.modal').modal('show');
                }
                if (data == '100'){
                    console.log(100)
                    // window.location.replace('/')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    const paymentDataRequest = getGooglePaymentDataRequest();
                    paymentDataRequest.transactionInfo = getGoogleTransactionInfo();
                
                    const paymentsClient = getGooglePaymentsClient();
                    paymentsClient.loadPaymentData(paymentDataRequest)
                        .then(function(paymentData) {
                        // handle the response
                        processPayment(paymentData);
                        })
                        .catch(function(err) {
                        // show error in developer console for debugging
                        console.error(err);
                        });
                } else if (data == '1'){
                    console.log("Заповніть всі поля!")
                    var inputs = document.querySelectorAll('input')
                    for (var input of inputs) {
                        if (input.classList.contains('is-invalid')) {
                            input.classList.remove('is-invalid')
                            $("select").removeClass('is-invalid')
                        }
                        if (input.value == ''){
                            input.classList.add('is-invalid')
                            // $(".invalid-feedback").html('Заповніть це поле!')
                        }
                    }
                    $(".invalid-feedback").html('Заповніть це поле!')
                } else if (data == '2'){
                    console.log('Введіть коректний номер картки!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#credit_card").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний номер картки!')
                } else if (data == '3'){
                    console.log('Введіть коректний місяць!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#month").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний місяць!')
                } else if (data == '4'){
                    console.log('Введіть коректний рік!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#year").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний рік!')
                } else if (data == '5'){
                    console.log('Введіть коректний cvv код!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#cvv").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть коректний cvv код!')
                } else if (data == '6'){
                    console.log('Введіть прізвище коректно!')
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#last_name").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть прізвище коректно!')
                } else if (data == '7'){
                    console.log("Введіть ім'я коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#first_name").addClass('is-invalid')
                    $(".invalid-feedback").html("Введіть ім'я коректно!")
                } else if (data == '8'){
                    console.log("Введіть по батькові коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#middle_name").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть по батькові коректно!')
                } else if (data == '9'){
                    console.log("Введіть телефон коректно!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#number").addClass('is-invalid')
                    $(".invalid-feedback").html('Введіть телефон коректно!')
                } else if (data == '10'){
                    console.log("Виберіть область!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#area-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Виберіть область!')
                } else if (data == '11'){
                    console.log("Виберіть місто!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#city-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Виберіть місто!')
                } else if (data == '12'){
                    console.log("Виберіть відділення!")
                    $("input").removeClass('is-invalid')
                    $("select").removeClass('is-invalid')
                    $("#location-select").addClass('is-invalid')
                    $(".invalid-feedback").html('Виберіть відділення!')
                } 
            }
        })
    })
})