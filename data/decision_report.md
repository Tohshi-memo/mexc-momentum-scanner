# Decision Report

- generated_at: 2026-10-26T21:51:22.044241+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17523**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.70% / filled 20/20。**
- 全期間 MARKET基準: n=17523, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 3/9 | 33.3% | +4.00% | **+1.33%** |
| LIMIT_7PCT | 9/20 | 45.0% | +2.85% | **+1.28%** |
| LIMIT_9PCT | 6/20 | 30.0% | +4.00% | **+1.20%** |
| LIMIT_8PCT | 7/20 | 35.0% | +2.86% | **+1.00%** |
| MARKET | 20/20 | 100.0% | +0.70% | **+0.70%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +2.19% | **+1.86%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.43% | **+1.35%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_BB3S_LONG | 6/11 | 54.5% | +1.62% | **+0.89%** |
| MARKET_LONG | 20/20 | 100.0% | +0.25% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7363件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$318.99** / 初期 $100.00 (+218.99%)
- 確定: 4052件 (Win 1116 / Loss 952 / Flat 1984) / skip 6882件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0647 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: KIMCHI/USDT:USDT `LIMIT_6PCT` SL_HIT account +0.15% 残高後 $318.99

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5687件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000298 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T21:51:10.687136+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.42% price=80181.8
- Funnel: target 1078 → liquid 159 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +144.35% | $14,996,447.21 |
| ARIA/USDT:USDT | +15.82% | $1,000,560.75 |
| KIMCHI/USDT:USDT | +5.98% | $4,381,030.06 |
| DNA/USDT:USDT | +4.30% | $1,196,141.51 |
| DODO/USDT:USDT | +3.96% | $1,442,088.55 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BTW/USDT:USDT | below_1h_threshold | +4.31% | +3.88% |
| BAT/USDT:USDT | below_1h_threshold | +2.38% | +1.96% |
| TIA/USDT:USDT | below_1h_threshold | +1.53% | +1.10% |
| SOXL/USDT:USDT | below_1h_threshold | +0.96% | +0.53% |
| INJ/USDT:USDT | below_1h_threshold | +0.92% | +0.49% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
