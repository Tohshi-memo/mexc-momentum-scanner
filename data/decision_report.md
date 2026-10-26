# Decision Report

- generated_at: 2026-10-26T01:36:35.435822+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17449**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.46% / filled 20/20。**
- 全期間 MARKET基準: n=17449, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.46%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 3/20 | 15.0% | +6.57% | **+0.99%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.40% | **+0.48%** |
| MARKET | 20/20 | 100.0% | +0.46% | **+0.46%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.94% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 5/20 | 25.0% | +4.53% | **+1.13%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +1.17% | **+0.59%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.46% | **+0.36%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +0.55% | **+0.33%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +1.56% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$121.74** / 初期 $100.00 (+21.74%)
- 確定トレード: 251件 (TP 93 / SL 150 / EXP 8)
- 最新: CT/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.74
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,545.92** / 初期 $100.00 (+1445.92%)
- 確定: 6702件 (Win 1951 / Loss 2141 / Flat 2610) / skip 7308件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $1,545.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$314.96** / 初期 $100.00 (+214.96%)
- 確定: 3992件 (Win 1109 / Loss 945 / Flat 1938) / skip 6868件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0439 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $314.96

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5609件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000347 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T01:36:15.528401+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.26% price=79924.9
- Funnel: target 1070 → liquid 135 → pre 50 → checked 50 → surge 2 → strict 2
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| KIMCHI/USDT:USDT | +49.53% | $2,501,253.89 |
| BR/USDT:USDT | +12.37% | $7,041,393.55 |
| CLAUDIA/USDT:USDT | +11.42% | $1,000,969.47 |
| AXIS/USDT:USDT | +7.28% | $2,104,182.33 |
| CAP/USDT:USDT | +5.09% | $5,259,666.23 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CAP/USDT:USDT | below_1h_threshold | +2.32% | +2.58% |
| SOXS/USDT:USDT | below_1h_threshold | +2.15% | +2.42% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.72% |
| AGT/USDT:USDT | below_1h_threshold | +1.08% | +1.35% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +0.84% | +1.10% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
