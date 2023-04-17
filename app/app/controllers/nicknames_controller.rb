require 'net/https'

class NicknamesController < ApplicationController
  def index
  end

  def create
    http = Net::HTTP.new(ENV['NICKNAME_API_HOST'], 443)
    http.use_ssl = true

    req = Net::HTTP::Post.new('/api/HttpTrigger')
    req['x-functions-key'] = ENV['AUTH_KEY']
    req.body = { name: params[:name] }.to_json

    response = http.request(req)

    @nickname = response.body
  end
end
