#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regex
puts ARGV[0].scan(/^h.n$/).join
