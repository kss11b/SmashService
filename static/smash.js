$(document).ready(function() {
  $("select").formSelect();

  $(".tier-clear").click(function() {
    $(".character-list").empty();
  });

  $(".stage-clear").click(function() {
    $(".stage-list").empty();
  });

  function selectRandomTier() {
    var tier = $(".tier-select")
      .children("option:selected")
      .val();
    console.log(tier, "tier");
    var url = "http://0.0.0.0:5000/tier";
    if (tier) {
      url += "/";
    }
    $.ajax({
      url: url + tier
    }).done(function(data) {
      $(".character-list").append(
        `<li class="collection-item">${data.character}  <span class="badge ">${
          data.tier
        }</span></li>`
      );
    });
  }

  function selectRandomStage() {
    var stage = $(".stage-select")
      .children("option:selected")
      .val();
    console.log(stage, "stage");
    var url = "http://0.0.0.0:5000/stage";
    if (stage) {
      url += "/";
    }
    $.ajax({
      url: url + stage
    }).done(function(data) {
      $(".stage-list").append(`<li class="collection-item">${data}</li>`);
    });
  }

  $(".tier-submit").click(selectRandomTier);
  $(".stage-submit").click(selectRandomStage);
});
