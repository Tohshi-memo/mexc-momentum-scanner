# Decision Report

- generated_at: 2026-10-22T08:36:27.635391+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17129**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17129, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.08% | **-1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_8PCT | 4/20 | 20.0% | +6.93% | **+1.39%** |
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_9PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_BB3S | 6/17 | 35.3% | +0.78% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +1.95% | **+1.66%** |
| LIMIT_FIB1272_LONG | 11/20 | 55.0% | +2.26% | **+1.24%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.90% | **+1.14%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +1.71% | **+1.11%** |
| MARKET_LONG | 20/20 | 100.0% | +1.09% | **+1.09%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 250件 (TP 92 / SL 150 / EXP 8)
- 最新: MSTRSTOCK/USDT:USDT EXPIRED PnL +0.27% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,355.80** / 初期 $100.00 (+1255.80%)
- 確定: 6511件 (Win 1893 / Loss 2076 / Flat 2542) / skip 7179件
- 成長率目線: 平均log +0.000400 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PTB/USDT:USDT `LIMIT_6PCT` TP_HIT account +1.00% 残高後 $1,355.80

## 4. Robust Adaptive DryRun ($100)

- 残高: **$277.63** / 初期 $100.00 (+177.63%)
- 確定: 3839件 (Win 1055 / Loss 899 / Flat 1885) / skip 6701件
- 成長率目線: 平均log +0.000266 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PTB/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.35% 残高後 $277.63

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5288件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000171 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-22T08:36:10.051970+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.34% price=81910.0
- Funnel: target 1090 → liquid 189 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MAGMA/USDT:USDT | +40.09% | $3,346,460.08 |
| AGT/USDT:USDT | +22.09% | $5,249,494.49 |
| PTB/USDT:USDT | +15.18% | $1,423,109.92 |
| SOXS/USDT:USDT | +11.54% | $11,367,846.61 |
| BTW/USDT:USDT | +11.15% | $33,968,020.99 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AGT/USDT:USDT | below_1h_threshold | +4.35% | +4.70% |
| IRYS/USDT:USDT | below_1h_threshold | +2.55% | +2.90% |
| BILL/USDT:USDT | below_1h_threshold | +1.44% | +1.79% |
| SOXS/USDT:USDT | below_1h_threshold | +1.09% | +1.44% |
| SQQQ/USDT:USDT | below_1h_threshold | +0.73% | +1.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
