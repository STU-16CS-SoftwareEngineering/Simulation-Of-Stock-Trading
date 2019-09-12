/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 50645
 Source Host           : localhost:3306
 Source Schema         : market

 Target Server Type    : MySQL
 Target Server Version : 50645
 File Encoding         : 65001

 Date: 12/09/2019 13:19:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for storage_db
-- ----------------------------
DROP TABLE IF EXISTS `storage_db`;
CREATE TABLE `storage_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `match_id` int(11) NOT NULL COMMENT '比赛id',
  `stock_id` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '股票id',
  `own_num` int(11) NOT NULL COMMENT '持仓数量',
  `ave_price` double NOT NULL COMMENT '买入价格',
  `lock_num` int(11) NOT NULL COMMENT '冻结数量',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
