# Decision Report

- generated_at: 2026-10-26T21:01:26.452070+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17521**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.25% / filled 20/20。**
- 全期間 MARKET基準: n=17521, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.25%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 7/20 | 35.0% | +3.83% | **+1.34%** |
| LIMIT_BB3S | 3/9 | 33.3% | +4.00% | **+1.33%** |
| MARKET | 20/20 | 100.0% | +1.25% | **+1.25%** |
| LIMIT_9PCT | 4/20 | 20.0% | +5.00% | **+1.00%** |
| LIMIT_8PCT | 5/20 | 25.0% | +3.20% | **+0.80%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +1.52% | **+1.29%** |
| LIMIT_3PCT_LONG | 15/20 | 75.0% | +0.85% | **+0.64%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +0.67% | **+0.63%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.61% | **+0.24%** |
| MARKET_LONG | 20/20 | 100.0% | +0.08% | **+0.08%** |

## 2. $100 Live Portfolio

- 残高: **$121.62** / 初期 $100.00 (+21.62%)
- 確定トレード: 252件 (TP 93 / SL 151 / EXP 8)
- 最新: Q/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.62
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,526.92** / 初期 $100.00 (+1426.92%)
- 確定: 6721件 (Win 1956 / Loss 2152 / Flat 2613) / skip 7361件
- 成長率目線: 平均log +0.000406 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: Q/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,526.92

## 4. Robust Adaptive DryRun ($100)

- 残高: **$319.62** / 初期 $100.00 (+219.62%)
- 確定: 4050件 (Win 1115 / Loss 951 / Flat 1984) / skip 6882件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.13%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0532 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $319.62

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5685件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-26T21:01:13.660217+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=79906.1
- Funnel: target 1078 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| Q/USDT:USDT | +142.93% | $12,767,776.58 |
| AGT/USDT:USDT | +5.73% | $1,657,880.19 |
| DNA/USDT:USDT | +5.51% | $1,148,069.55 |
| AXIS/USDT:USDT | +4.76% | $1,479,283.41 |
| DOOD/USDT:USDT | +4.01% | $3,978,122.10 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AXIS/USDT:USDT | below_1h_threshold | +1.30% | +1.22% |
| SOXL/USDT:USDT | below_1h_threshold | +0.96% | +0.88% |
| AAOISTOCK/USDT:USDT | below_1h_threshold | +0.76% | +0.69% |
| KORU/USDT:USDT | below_1h_threshold | +0.73% | +0.65% |
| SAMSUNGSTOCK/USDT:USDT | below_1h_threshold | +0.72% | +0.64% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
