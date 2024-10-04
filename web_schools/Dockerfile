FROM node:22

ENV USER school
ENV PORT 5001

RUN adduser --disabled-password $USER

ENV YOUR_FLAG_HERE=sunctf{ea5h_pr0cess_ha5_1ts_oWn_PID}

WORKDIR /app

COPY src/package*.json ./

RUN npm install

COPY src/ .

USER $USER
EXPOSE $PORT

CMD ["node", "app.js"]