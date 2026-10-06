# Decision Report

- generated_at: 2026-10-06T02:31:32.040858+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **16179**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.45% / filled 20/20。**
- 全期間 MARKET基準: n=16179, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.45%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.13% | **+1.07%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.81% | **+0.57%** |
| LIMIT_ATR | 12/20 | 60.0% | +0.82% | **+0.49%** |
| LIMIT_BB3S | 3/18 | 16.7% | +2.72% | **+0.45%** |
| MARKET | 20/20 | 100.0% | +0.45% | **+0.45%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 2/2 | 100.0% | +5.61% | **+5.61%** |
| LIMIT_5PCT_LONG | 12/20 | 60.0% | +1.86% | **+1.12%** |
| LIMIT_4PCT_LONG | 12/20 | 60.0% | +1.40% | **+0.84%** |
| LIMIT_6PCT_LONG | 10/20 | 50.0% | +0.39% | **+0.19%** |
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +0.38% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$120.15** / 初期 $100.00 (+20.15%)
- 確定トレード: 230件 (TP 82 / SL 141 / EXP 7)
- 最新: MOVR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.15
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,277.79** / 初期 $100.00 (+1177.79%)
- 確定: 6236件 (Win 1825 / Loss 1993 / Flat 2418) / skip 6504件
- 成長率目線: 平均log +0.000409 / 幾何平均 +0.041% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RLC/USDT:USDT `LIMIT_4PCT_LONG` SL_HIT account -0.50% 残高後 $1,277.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$274.46** / 初期 $100.00 (+174.46%)
- 確定: 3611件 (Win 1005 / Loss 845 / Flat 1761) / skip 5979件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0204 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RLC/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $274.46

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4337件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000114 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-06T02:31:18.525416+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.04% price=85589.8
- Funnel: target 1074 → liquid 166 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RLC/USDT:USDT | +26.69% | $19,456,858.42 |
| ORCA/USDT:USDT | +22.78% | $2,062,332.25 |
| BR/USDT:USDT | +9.04% | $15,924,534.46 |
| CHIP/USDT:USDT | +8.47% | $2,120,160.29 |
| RAY/USDT:USDT | +7.86% | $4,982,686.02 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +3.11% | +3.15% |
| ORCA/USDT:USDT | below_1h_threshold | +2.02% | +2.07% |
| VELVET/USDT:USDT | below_1h_threshold | +1.29% | +1.33% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.07% | +1.11% |
| ZRO/USDT:USDT | below_1h_threshold | +0.94% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
