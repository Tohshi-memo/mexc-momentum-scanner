# Decision Report

- generated_at: 2026-06-13T23:08:16.088392+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6617**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6617, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.29% | **+0.29%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.07% | **+0.27%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_6PCT_LONG | 12/20 | 60.0% | +1.62% | **+0.97%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.23% | **+0.92%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$167.72** / 初期 $100.00 (+67.72%)
- 確定: 1490件 (Win 401 / Loss 476 / Flat 613) / skip 1688件
- 成長率目線: 平均log +0.000347 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $167.72

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.99** / 初期 $100.00 (-1.01%)
- 確定: 28件 (Win 10 / Loss 10 / Flat 8) / skip 0件
- 成長率目線: 平均log -0.000363 / 幾何平均 -0.036% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0240 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.99

## 5. Latest Market Context

- 更新: 2026-06-13T23:08:11.829214+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.01% price=64419.5
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +28.12% | $1,770,363.79 |
| RIF/USDT:USDT | +24.39% | $12,128,801.56 |
| MEGA/USDT:USDT | +15.90% | $2,651,201.68 |
| H/USDT:USDT | +12.59% | $15,622,834.59 |
| BILL/USDT:USDT | +7.65% | $2,121,177.17 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TAO/USDT:USDT | below_1h_threshold | +1.27% | +1.26% |
| RIF/USDT:USDT | below_1h_threshold | +1.15% | +1.14% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +0.72% | +0.72% |
| BSB/USDT:USDT | below_1h_threshold | +0.65% | +0.64% |
| AR/USDT:USDT | below_1h_threshold | +0.49% | +0.48% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
