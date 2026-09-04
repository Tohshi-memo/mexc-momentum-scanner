# Decision Report

- generated_at: 2026-09-04T03:01:23.168452+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13572**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +2.16% / filled 20/20。**
- 全期間 MARKET基準: n=13572, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=+2.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +2.28% | **+2.16%** |
| MARKET | 20/20 | 100.0% | +2.16% | **+2.16%** |
| LIMIT_2PCT | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_BB3S | 4/19 | 21.1% | +4.67% | **+0.98%** |
| LIMIT_3PCT | 11/20 | 55.0% | +1.48% | **+0.81%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +2.22% | **+0.33%** |
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +1.10% | **+0.27%** |
| LIMIT_8PCT_LONG | 9/20 | 45.0% | +0.00% | **+0.00%** |
| LIMIT_FIB1618_LONG | 2/20 | 10.0% | -0.29% | **-0.03%** |
| LIMIT_1PCT_LONG | 19/20 | 95.0% | -0.08% | **-0.08%** |

## 2. $100 Live Portfolio

- 残高: **$120.68** / 初期 $100.00 (+20.68%)
- 確定トレード: 199件 (TP 74 / SL 120 / EXP 5)
- 最新: MARSCOIN/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.68
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$859.66** / 初期 $100.00 (+759.66%)
- 確定: 5009件 (Win 1516 / Loss 1644 / Flat 1849) / skip 5124件
- 成長率目線: 平均log +0.000429 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $859.66

## 4. Robust Adaptive DryRun ($100)

- 残高: **$185.25** / 初期 $100.00 (+85.25%)
- 確定: 2388件 (Win 676 / Loss 576 / Flat 1136) / skip 4595件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0899 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $185.25

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.71** / 初期 $100.00 (+16.71%)
- 確定: 2228件 (Win 664 / Loss 874 / Flat 690) / pending 3件 / skip 2814件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000185 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: ARB/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $116.71

## 6. Latest Market Context

- 更新: 2026-09-04T03:01:13.295296+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=80830.5
- Funnel: target 1046 → liquid 164 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +32.03% | $10,526,054.44 |
| BASECAT/USDT:USDT | +16.32% | $1,972,406.53 |
| PONS/USDT:USDT | +15.84% | $9,368,861.88 |
| MARSCOIN/USDT:USDT | +15.72% | $10,007,419.84 |
| USELESS/USDT:USDT | +11.47% | $28,769,778.27 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KORU/USDT:USDT | below_1h_threshold | +1.18% | +1.15% |
| MUU/USDT:USDT | below_1h_threshold | +0.78% | +0.74% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +0.69% | +0.65% |
| SOXL/USDT:USDT | below_1h_threshold | +0.65% | +0.61% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.57% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
