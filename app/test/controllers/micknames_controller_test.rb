require "test_helper"

class MicknamesControllerTest < ActionDispatch::IntegrationTest
  test "should get index" do
    get micknames_index_url
    assert_response :success
  end
end
