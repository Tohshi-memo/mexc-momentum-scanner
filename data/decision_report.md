# Decision Report

- generated_at: 2026-11-12T02:51:28.670697+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18715**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +3.99% / filled 20/20。**
- 全期間 MARKET基準: n=18715, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+3.99%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.99% | **+3.99%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +3.99% | **+3.99%** |
| LIMIT_1PCT | 13/20 | 65.0% | +2.49% | **+1.62%** |
| LIMIT_ATR | 11/20 | 55.0% | +2.60% | **+1.43%** |
| LIMIT_2PCT | 11/20 | 55.0% | +2.38% | **+1.31%** |
| LIMIT_3PCT | 8/20 | 40.0% | +0.89% | **+0.36%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_FIB1618_LONG | 8/20 | 40.0% | +0.18% | **+0.07%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.40% | **-0.20%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | -1.23% | **-0.67%** |

## 2. $100 Live Portfolio

- 残高: **$121.25** / 初期 $100.00 (+21.25%)
- 確定トレード: 273件 (TP 99 / SL 166 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.25
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,708.40** / 初期 $100.00 (+1608.40%)
- 確定: 7233件 (Win 2083 / Loss 2316 / Flat 2834) / skip 8043件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_FIB1272` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SNXX/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,708.40

## 4. Robust Adaptive DryRun ($100)

- 残高: **$390.28** / 初期 $100.00 (+290.28%)
- 確定: 4779件 (Win 1283 / Loss 1057 / Flat 2439) / skip 7347件
- 成長率目線: 平均log +0.000285 / 幾何平均 +0.028% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0302 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AGT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $390.28

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6875件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000085 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-12T02:51:12.374165+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.27% price=73885.5
- Funnel: target 1103 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| IDOL/USDT:USDT | +31.03% | $2,938,610.74 |
| Q/USDT:USDT | +6.81% | $4,111,520.26 |
| SOXS/USDT:USDT | +6.48% | $59,053,385.13 |
| SQQQ/USDT:USDT | +2.70% | $2,286,952.66 |
| AMDSTOCK/USDT:USDT | +2.24% | $21,732,074.85 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DELTAELECSTOCK/USDT:USDT | below_1h_threshold | +1.98% | +1.71% |
| CBRSSTOCK/USDT:USDT | below_1h_threshold | +1.19% | +0.92% |
| AVAX/USDT:USDT | below_1h_threshold | +1.06% | +0.78% |
| OPENAI/USDT:USDT | below_1h_threshold | +0.93% | +0.66% |
| NIGHT/USDT:USDT | below_1h_threshold | +0.89% | +0.62% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
