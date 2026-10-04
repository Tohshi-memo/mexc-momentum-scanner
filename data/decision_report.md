# Decision Report

- generated_at: 2026-10-04T21:51:30.467315+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16136**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=16136, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.85%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.85% | **-0.85%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +5.13% | **+1.54%** |
| LIMIT_BB3S | 3/9 | 33.3% | +4.00% | **+1.33%** |
| LIMIT_6PCT | 8/20 | 40.0% | +2.71% | **+1.08%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.92% | **+0.69%** |
| LIMIT_5PCT | 13/20 | 65.0% | +1.02% | **+0.66%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.93% | **+1.45%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.58% | **+1.34%** |
| MARKET_LONG | 20/20 | 100.0% | +1.12% | **+1.12%** |
| LIMIT_3PCT_LONG | 13/20 | 65.0% | +1.43% | **+0.93%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.27** / 初期 $100.00 (+20.27%)
- 確定トレード: 229件 (TP 82 / SL 140 / EXP 7)
- 最新: SI/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.27
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,303.95** / 初期 $100.00 (+1203.95%)
- 確定: 6195件 (Win 1822 / Loss 1986 / Flat 2387) / skip 6502件
- 成長率目線: 平均log +0.000415 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,303.95

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3609件 (Win 1005 / Loss 845 / Flat 1759) / skip 5938件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BATON/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4295件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000234 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-04T21:51:13.939046+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=85926.3
- Funnel: target 1076 → liquid 137 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.9 >= 65=1, 4h RSI 69.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BATON/USDT:USDT | +179.48% | $8,092,208.31 |
| HNT/USDT:USDT | +10.31% | $4,079,822.55 |
| FLOKI/USDT:USDT | +8.05% | $2,151,200.10 |
| VVV/USDT:USDT | +6.78% | $2,311,247.74 |
| SKY/USDT:USDT | +4.84% | $2,036,305.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| STRK/USDT:USDT | below_1h_threshold | +3.09% | +2.94% |
| SHIB/USDT:USDT | below_1h_threshold | +2.71% | +2.55% |
| WIF/USDT:USDT | below_1h_threshold | +2.35% | +2.19% |
| PENGU/USDT:USDT | below_1h_threshold | +1.81% | +1.65% |
| AKT/USDT:USDT | below_1h_threshold | +1.76% | +1.61% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
