# Decision Report

- generated_at: 2026-08-05T01:36:29.623126+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **10335**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=10335, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.21%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.21% | **-0.21%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +4.78% | **+0.96%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.59% | **+0.69%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.80% | **+0.56%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.47% | **+0.30%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +1.63% | **+0.81%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.71% | **+0.77%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.79% | **+0.63%** |
| LIMIT_4PCT_LONG | 11/20 | 55.0% | +1.14% | **+0.63%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +1.52% | **+0.53%** |

## 2. $100 Live Portfolio

- 残高: **$121.17** / 初期 $100.00 (+21.17%)
- 確定トレード: 174件 (TP 67 / SL 102 / EXP 5)
- 最新: SKHYSTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.17
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$576.27** / 初期 $100.00 (+476.27%)
- 確定: 3732件 (Win 1180 / Loss 1223 / Flat 1329) / skip 3164件
- 成長率目線: 平均log +0.000469 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $576.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$139.82** / 初期 $100.00 (+39.82%)
- 確定: 1285件 (Win 359 / Loss 299 / Flat 627) / skip 2461件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0666 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SKYAI/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $139.82

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.18** / 初期 $100.00 (+17.18%)
- 確定: 1091件 (Win 350 / Loss 423 / Flat 318) / pending 5件 / skip 714件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000284 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.18

## 6. Latest Market Context

- 更新: 2026-08-05T01:36:17.976857+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=64129.9
- Funnel: target 937 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 84.6 >= 65=1, 4h RSI 91.6 >= 65=1, 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEI/USDT:USDT | +52.47% | $4,793,130.62 |
| MARSCOIN/USDT:USDT | +31.20% | $1,062,516.86 |
| CASHCAT/USDT:USDT | +28.74% | $1,136,112.83 |
| TAKE/USDT:USDT | +28.01% | $1,352,971.29 |
| SKYAI/USDT:USDT | +23.72% | $49,106,439.11 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ADVANTESTSTOCK/USDT:USDT | below_1h_threshold | +4.83% | +4.58% |
| TAKE/USDT:USDT | below_1h_threshold | +4.79% | +4.54% |
| CASHCAT/USDT:USDT | below_1h_threshold | +4.17% | +3.93% |
| ALABSTOCK/USDT:USDT | below_1h_threshold | +3.41% | +3.16% |
| COTI/USDT:USDT | below_1h_threshold | +3.17% | +2.92% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
