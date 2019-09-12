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

 Date: 12/09/2019 13:19:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for order_db
-- ----------------------------
DROP TABLE IF EXISTS `order_db`;
CREATE TABLE `order_db`  (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '数据项id',
  `order_type` int(11) NOT NULL COMMENT '订单类型，1 买入，2 售出',
  `wxid` text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '微信id',
  `create_time` int(11) NOT NULL COMMENT '创建时间',
  `order_status` int(11) NOT NULL COMMENT '订单状态, 1 进行中、2 完成、3 撤销',
  `stock_id` int(11) NOT NULL COMMENT '股票id',
  `order_num` int(11) NOT NULL COMMENT '数量',
  `price` int(11) NOT NULL COMMENT '价格',
  `match_id` int(11) NOT NULL COMMENT '比赛id',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
