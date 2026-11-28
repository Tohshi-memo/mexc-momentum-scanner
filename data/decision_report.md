# Decision Report

- generated_at: 2026-11-28T02:56:15.358552+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19813**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19813, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.39% | **+0.37%** |
| LIMIT_3PCT | 15/20 | 75.0% | -0.06% | **-0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +4.21% | **+2.81%** |
| LIMIT_6PCT_LONG | 8/20 | 40.0% | +2.06% | **+0.82%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.49% | **+0.47%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.92% | **+0.42%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +1.70% | **+0.25%** |

## 2. $100 Live Portfolio

- 残高: **$121.76** / 初期 $100.00 (+21.76%)
- 確定トレード: 292件 (TP 106 / SL 176 / EXP 10)
- 最新: SNXX/USDT:USDT EXPIRED PnL +2.62% 残高後 $121.76
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,955.30** / 初期 $100.00 (+1855.30%)
- 確定: 7650件 (Win 2201 / Loss 2462 / Flat 2987) / skip 8724件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +9.04%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ACE/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account -0.30% 残高後 $1,955.30

## 4. Robust Adaptive DryRun ($100)

- 残高: **$460.06** / 初期 $100.00 (+360.06%)
- 確定: 5297件 (Win 1410 / Loss 1141 / Flat 2746) / skip 7927件
- 成長率目線: 平均log +0.000288 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0084 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PORTAL/USDT:USDT `LIMIT_6PCT` SL_HIT account -0.35% 残高後 $460.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7971件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000030 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-28T02:56:02.577258+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=59968.5
- Funnel: target 1101 → liquid 142 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SKY/USDT:USDT | +12.37% | $3,780,949.79 |
| ACE/USDT:USDT | +10.35% | $3,499,587.31 |
| BTW/USDT:USDT | +6.62% | $9,244,610.83 |
| STX/USDT:USDT | +4.70% | $1,220,862.41 |
| SOXL/USDT:USDT | +4.15% | $869,799,307.95 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NVIDIA/USDT:USDT | below_1h_threshold | +0.45% | +0.77% |
| SEI/USDT:USDT | below_1h_threshold | +0.39% | +0.71% |
| KORU/USDT:USDT | below_1h_threshold | +0.35% | +0.66% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.35% | +0.66% |
| LTC/USDT:USDT | below_1h_threshold | +0.34% | +0.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
