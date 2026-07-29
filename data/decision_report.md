# Decision Report

- generated_at: 2026-07-29T16:41:37.768192+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9813**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9813, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.16% | **-1.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR | 11/20 | 55.0% | +2.12% | **+1.17%** |
| LIMIT_6PCT | 5/20 | 25.0% | +4.33% | **+1.08%** |
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_BB3S | 2/19 | 10.5% | +4.35% | **+0.46%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.30% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +2.04% | **+1.94%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +2.53% | **+1.90%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.80% | **+0.99%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +2.13% | **+0.96%** |
| LIMIT_5PCT_LONG | 6/20 | 30.0% | +2.28% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$119.27** / 初期 $100.00 (+19.27%)
- 確定トレード: 162件 (TP 63 / SL 94 / EXP 5)
- 最新: ON/USDT:USDT SL_HIT PnL -4.00% 残高後 $119.27
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$494.05** / 初期 $100.00 (+394.05%)
- 確定: 3519件 (Win 1113 / Loss 1147 / Flat 1259) / skip 2855件
- 成長率目線: 平均log +0.000454 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: JIMOTHY/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.50% 残高後 $494.05

## 4. Robust Adaptive DryRun ($100)

- 残高: **$138.42** / 初期 $100.00 (+38.42%)
- 確定: 1229件 (Win 340 / Loss 275 / Flat 614) / skip 1995件
- 成長率目線: 平均log +0.000265 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0091 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COTI/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $138.42

## 5. Causal Adaptive DryRun ($100)

- 残高: **$109.01** / 初期 $100.00 (+9.01%)
- 確定: 766件 (Win 246 / Loss 297 / Flat 223) / pending 0件 / skip 520件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000183 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $109.01

## 6. Latest Market Context

- 更新: 2026-07-29T16:41:25.589149+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.15% price=63842.7
- Funnel: target 911 → liquid 165 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 81.9 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| UAI/USDT:USDT | +7.35% | $8,088,600.05 |
| DIA/USDT:USDT | +6.49% | $1,080,502.59 |
| BEAT/USDT:USDT | +6.04% | $45,381,152.37 |
| KAITO/USDT:USDT | +4.60% | $9,406,636.04 |
| DEXE/USDT:USDT | +3.57% | $5,432,224.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| KAITO/USDT:USDT | below_1h_threshold | +4.40% | +4.55% |
| RE/USDT:USDT | below_1h_threshold | +3.71% | +3.86% |
| DEXE/USDT:USDT | below_1h_threshold | +3.65% | +3.81% |
| SOXS/USDT:USDT | below_1h_threshold | +3.17% | +3.32% |
| ON/USDT:USDT | below_1h_threshold | +2.40% | +2.56% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
