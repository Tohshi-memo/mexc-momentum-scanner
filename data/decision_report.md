# Decision Report

- generated_at: 2026-10-01T07:46:16.333244+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15880**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15880, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-0.96%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.96% | **-0.96%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 6/20 | 30.0% | +1.89% | **+0.57%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.38% | **+0.13%** |
| LIMIT_4PCT | 13/20 | 65.0% | -0.31% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 11/20 | 55.0% | +2.51% | **+1.38%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.73% | **+1.30%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.16% | **+1.04%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +2.08% | **+1.04%** |
| LIMIT_FIB1618_LONG | 5/20 | 25.0% | +2.38% | **+0.59%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,247.48** / 初期 $100.00 (+1147.48%)
- 確定: 5999件 (Win 1772 / Loss 1930 / Flat 2297) / skip 6442件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: NOM/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,247.48

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3537件 (Win 974 / Loss 812 / Flat 1751) / skip 5754件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1293 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MOVR/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4038件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000305 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T07:46:04.862033+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.70% price=83492.5
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 76.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +68.33% | $15,023,934.37 |
| NOM/USDT:USDT | +20.90% | $1,305,091.98 |
| MONAD/USDT:USDT | +17.70% | $7,302,241.65 |
| STX/USDT:USDT | +16.13% | $5,473,900.02 |
| NIGHT/USDT:USDT | +12.81% | $7,228,959.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BR/USDT:USDT | below_1h_threshold | +2.26% | +2.96% |
| USOIL/USDT:USDT | below_1h_threshold | +1.46% | +2.16% |
| UKOIL/USDT:USDT | below_1h_threshold | +1.28% | +1.99% |
| JASMY/USDT:USDT | below_1h_threshold | +1.08% | +1.78% |
| CT/USDT:USDT | below_1h_threshold | +1.05% | +1.75% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
