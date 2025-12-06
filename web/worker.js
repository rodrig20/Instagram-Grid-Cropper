self.onmessage = async e => {
  const {width, height, file, cols, cellWidth, cellHeight, marginHorizontal, cropPixels, rows} = e.data;

  // Carrega a imagem como bitmap
  const bitmap = await createImageBitmap(file);

  // Se rows não for fornecido, calcular baseado na altura
  const calculatedRows = rows ? Math.floor(rows) : Math.floor(height / cellHeight);

  for (let r = 0; r < calculatedRows; r++) {
    const startY = height - cellHeight * (calculatedRows - r);
    const safeStartY = Math.max(0, startY);

    for (let i = 0; i < cols; i++) {
      const startX = i === 0 ? 0 : i * cellWidth - i * marginHorizontal;
      const endX = startX + cellWidth;
      const sx = Math.max(0, startX);
      let sw = Math.min(cellWidth, Math.max(0, width - sx));

      let sxCrop = sx + cropPixels;
      let swCrop = sw - 2 * cropPixels;
      if (swCrop < 0) { sxCrop = sx; swCrop = sw; }

      // Canvas para thumb
      const tcanvas = new OffscreenCanvas(swCrop, cellHeight);
      tcanvas.getContext('2d').drawImage(bitmap, sxCrop, safeStartY, swCrop, cellHeight, 0, 0, swCrop, cellHeight);
      const thumbBase64 = tcanvas.convertToBlob({type:'image/png'}).then(blob => {
        return new Promise(res => {
          const reader = new FileReader();
          reader.onload = () => res(reader.result);
          reader.readAsDataURL(blob);
        });
      });

      // Canvas para full
      const fcanvas = new OffscreenCanvas(sw, cellHeight);
      fcanvas.getContext('2d').drawImage(bitmap, sx, safeStartY, sw, cellHeight, 0, 0, sw, cellHeight);
      const fullBase64 = fcanvas.convertToBlob({type:'image/png'}).then(blob => {
        return new Promise(res => {
          const reader = new FileReader();
          reader.onload = () => res(reader.result);
          reader.readAsDataURL(blob);
        });
      });

      // Espera os dois base64
      const [t, f] = await Promise.all([thumbBase64, fullBase64]);

      self.postMessage({type:'subimage', thumbBase64: t, fullBase64: f, row: calculatedRows - r, col: i + 1});
    }
  }

  self.postMessage({type:'done'});
};
