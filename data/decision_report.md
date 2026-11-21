# Decision Report

- generated_at: 2026-11-21T16:11:27.980301+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19317**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.80% / filled 20/20。**
- 全期間 MARKET基準: n=19317, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.80%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.53% | **+2.41%** |
| LIMIT_2PCT | 17/20 | 85.0% | +2.49% | **+2.11%** |
| LIMIT_3PCT | 16/20 | 80.0% | +1.83% | **+1.46%** |
| MARKET | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_BB3S | 8/17 | 47.1% | +1.55% | **+0.73%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +3.34% | **+2.00%** |
| LIMIT_7PCT_LONG | 11/20 | 55.0% | +3.61% | **+1.98%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +3.14% | **+1.88%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +3.23% | **+1.77%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +2.77% | **+1.66%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,703.43** / 初期 $100.00 (+1603.43%)
- 確定: 7460件 (Win 2141 / Loss 2401 / Flat 2918) / skip 8418件
- 成長率目線: 平均log +0.000380 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DCTY/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $1,703.43

## 4. Robust Adaptive DryRun ($100)

- 残高: **$449.80** / 初期 $100.00 (+349.80%)
- 確定: 5122件 (Win 1363 / Loss 1099 / Flat 2660) / skip 7606件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score +0.0183 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DCTY/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $449.80

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7477件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000194 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T16:11:18.034742+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=59870.4
- Funnel: target 1086 → liquid 141 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AKE/USDT:USDT | +3.02% | $12,868,976.31 |
| BARD/USDT:USDT | +1.96% | $3,912,296.43 |
| IDOL/USDT:USDT | +1.38% | $1,753,596.55 |
| IRYS/USDT:USDT | +1.01% | $2,579,486.67 |
| SOXL/USDT:USDT | +0.95% | $1,086,376,125.93 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AKE/USDT:USDT | below_1h_threshold | +3.02% | +3.09% |
| BARD/USDT:USDT | below_1h_threshold | +1.64% | +1.70% |
| IDOL/USDT:USDT | below_1h_threshold | +1.39% | +1.46% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.03% | +1.10% |
| IRYS/USDT:USDT | below_1h_threshold | +1.01% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
