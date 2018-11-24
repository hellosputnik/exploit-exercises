local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 50001))

function hash(password)
  prog = io.popen("echo "..password.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local line, err = client:receive()
  if not err then
      print("trying " .. line) -- log from where ;\
      local h = hash(line)

      if h ~= "4754a4f4bd5787accd33de887b9250a0691dd198" then
          client:send("Better luck next time\n");
      else
          client:send("Congrats, your token is 413**CARRIER LOST**\n")
      end

  end

  client:close()
end

