# Decision Report

- generated_at: 2026-10-30T04:41:20.050133+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17825**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17825, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.16%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 5/20 | 25.0% | +0.22% | **+0.05%** |
| LIMIT_4PCT | 12/20 | 60.0% | -0.14% | **-0.08%** |
| LIMIT_6PCT | 2/20 | 10.0% | -1.06% | **-0.11%** |
| MARKET | 20/20 | 100.0% | -0.16% | **-0.16%** |
| LIMIT_FIB1618 | 3/20 | 15.0% | -1.39% | **-0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.99% | **+0.75%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +1.76% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.59% | **+0.59%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.11% | **+0.51%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 256件 (TP 94 / SL 154 / EXP 8)
- 最新: BEAT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,523.56** / 初期 $100.00 (+1423.56%)
- 確定: 6805件 (Win 1975 / Loss 2181 / Flat 2649) / skip 7581件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `MARKET` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: EVAA/USDT:USDT `MARKET` SL_HIT account -0.50% 残高後 $1,523.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$363.77** / 初期 $100.00 (+263.77%)
- 確定: 4342件 (Win 1168 / Loss 980 / Flat 2194) / skip 6894件
- 成長率目線: 平均log +0.000297 / 幾何平均 +0.030% per trade / maxDD +4.13%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0002 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: Q/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $363.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5985件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000268 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-30T04:41:08.498097+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.12% price=78291.5
- Funnel: target 1086 → liquid 195 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| PARTI/USDT:USDT | +60.42% | $7,315,055.08 |
| Q/USDT:USDT | +43.00% | $24,383,788.76 |
| SOXS/USDT:USDT | +17.84% | $69,723,546.14 |
| BLESS/USDT:USDT | +11.17% | $14,266,167.01 |
| RUNE/USDT:USDT | +8.97% | $1,267,121.50 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PREDICT/USDT:USDT | below_1h_threshold | +2.60% | +2.48% |
| APR/USDT:USDT | below_1h_threshold | +1.83% | +1.72% |
| INIT/USDT:USDT | below_1h_threshold | +0.81% | +0.69% |
| JCT/USDT:USDT | below_1h_threshold | +0.56% | +0.44% |
| GOOGLSTOCK/USDT:USDT | below_1h_threshold | +0.42% | +0.30% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
