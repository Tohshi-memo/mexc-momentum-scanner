# Decision Report

- generated_at: 2026-11-21T08:51:27.485791+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **19290**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=19290, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.08% | **+0.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.99% | **+1.69%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +3.77% | **+1.51%** |
| LIMIT_10PCT | 3/20 | 15.0% | +6.45% | **+0.97%** |
| LIMIT_9PCT | 3/20 | 15.0% | +6.45% | **+0.97%** |
| LIMIT_8PCT | 3/20 | 15.0% | +3.34% | **+0.50%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +2.60% | **+1.95%** |
| LIMIT_10PCT_LONG | 4/20 | 20.0% | +6.56% | **+1.31%** |
| LIMIT_4PCT_LONG | 13/20 | 65.0% | +1.74% | **+1.13%** |
| LIMIT_3PCT_LONG | 14/20 | 70.0% | +1.54% | **+1.08%** |
| LIMIT_5PCT_LONG | 10/20 | 50.0% | +2.04% | **+1.02%** |

## 2. $100 Live Portfolio

- 残高: **$121.49** / 初期 $100.00 (+21.49%)
- 確定トレード: 283件 (TP 103 / SL 172 / EXP 8)
- 最新: INTCSTOCK/USDT:USDT TP_HIT PnL +5.26% 残高後 $121.49
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,660.88** / 初期 $100.00 (+1560.88%)
- 確定: 7433件 (Win 2135 / Loss 2397 / Flat 2901) / skip 8418件
- 成長率目線: 平均log +0.000378 / 幾何平均 +0.038% per trade / maxDD +9.04%
- 次の候補: `LIMIT_7PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BLESS/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $1,660.88

## 4. Robust Adaptive DryRun ($100)

- 残高: **$447.64** / 初期 $100.00 (+347.64%)
- 確定: 5095件 (Win 1357 / Loss 1088 / Flat 2650) / skip 7606件
- 成長率目線: 平均log +0.000294 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BLESS/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $447.64

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 7452件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000175 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-21T08:51:13.502014+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.08% price=58013.0
- Funnel: target 1086 → liquid 161 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 79.6 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BLESS/USDT:USDT | +64.30% | $27,951,316.09 |
| CLAUDIA/USDT:USDT | +40.47% | $1,008,261.70 |
| PIEVERSE/USDT:USDT | +17.10% | $4,330,212.26 |
| BTW/USDT:USDT | +17.10% | $4,417,806.47 |
| EVAA/USDT:USDT | +10.27% | $35,707,633.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +4.18% | +4.09% |
| EVAA/USDT:USDT | below_1h_threshold | +3.49% | +3.41% |
| H/USDT:USDT | below_1h_threshold | +2.53% | +2.44% |
| SOXS/USDT:USDT | below_1h_threshold | +1.81% | +1.73% |
| JCT/USDT:USDT | below_1h_threshold | +1.59% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
