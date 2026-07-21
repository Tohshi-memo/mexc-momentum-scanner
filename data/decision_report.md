# Decision Report

- generated_at: 2026-07-21T08:06:12.658574+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9162**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9162, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.98% | **+0.50%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.02% | **+0.36%** |
| LIMIT_BB3S | 6/14 | 42.9% | +0.63% | **+0.27%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.11% | **+0.11%** |
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.79% | **+1.52%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.74% | **+0.48%** |
| LIMIT_8PCT_LONG | 6/20 | 30.0% | +1.33% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$107.51** / 初期 $100.00 (+7.51%)
- 確定トレード: 126件 (TP 44 / SL 77 / EXP 5)
- 最新: US/USDT:USDT SL_HIT PnL -4.00% 残高後 $107.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$424.67** / 初期 $100.00 (+324.67%)
- 確定: 3224件 (Win 1013 / Loss 1027 / Flat 1184) / skip 2499件
- 成長率目線: 平均log +0.000449 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $424.67

## 4. Robust Adaptive DryRun ($100)

- 残高: **$131.97** / 初期 $100.00 (+31.97%)
- 確定: 1123件 (Win 299 / Loss 235 / Flat 589) / skip 1450件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0869 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $131.97

## 5. Causal Adaptive DryRun ($100)

- 残高: **$100.91** / 初期 $100.00 (+0.91%)
- 確定: 341件 (Win 120 / Loss 152 / Flat 69) / pending 0件 / skip 294件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000221 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: 1000BONK/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $100.91

## 6. Latest Market Context

- 更新: 2026-07-21T08:06:06.114815+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.09% price=66228.6
- Funnel: target 885 → liquid 168 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +115.35% | $4,085,496.21 |
| ERA/USDT:USDT | +53.65% | $6,236,339.20 |
| ZHIPUSTOCK/USDT:USDT | +35.65% | $2,879,586.35 |
| ONDO/USDT:USDT | +10.79% | $35,304,399.58 |
| LDO/USDT:USDT | +10.25% | $9,517,063.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZHIPUSTOCK/USDT:USDT | below_1h_threshold | +2.75% | +2.65% |
| USELESS/USDT:USDT | below_1h_threshold | +1.09% | +0.99% |
| US/USDT:USDT | below_1h_threshold | +0.61% | +0.52% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +0.45% | +0.35% |
| KORU/USDT:USDT | below_1h_threshold | +0.40% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
