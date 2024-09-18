FROM node:22

ENV USER school
ENV PORT 5001

RUN adduser --disabled-password $USER

ENV FLAG=sunctf{ea5h_pr0cess_ha5_th3iR_oWn_PID}

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

USER $USER
EXPOSE $PORT

CMD ["node", "app.js"]