# Decision Report

- generated_at: 2026-11-03T20:46:57.748751+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18096**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18096, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.81%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.81% | **-0.81%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 3/20 | 15.0% | +3.15% | **+0.47%** |
| LIMIT_9PCT | 3/20 | 15.0% | +2.86% | **+0.43%** |
| LIMIT_8PCT | 3/20 | 15.0% | +2.57% | **+0.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +0.70% | **+0.14%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.16% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +3.11% | **+2.48%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.07% | **+1.97%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.94% | **+1.36%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +2.40% | **+1.32%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.94% | **+1.26%** |

## 2. $100 Live Portfolio

- 残高: **$121.61** / 初期 $100.00 (+21.61%)
- 確定トレード: 261件 (TP 96 / SL 157 / EXP 8)
- 最新: IDOL/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.61
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,500.44** / 初期 $100.00 (+1400.44%)
- 確定: 6921件 (Win 2001 / Loss 2219 / Flat 2701) / skip 7736件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ICNT/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $1,500.44

## 4. Robust Adaptive DryRun ($100)

- 残高: **$381.36** / 初期 $100.00 (+281.36%)
- 確定: 4511件 (Win 1208 / Loss 1003 / Flat 2300) / skip 6996件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0640 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LYN/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $381.36

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6255件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-03T20:46:48.464706+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=77777.2
- Funnel: target 1084 → liquid 156 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| LYN/USDT:USDT | +19.45% | $1,472,000.24 |
| BEAT/USDT:USDT | +8.64% | $9,563,840.23 |
| IDOL/USDT:USDT | +4.76% | $13,825,789.04 |
| ARIA/USDT:USDT | +4.51% | $2,359,256.36 |
| AIN/USDT:USDT | +4.20% | $3,479,999.71 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +3.94% | +3.69% |
| LYN/USDT:USDT | below_1h_threshold | +3.36% | +3.11% |
| SOXS/USDT:USDT | below_1h_threshold | +2.44% | +2.19% |
| IDOL/USDT:USDT | below_1h_threshold | +2.18% | +1.94% |
| RUNE/USDT:USDT | below_1h_threshold | +1.79% | +1.55% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
