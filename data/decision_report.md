# Decision Report

- generated_at: 2026-08-31T09:56:23.851779+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13159**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.63% / filled 20/20。**
- 全期間 MARKET基準: n=13159, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+2.63%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.63% | **+2.63%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.63% | **+2.63%** |
| LIMIT_1PCT | 16/20 | 80.0% | +2.18% | **+1.74%** |
| LIMIT_BB3S | 5/14 | 35.7% | +2.31% | **+0.82%** |
| LIMIT_4PCT | 9/20 | 45.0% | +1.61% | **+0.72%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.96% | **+0.69%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | +0.80% | **+0.40%** |
| LIMIT_7PCT_LONG | 12/20 | 60.0% | +0.22% | **+0.13%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | -0.08% | **-0.02%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$796.73** / 初期 $100.00 (+696.73%)
- 確定: 4875件 (Win 1485 / Loss 1608 / Flat 1782) / skip 4845件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_5PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: FONE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $796.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.14** / 初期 $100.00 (+73.14%)
- 確定: 2167件 (Win 601 / Loss 528 / Flat 1038) / skip 4403件
- 成長率目線: 平均log +0.000253 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.14

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.89** / 初期 $100.00 (+15.89%)
- 確定: 2084件 (Win 610 / Loss 812 / Flat 662) / pending 0件 / skip 2548件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000159 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ZORA/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $115.89

## 6. Latest Market Context

- 更新: 2026-08-31T09:56:16.210048+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=78510.0
- Funnel: target 1028 → liquid 155 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HEMI/USDT:USDT | +47.46% | $7,288,664.32 |
| SKR/USDT:USDT | +44.21% | $46,738,962.26 |
| BASECAT/USDT:USDT | +42.93% | $1,836,795.92 |
| ZORA/USDT:USDT | +31.27% | $12,318,692.84 |
| CYS/USDT:USDT | +28.63% | $6,269,520.29 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PONS/USDT:USDT | below_1h_threshold | +4.21% | +4.12% |
| BASECAT/USDT:USDT | below_1h_threshold | +3.75% | +3.66% |
| 1000BONK/USDT:USDT | below_1h_threshold | +3.41% | +3.32% |
| XMR/USDT:USDT | below_1h_threshold | +2.44% | +2.35% |
| NOT/USDT:USDT | below_1h_threshold | +2.43% | +2.34% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
