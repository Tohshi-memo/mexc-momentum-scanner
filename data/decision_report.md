# Decision Report

- generated_at: 2026-11-28T03:36:29.973087+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19816**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19816, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +2.10% | **+0.84%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.78% | **+0.59%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.74% | **+0.56%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_6PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/5 | 60.0% | +3.67% | **+2.20%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.97% | **+0.92%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.82%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,955.30** / 初期 $100.00 (+1855.30%)
- 確定: 7650件 (Win 2201 / Loss 2462 / Flat 2987) / skip 8727件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account -0.30% 残高後 $1,955.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5297件 (Win 1410 / Loss 1141 / Flat 2746) / skip 7930件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0418 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7975件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000128 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T03:36:10.765011+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=59924.4
- Funnel: target 1101 → liquid 139 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +12.20% | $23,454,158.45 |
| SKY/USDT:USDT | +11.80% | $3,784,292.38 |
| ACE/USDT:USDT | +8.13% | $3,576,187.88 |
| BTW/USDT:USDT | +6.89% | $9,382,260.04 |
| SOXL/USDT:USDT | +4.78% | $843,489,092.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PIEVERSE/USDT:USDT | below_1h_threshold | +0.59% | +0.62% |
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +0.56% | +0.58% |
| SOXL/USDT:USDT | below_1h_threshold | +0.50% | +0.53% |
| NEAR/USDT:USDT | below_1h_threshold | +0.39% | +0.42% |
| PUMPFUN/USDT:USDT | below_1h_threshold | +0.38% | +0.41% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
