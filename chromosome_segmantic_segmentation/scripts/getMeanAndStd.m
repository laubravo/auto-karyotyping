%% get mean by channel
%  organized as B,G,R

base_dir='/media/SSD2/cariotipos/classification-net/classificationDB/train';
%save_dir = '/home/labravo/semanticContours/data/FLC2017_resized';

nB = 0;

total_pix = 0;

pixList = [];

for i = 1:23
objects = dir(fullfile(base_dir, num2str(i),'*.bmp'));

for j = 1:length(objects)

im = imread(fullfile(base_dir, num2str(i), objects(j).name));
disp(['Size: ', num2str(size(im,1)), ' ', num2str(size(im,2))])
[fil,col] = size(im);
total_pix = total_pix + fil*col;

nB = nB + sum(im(:));

pixList = cat(1,pixList,im(:)); 

disp(['done im', objects(j).name])
end
end
mB = nB/total_pix;

sB = std(double(pixList))

disp(['Mean: ',num2str(mB),' std: ', num2str(sB)])

%fileID = fopen(fullfile(save_dir,'channel_means.txt'),'w');
%fprintf(fileID,'channel means\n');
%fprintf(fileID,'mean Blue = %s\n',num2str(mB));
%fclose(fileID);
%disp('done writing .txt')
