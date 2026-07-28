# Decision Report

- generated_at: 2026-07-28T01:51:30.646579+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9665**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9665, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.03% | **-1.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 8/18 | 44.4% | +2.58% | **+1.15%** |
| LIMIT_10PCT | 2/20 | 10.0% | +6.73% | **+0.67%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 4/20 | 20.0% | +1.78% | **+0.36%** |
| LIMIT_ATR | 16/20 | 80.0% | +0.41% | **+0.33%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +3.78% | **+1.32%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +5.70% | **+0.85%** |
| LIMIT_FIB1272_LONG | 8/20 | 40.0% | +2.03% | **+0.81%** |
| MARKET_LONG | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +2.53% | **+0.63%** |

## 2. $100 Live Portfolio

- 残高: **$106.92** / 初期 $100.00 (+6.92%)
- 確定トレード: 148件 (TP 51 / SL 92 / EXP 5)
- 最新: BANK/USDT:USDT TP_HIT PnL +8.00% 残高後 $106.92
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$461.56** / 初期 $100.00 (+361.56%)
- 確定: 3435件 (Win 1088 / Loss 1118 / Flat 1229) / skip 2791件
- 成長率目線: 平均log +0.000445 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COTI/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $461.56

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1224件 (Win 338 / Loss 275 / Flat 611) / skip 1852件
- 成長率目線: 平均log +0.000259 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SOXS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$108.41** / 初期 $100.00 (+8.41%)
- 確定: 685件 (Win 223 / Loss 261 / Flat 201) / pending 3件 / skip 447件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000184 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $108.41

## 6. Latest Market Context

- 更新: 2026-07-28T01:51:19.364550+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.32% price=63249.2
- Funnel: target 902 → liquid 179 → pre 50 → checked 50 → surge 3 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.7 >= 65=1, 4h RSI 94.6 >= 65=1
- データ欠損注意: funding_rate 0%, open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| COTI/USDT:USDT | +52.15% | $8,915,938.72 |
| RIF/USDT:USDT | +14.07% | $7,322,154.23 |
| SOONNETWORK/USDT:USDT | +11.63% | $1,344,142.38 |
| ALLO/USDT:USDT | +8.74% | $5,502,426.35 |
| DEXE/USDT:USDT | +8.54% | $15,091,804.04 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.44% | +3.76% |
| SOONNETWORK/USDT:USDT | below_1h_threshold | +2.21% | +2.53% |
| ALLO/USDT:USDT | below_1h_threshold | +1.85% | +2.17% |
| KAITO/USDT:USDT | below_1h_threshold | +1.83% | +2.15% |
| ESPORTS/USDT:USDT | below_1h_threshold | +1.76% | +2.08% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
