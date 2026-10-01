# Decision Report

- generated_at: 2026-10-01T10:56:34.024282+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15896**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15896, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.68% | **-1.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 11/20 | 55.0% | +0.95% | **+0.52%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_FIB1272 | 2/20 | 10.0% | +0.56% | **+0.06%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.05% | **+0.04%** |
| LIMIT_ATR | 17/20 | 85.0% | +0.03% | **+0.03%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/9 | 77.8% | +3.32% | **+2.58%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.22% | **+2.00%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +2.55% | **+1.66%** |
| MARKET_LONG | 20/20 | 100.0% | +1.62% | **+1.62%** |
| LIMIT_8PCT_LONG | 3/20 | 15.0% | +5.33% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,294.35** / 初期 $100.00 (+1194.35%)
- 確定: 6014件 (Win 1781 / Loss 1934 / Flat 2299) / skip 6443件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CT/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,294.35

## 4. Robust Adaptive DryRun ($100)

- 残高: **$270.09** / 初期 $100.00 (+170.09%)
- 確定: 3549件 (Win 982 / Loss 815 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000280 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1419 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CT/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $270.09

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4056件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000338 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T10:56:21.117093+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=83977.1
- Funnel: target 1097 → liquid 177 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +66.87% | $17,315,753.17 |
| LONGXIA/USDT:USDT | +47.11% | $3,028,524.77 |
| NOM/USDT:USDT | +29.38% | $2,579,255.53 |
| NIGHT/USDT:USDT | +22.82% | $8,948,403.95 |
| CT/USDT:USDT | +21.87% | $6,338,799.66 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CT/USDT:USDT | below_1h_threshold | +4.75% | +4.47% |
| MOVR/USDT:USDT | below_1h_threshold | +3.53% | +3.25% |
| NIGHT/USDT:USDT | below_1h_threshold | +3.52% | +3.24% |
| NOM/USDT:USDT | below_1h_threshold | +2.48% | +2.21% |
| BR/USDT:USDT | below_1h_threshold | +2.36% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
