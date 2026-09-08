# Decision Report

- generated_at: 2026-09-08T20:26:14.674576+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **14018**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.25% / filled 20/20。**
- 全期間 MARKET基準: n=14018, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 6/20 | 30.0% | +1.00% | **+0.30%** |
| MARKET | 20/20 | 100.0% | +0.25% | **+0.25%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.29% | **+0.22%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_4PCT | 13/20 | 65.0% | +0.08% | **+0.05%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.15% | **+1.15%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.98% | **+0.69%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | +0.51% | **+0.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,012.19** / 初期 $100.00 (+912.19%)
- 確定: 5282件 (Win 1587 / Loss 1707 / Flat 1988) / skip 5297件
- 成長率目線: 平均log +0.000438 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,012.19

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.50** / 初期 $100.00 (+90.50%)
- 確定: 2621件 (Win 725 / Loss 622 / Flat 1274) / skip 4808件
- 成長率目線: 平均log +0.000246 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0156 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $190.50

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.91** / 初期 $100.00 (+19.91%)
- 確定: 2601件 (Win 762 / Loss 987 / Flat 852) / pending 5件 / skip 2884件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $119.91

## 6. Latest Market Context

- 更新: 2026-09-08T20:26:06.914398+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=78469.9
- Funnel: target 1070 → liquid 161 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARX/USDT:USDT | +8.16% | $1,040,134.74 |
| DOT/USDT:USDT | +5.93% | $33,170,952.12 |
| BNCSTOCK/USDT:USDT | +5.33% | $2,597,259.70 |
| BONER/USDT:USDT | +4.94% | $1,972,626.24 |
| DOGS/USDT:USDT | +4.74% | $2,631,269.36 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| DOGS/USDT:USDT | below_1h_threshold | +2.34% | +2.26% |
| DOT/USDT:USDT | below_1h_threshold | +1.96% | +1.88% |
| RAY/USDT:USDT | below_1h_threshold | +1.79% | +1.71% |
| SOLV/USDT:USDT | below_1h_threshold | +1.76% | +1.68% |
| CP/USDT:USDT | below_1h_threshold | +1.71% | +1.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
