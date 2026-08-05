# Decision Report

- generated_at: 2026-08-05T00:56:20.650013+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10330**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.96% / filled 20/20。**
- 全期間 MARKET基準: n=10330, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 13/20 | 65.0% | +2.08% | **+1.35%** |
| MARKET | 20/20 | 100.0% | +0.96% | **+0.96%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.06% | **+0.96%** |
| LIMIT_2PCT | 14/20 | 70.0% | +1.23% | **+0.86%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.84% | **+0.74%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_4PCT_LONG | 15/20 | 75.0% | +1.50% | **+1.12%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.77% | **+1.06%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +0.97% | **+0.53%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +1.19% | **+0.48%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$577.81** / 初期 $100.00 (+477.81%)
- 確定: 3727件 (Win 1179 / Loss 1222 / Flat 1326) / skip 3164件
- 成長率目線: 平均log +0.000471 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $577.81

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2456件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0043 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.88** / 初期 $100.00 (+16.88%)
- 確定: 1086件 (Win 349 / Loss 423 / Flat 314) / pending 1件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000220 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $116.88

## 6. Latest Market Context

- 更新: 2026-08-05T00:56:13.480326+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.14% price=63984.9
- Funnel: target 937 → liquid 184 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +32.06% | $4,174,452.32 |
| CASHCAT/USDT:USDT | +28.19% | $1,133,306.69 |
| TAKE/USDT:USDT | +22.82% | $1,325,681.63 |
| MARSCOIN/USDT:USDT | +15.32% | $1,031,362.62 |
| BICO/USDT:USDT | +15.18% | $15,162,899.16 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNXX/USDT:USDT | below_1h_threshold | +3.45% | +3.59% |
| SYN/USDT:USDT | below_1h_threshold | +3.29% | +3.43% |
| SKYAI/USDT:USDT | below_1h_threshold | +2.90% | +3.04% |
| DEXE/USDT:USDT | below_1h_threshold | +2.62% | +2.76% |
| NIL/USDT:USDT | below_1h_threshold | +2.13% | +2.27% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
