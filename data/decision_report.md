# Decision Report

- generated_at: 2026-10-01T09:46:26.768276+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15885**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15885, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-2.12%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.12% | **-2.12%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +1.89% | **+0.47%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.80% | **+0.42%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.03% | **+0.01%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.22% | **-0.16%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.10% | **+2.07%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +2.47% | **+1.98%** |
| LIMIT_ATR_LONG | 12/20 | 60.0% | +3.27% | **+1.96%** |
| LIMIT_4PCT_LONG | 9/20 | 45.0% | +4.09% | **+1.84%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.42% | **+1.20%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,265.27** / 初期 $100.00 (+1165.27%)
- 確定: 6004件 (Win 1775 / Loss 1931 / Flat 2298) / skip 6442件
- 成長率目線: 平均log +0.000423 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.63% 残高後 $1,265.27

## 4. Robust Adaptive DryRun ($100)

- 残高: **$264.21** / 初期 $100.00 (+164.21%)
- 確定: 3538件 (Win 975 / Loss 812 / Flat 1751) / skip 5758件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1447 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.43% 残高後 $264.21

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4045件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000361 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T09:46:12.149647+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=83818.4
- Funnel: target 1097 → liquid 174 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +62.20% | $17,056,759.75 |
| NOM/USDT:USDT | +31.43% | $2,191,661.31 |
| NIGHT/USDT:USDT | +20.10% | $8,120,521.45 |
| JASMY/USDT:USDT | +18.91% | $7,473,390.65 |
| CT/USDT:USDT | +17.52% | $4,947,840.38 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AR/USDT:USDT | below_1h_threshold | +4.61% | +4.26% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.79% | +3.44% |
| MOVR/USDT:USDT | below_1h_threshold | +3.03% | +2.68% |
| BR/USDT:USDT | below_1h_threshold | +2.06% | +1.71% |
| NOM/USDT:USDT | below_1h_threshold | +1.62% | +1.26% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
