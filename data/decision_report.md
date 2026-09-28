# Decision Report

- generated_at: 2026-09-28T13:41:31.096016+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15725**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15725, expectancy=+0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.48% | **-1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_10PCT | 3/20 | 15.0% | +8.00% | **+1.20%** |
| LIMIT_BB3S | 5/17 | 29.4% | +3.83% | **+1.13%** |
| LIMIT_FIB1272 | 11/20 | 55.0% | +1.57% | **+0.86%** |
| LIMIT_8PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 3/3 | 100.0% | +2.39% | **+2.39%** |
| MARKET_LONG | 20/20 | 100.0% | +1.88% | **+1.88%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +1.25% | **+0.56%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +0.77% | **+0.46%** |
| LIMIT_9PCT_LONG | 2/20 | 10.0% | +4.55% | **+0.45%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,233.41** / 初期 $100.00 (+1133.41%)
- 確定: 5982件 (Win 1766 / Loss 1924 / Flat 2292) / skip 6304件
- 成長率目線: 平均log +0.000420 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: MARSCOIN/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,233.41

## 4. Robust Adaptive DryRun ($100)

- 残高: **$263.08** / 初期 $100.00 (+163.08%)
- 確定: 3534件 (Win 974 / Loss 812 / Flat 1748) / skip 5602件
- 成長率目線: 平均log +0.000274 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: QNT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $263.08

## 5. Causal Adaptive DryRun ($100)

- 残高: **$119.06** / 初期 $100.00 (+19.06%)
- 確定: 3291件 (Win 954 / Loss 1290 / Flat 1047) / pending 6件 / skip 3903件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000170 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BATON/USDT:USDT `MARKET_LONG` TP_HIT account +0.34% 残高後 $119.06

## 6. Latest Market Context

- 更新: 2026-09-28T13:41:21.926550+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.16% price=83681.6
- Funnel: target 1064 → liquid 171 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 67.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SI/USDT:USDT | +75.88% | $1,025,523.72 |
| BATON/USDT:USDT | +55.87% | $1,614,297.49 |
| QNT/USDT:USDT | +32.30% | $328,908,223.08 |
| HBAR/USDT:USDT | +30.85% | $102,790,359.56 |
| MARSCOIN/USDT:USDT | +21.82% | $3,091,782.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SI/USDT:USDT | below_1h_threshold | +4.00% | +3.84% |
| BTW/USDT:USDT | below_1h_threshold | +3.59% | +3.42% |
| NMR/USDT:USDT | below_1h_threshold | +2.34% | +2.18% |
| HBAR/USDT:USDT | below_1h_threshold | +2.22% | +2.06% |
| GRASS/USDT:USDT | below_1h_threshold | +1.99% | +1.83% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
