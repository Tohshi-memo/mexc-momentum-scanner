# Decision Report

- generated_at: 2026-09-22T10:21:21.407719+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15314**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15314, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.23% | **-1.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 12/16 | 75.0% | +3.13% | **+2.35%** |
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 4/20 | 20.0% | +3.42% | **+0.68%** |
| LIMIT_5PCT | 6/20 | 30.0% | +2.13% | **+0.64%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.72% | **+0.32%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +5.18% | **+3.88%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +1.33% | **+0.99%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| MARKET_LONG | 20/20 | 100.0% | +0.83% | **+0.83%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +3.20% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$120.44** / 初期 $100.00 (+20.44%)
- 確定トレード: 216件 (TP 79 / SL 132 / EXP 5)
- 最新: PIEVERSE/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.44
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,186.90** / 初期 $100.00 (+1086.90%)
- 確定: 5805件 (Win 1725 / Loss 1868 / Flat 2212) / skip 6070件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_8PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +1.00% 残高後 $1,186.90

## 4. Robust Adaptive DryRun ($100)

- 残高: **$251.26** / 初期 $100.00 (+151.26%)
- 確定: 3351件 (Win 926 / Loss 779 / Flat 1646) / skip 5374件
- 成長率目線: 平均log +0.000275 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.69% 残高後 $251.26

## 5. Causal Adaptive DryRun ($100)

- 残高: **$123.18** / 初期 $100.00 (+23.18%)
- 確定: 3085件 (Win 907 / Loss 1207 / Flat 971) / pending 6件 / skip 3696件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_5PCT` (selected_by_causal_log_growth) / causal_score +0.000069 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_2PCT_LONG` TP_HIT account +0.34% 残高後 $123.18

## 6. Latest Market Context

- 更新: 2026-09-22T10:21:10.166539+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.27% price=85974.8
- Funnel: target 1056 → liquid 174 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| 4STOCK/USDT:USDT | +61.96% | $2,413,204.21 |
| MUBARAK/USDT:USDT | +36.76% | $3,794,392.72 |
| KERNEL/USDT:USDT | +35.84% | $4,330,903.73 |
| NIL/USDT:USDT | +24.71% | $3,434,290.90 |
| GRASS/USDT:USDT | +22.55% | $3,561,686.48 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MARSCOIN/USDT:USDT | below_1h_threshold | +3.79% | +4.07% |
| NIL/USDT:USDT | below_1h_threshold | +1.98% | +2.26% |
| MUBARAK/USDT:USDT | below_1h_threshold | +1.98% | +2.26% |
| GRASS/USDT:USDT | below_1h_threshold | +1.95% | +2.23% |
| USELESS/USDT:USDT | below_1h_threshold | +1.93% | +2.20% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
