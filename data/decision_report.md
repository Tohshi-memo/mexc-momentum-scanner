# Decision Report

- generated_at: 2026-08-09T18:36:31.359140+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11069**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11069, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.58%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.58% | **-1.58%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +3.23% | **+0.81%** |
| LIMIT_3PCT | 18/20 | 90.0% | +0.39% | **+0.35%** |
| LIMIT_5PCT | 4/20 | 20.0% | +0.95% | **+0.19%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.02% | **+0.01%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +1.66% | **+1.66%** |
| LIMIT_1PCT_LONG | 12/20 | 60.0% | +2.28% | **+1.37%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.88% | **+0.73%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +2.41% | **+0.72%** |
| LIMIT_7PCT_LONG | 4/20 | 20.0% | +3.41% | **+0.68%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 176件 (TP 67 / SL 104 / EXP 5)
- 最新: AAOISTOCK/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$628.11** / 初期 $100.00 (+528.11%)
- 確定: 3931件 (Win 1230 / Loss 1281 / Flat 1420) / skip 3699件
- 成長率目線: 平均log +0.000467 / 幾何平均 +0.047% per trade / maxDD +8.13%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: XAI/USDT:USDT `LIMIT_FIB1272_LONG` SL_HIT account -0.50% 残高後 $628.11

## 4. Robust Adaptive DryRun ($100)

- 残高: **$141.89** / 初期 $100.00 (+41.89%)
- 確定: 1513件 (Win 424 / Loss 361 / Flat 728) / skip 2967件
- 成長率目線: 平均log +0.000231 / 幾何平均 +0.023% per trade / maxDD +3.96%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TST/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.08% 残高後 $141.89

## 5. Causal Adaptive DryRun ($100)

- 残高: **$116.97** / 初期 $100.00 (+16.97%)
- 確定: 1280件 (Win 395 / Loss 492 / Flat 393) / pending 3件 / skip 1262件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000239 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CASHCAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $116.97

## 6. Latest Market Context

- 更新: 2026-08-09T18:36:19.145460+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=65200.0
- Funnel: target 961 → liquid 153 → pre 50 → checked 50 → surge 3 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.4 >= 65=1, 4h RSI 80.9 >= 65=1, 4h RSI 94.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| BMT/USDT:USDT | +37.59% | $12,858,652.57 |
| COOKIE/USDT:USDT | +25.38% | $6,927,527.26 |
| TUT/USDT:USDT | +19.53% | $76,773,929.66 |
| MUBARAK/USDT:USDT | +14.59% | $6,192,269.55 |
| XAN/USDT:USDT | +14.36% | $6,303,971.68 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| TST/USDT:USDT | below_1h_threshold | +3.88% | +3.83% |
| XAN/USDT:USDT | below_1h_threshold | +3.23% | +3.19% |
| CYS/USDT:USDT | below_1h_threshold | +2.63% | +2.59% |
| UB/USDT:USDT | below_1h_threshold | +2.63% | +2.58% |
| VVV/USDT:USDT | below_1h_threshold | +2.36% | +2.31% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
