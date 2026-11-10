# Decision Report

- generated_at: 2026-11-10T09:56:31.934860+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18591**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18591, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.60% | **-0.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 9/20 | 45.0% | +1.82% | **+0.82%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.89% | **+0.75%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.32% | **+0.23%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.86% | **+1.40%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.49% | **+1.37%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +1.59% | **+0.95%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.71% | **+0.94%** |
| MARKET_LONG | 20/20 | 100.0% | +0.69% | **+0.69%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,673.70** / 初期 $100.00 (+1573.70%)
- 確定: 7188件 (Win 2067 / Loss 2294 / Flat 2827) / skip 7964件
- 成長率目線: 平均log +0.000392 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: AIN/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,673.70

## 4. Robust Adaptive DryRun ($100)

- 残高: **$389.88** / 初期 $100.00 (+289.88%)
- 確定: 4759件 (Win 1278 / Loss 1048 / Flat 2433) / skip 7243件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0885 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $389.88

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6751件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000404 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T09:56:14.018224+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=74444.8
- Funnel: target 1094 → liquid 150 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +61.80% | $13,339,547.99 |
| ONE/USDT:USDT | +24.02% | $6,091,594.69 |
| NIUBI/USDT:USDT | +11.45% | $2,338,730.13 |
| AIN/USDT:USDT | +10.85% | $2,744,712.44 |
| ARIA/USDT:USDT | +10.61% | $1,301,432.73 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SOXL/USDT:USDT | below_1h_threshold | +2.85% | +3.19% |
| MUU/USDT:USDT | below_1h_threshold | +1.43% | +1.77% |
| SNXX/USDT:USDT | below_1h_threshold | +1.09% | +1.43% |
| KORU/USDT:USDT | below_1h_threshold | +1.04% | +1.39% |
| AMDSTOCK/USDT:USDT | below_1h_threshold | +0.89% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
