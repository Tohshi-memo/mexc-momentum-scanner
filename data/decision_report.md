# Decision Report

- generated_at: 2026-09-28T16:36:43.155376+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15738**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.74% / filled 20/20。**
- 全期間 MARKET基準: n=15738, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=+0.74%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.74% | **+0.74%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 5/17 | 29.4% | +4.49% | **+1.32%** |
| LIMIT_1PCT | 18/20 | 90.0% | +1.45% | **+1.31%** |
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +3.02% | **+1.06%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.72% | **+0.36%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | -0.04% | **-0.02%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | -0.60% | **-0.09%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | -0.17% | **-0.10%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,227.24** / 初期 $100.00 (+1127.24%)
- 確定: 5983件 (Win 1766 / Loss 1925 / Flat 2292) / skip 6316件
- 成長率目線: 平均log +0.000419 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` SL_HIT account -0.50% 残高後 $1,227.24

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5615件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$118.20** / 初期 $100.00 (+18.20%)
- 確定: 3302件 (Win 957 / Loss 1298 / Flat 1047) / pending 5件 / skip 3905件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000142 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: HBAR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $118.20

## 6. Latest Market Context

- 更新: 2026-09-28T16:36:24.525951+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.69% price=83914.7
- Funnel: target 1066 → liquid 173 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.9 >= 65=1, 4h RSI 67.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MARSCOIN/USDT:USDT | +10.12% | $3,462,995.16 |
| QNT/USDT:USDT | +6.26% | $333,460,325.67 |
| GRASS/USDT:USDT | +5.89% | $6,002,831.57 |
| PUMPFUN/USDT:USDT | +5.37% | $68,859,869.47 |
| LINK/USDT:USDT | +5.16% | $105,113,931.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUMPFUN/USDT:USDT | below_relative_strength | +5.18% | +4.49% |
| LINK/USDT:USDT | below_1h_threshold | +5.00% | +4.31% |
| AZTEC/USDT:USDT | below_1h_threshold | +4.61% | +3.92% |
| VIRTUAL/USDT:USDT | below_1h_threshold | +3.68% | +2.99% |
| SEI/USDT:USDT | below_1h_threshold | +2.82% | +2.13% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
