# Decision Report

- generated_at: 2026-10-01T10:21:30.591928+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15889**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15889, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.19%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.19% | **-2.19%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1272 | 4/20 | 20.0% | +0.11% | **+0.02%** |
| LIMIT_BB3S | 2/13 | 15.4% | -3.23% | **-0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +4.01% | **+2.86%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +3.13% | **+2.81%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +3.40% | **+2.38%** |
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_3PCT_LONG | 8/20 | 40.0% | +3.13% | **+1.25%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,297.53** / 初期 $100.00 (+1197.53%)
- 確定: 6008件 (Win 1779 / Loss 1931 / Flat 2298) / skip 6442件
- 成長率目線: 平均log +0.000427 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,297.53

## 4. Robust Adaptive DryRun ($100)

- 残高: **$268.77** / 初期 $100.00 (+168.77%)
- 確定: 3542件 (Win 979 / Loss 812 / Flat 1751) / skip 5758件
- 成長率目線: 平均log +0.000279 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1470 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CT/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $268.77

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4050件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000324 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T10:21:14.385040+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.10% price=83662.2
- Funnel: target 1097 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +64.27% | $16,929,536.57 |
| CT/USDT:USDT | +28.89% | $5,504,976.51 |
| NOM/USDT:USDT | +23.36% | $2,447,910.33 |
| LONGXIA/USDT:USDT | +23.21% | $2,489,080.84 |
| NIGHT/USDT:USDT | +20.38% | $8,429,535.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +1.94% | +2.04% |
| MOVR/USDT:USDT | below_1h_threshold | +1.91% | +2.01% |
| NIGHT/USDT:USDT | below_1h_threshold | +1.57% | +1.67% |
| BTW/USDT:USDT | below_1h_threshold | +0.84% | +0.94% |
| ACNSTOCK/USDT:USDT | below_1h_threshold | +0.61% | +0.71% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
