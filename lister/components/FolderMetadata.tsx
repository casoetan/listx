import { HTMLAttributes, useEffect, useState } from "react";

interface FolderMetadataProps extends HTMLAttributes<HTMLDivElement> { 
  folderList: any[]
}

const FolderMetadata = ({ folderList }: FolderMetadataProps) => {
  const [totalSize, setTotalSize] = useState(0);
  useEffect(() => {
    setTotalSize(folderList.reduce((acc, folder) => acc + folder.size, 0));
  }, [folderList])

  return (
    <div>
      {folderList.length ? <span>Total Size: <b>{totalSize} KB</b> Count: <b>{folderList.length}</b></span> : ''}
    </div>
  );
}

export default FolderMetadata;
