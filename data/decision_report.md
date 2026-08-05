# Decision Report

- generated_at: 2026-08-05T01:31:41.698963+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10333**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.29% / filled 20/20。**
- 全期間 MARKET基準: n=10333, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.29%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.29% | **+0.29%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 7/20 | 35.0% | +2.46% | **+0.86%** |
| LIMIT_8PCT | 3/20 | 15.0% | +5.14% | **+0.77%** |
| LIMIT_ATR | 13/20 | 65.0% | +1.15% | **+0.75%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.72% | **+0.69%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.94% | **+1.16%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.42% | **+0.92%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.53% | **+0.77%** |
| LIMIT_2PCT_LONG | 18/20 | 90.0% | +0.82% | **+0.73%** |
| LIMIT_3PCT_LONG | 16/20 | 80.0% | +0.84% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$574.92** / 初期 $100.00 (+474.92%)
- 確定: 3730件 (Win 1179 / Loss 1223 / Flat 1328) / skip 3164件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $574.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2459件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score -0.0257 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.18** / 初期 $100.00 (+17.18%)
- 確定: 1089件 (Win 350 / Loss 423 / Flat 316) / pending 5件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000240 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.18

## 6. Latest Market Context

- 更新: 2026-08-05T01:31:31.029103+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.22% price=64112.5
- Funnel: target 937 → liquid 179 → pre 50 → checked 50 → surge 4 → strict 0
- Surge前reject: below_1h_threshold=46, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 91.7 >= 65=1, 4h RSI 73.4 >= 65=1, 4h RSI 82.7 >= 65=1, 4h RSI 75.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +52.26% | $4,751,340.62 |
| CASHCAT/USDT:USDT | +30.79% | $1,130,349.99 |
| MARSCOIN/USDT:USDT | +29.99% | $1,054,210.51 |
| TAKE/USDT:USDT | +27.33% | $1,350,146.81 |
| HFT/USDT:USDT | +16.58% | $1,439,664.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ADVANTESTSTOCK/USDT:USDT | below_1h_threshold | +4.83% | +4.61% |
| TAKE/USDT:USDT | below_1h_threshold | +3.83% | +3.61% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +3.41% | +3.19% |
| HFT/USDT:USDT | below_1h_threshold | +3.28% | +3.06% |
| DEXE/USDT:USDT | below_1h_threshold | +3.06% | +2.84% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
